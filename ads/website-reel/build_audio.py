"""Soundtrack + timeline for the "Your website is losing you jobs" reel.

Reuses the voice, music and sound-effect engine in ../powell-reel/build_audio.py.
Outputs timeline.json and mix.wav in this folder.
"""
import json, os, sys
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "powell-reel"))
import build_audio as ba  # noqa: E402
from build_audio import SR, place, filt, impact, whoosh, pop, ding, key_click, rng  # noqa: E402

ba.SCENES = [
    ["Your website is losing you jobs."],
    ["A homeowner searches for a roofer.", "They click you first."],
    ["It's slow.", "The text is tiny.", "No reviews."],
    ["So they hit back, and click your competitor."],
    ["Loads fast.", "Five-star reviews.", "One tap to call."],
    ["They ring them.", "Not you."],
    ["Book a free growth audit.", "We'll show you what's costing you jobs."],
]
ba.GAP_SCENE, ba.TAIL = 0.34, 1.8

def buzz():
    n = int(0.11 * SR); tt = np.arange(n) / SR
    sq = np.sign(np.sin(2 * np.pi * 98 * tt)) * 0.5 + np.sign(np.sin(2 * np.pi * 104 * tt)) * 0.5
    one = filt(sq, "lowpass", 1800) * np.minimum(1, (n - np.arange(n)) / 400)
    return np.concatenate([one, np.zeros(int(0.04 * SR)), one])

def tap():
    p = pop(1400, 600); n = len(p)
    return filt(rng.standard_normal(n), "bandpass", [2000, 7000]) * np.exp(-np.arange(n) / (0.004 * SR)) * 0.7 + p * 0.3

def ringback(d):
    """UK ringback: 400+450 Hz, 0.4 on, 0.2 off, 0.4 on, 2.0 off."""
    n = int(d * SR); tt = np.arange(n) / SR
    tone = (np.sin(2 * np.pi * 400 * tt) + np.sin(2 * np.pi * 450 * tt)) * 0.5
    ph = tt % 3.0
    gate = ((ph < 0.4) | ((ph > 0.6) & (ph < 1.0))).astype(float)
    gate = np.convolve(gate, np.ones(240) / 240, "same")
    return filt(tone * gate, "bandpass", [300, 3400]) * 0.6

def main():
    os.chdir(HERE)
    vo, scenes, total = ba.build_vo()

    def W(s, j, w):
        return scenes[s - 1]["sentences"][j]["words"][w]["t"]

    S = lambda i: scenes[i - 1]["start"]
    cues = {
        "phone_in": 0.45,
        "tap1": W(2, 1, 1), "old_in": W(2, 1, 1) + 0.25,
        "loaded": W(3, 0, 1) + 0.35,
        "bad": [W(3, 0, 1), W(3, 1, 3), W(3, 2, 1)],
        "back": W(4, 0, 3), "tap2": W(4, 0, 5), "new_in": W(4, 0, 5) + 0.2,
        "good": [W(5, 0, 1), W(5, 1, 0), W(5, 2, 1)],
        "tap3": W(5, 2, 3),
        "ring": W(6, 0, 1) - 0.1, "notyou": W(6, 1, 0),
        "cta": S(7), "button": W(7, 0, 4), "logo": scenes[6]["sentences"][1]["end"] + 0.1,
    }

    mus = ba.build_music(total, 0.0, 0.0)  # full arrangement throughout
    n = len(vo)
    mus = mus[:n] if len(mus) >= n else np.pad(mus, (0, n - len(mus)))
    tt = np.arange(n) / SR
    # Story arc: music sours (muffled) on your old site, comes back on the
    # competitor's site, cuts out on "Not you", returns for the CTA.
    lo = filt(mus, "lowpass", 500, 4)
    sour = np.clip((tt - cues["old_in"]) / 0.1, 0, 1) * (1 - np.clip((tt - cues["new_in"]) / 0.1, 0, 1))
    mus = mus * (1 - sour) + lo * sour
    gap = np.clip((tt - cues["notyou"]) / 0.03, 0, 1) * (1 - np.clip((tt - cues["cta"]) / 0.05, 0, 1))
    mus *= 1 - gap

    sfx = np.zeros(n)
    place(sfx, impact(), W(1, 0, 3) - 0.02, 0.9)          # "losing"
    place(sfx, whoosh(0.45), cues["phone_in"] - 0.25, 0.5)
    for i in range(2, 8):
        if i not in (3, 5, 6):
            place(sfx, whoosh(0.45), S(i) - 0.35, 0.4)
    q = "roofer near me"
    for i in range(len(q)):
        place(sfx, key_click(), S(2) + 0.25 + i * 0.045, 0.45)
    for k in ("tap1", "tap2", "tap3"):
        place(sfx, tap(), cues[k], 0.7)
    for t in cues["bad"]:
        place(sfx, buzz(), t, 0.35)
    place(sfx, whoosh(0.35), cues["back"] - 0.15, 0.4)
    place(sfx, whoosh(0.3), cues["new_in"] - 0.2, 0.35)
    for k, t in enumerate(cues["good"]):
        place(sfx, ding(1318.5 * 2 ** (k * 4 / 12), 1.0), t, 0.22)
    place(sfx, ringback(cues["notyou"] - cues["ring"]), cues["ring"], 0.45)
    place(sfx, impact(1.8, 50), cues["notyou"], 1.0)
    for k, f in enumerate([1046.5, 1318.5, 1568, 2093]):
        place(sfx, ding(f, 1.2), cues["button"] + k * 0.06, 0.16)
    place(sfx, impact(2.0, 60), cues["logo"], 0.6)

    env = np.convolve(np.abs(vo), np.ones(2400) / 2400, "same")
    duck = np.convolve(np.clip(env / 0.04, 0, 1), np.ones(4800) / 4800, "same")
    mus = mus / np.max(np.abs(mus)) * (1 - 0.55 * duck)
    fade = np.clip((total - tt) / 0.9, 0, 1)
    mix = (vo + mus * 0.32 * fade + sfx * 0.5)[: int(total * SR)]
    mix = np.tanh(mix / np.max(np.abs(mix)) * 1.3) * 0.95
    sf.write("mix.wav", np.stack([mix, mix], 1).astype(np.float32), SR)

    beats = [round(b * ba.BEAT, 3) for b in range(int(total / ba.BEAT) + 1)]
    rnd = lambda v: [round(x, 3) for x in v] if isinstance(v, list) else round(v, 3)
    json.dump({"duration": round(total, 3), "bpm": ba.BPM, "beats": beats,
               "cues": {k: rnd(v) for k, v in cues.items()}, "scenes": scenes},
              open("timeline.json", "w"), indent=1)
    print(f"duration {total:.2f}s")
    for i, s in enumerate(scenes, 1):
        print(i, s["start"], [x["text"] for x in s["sentences"]])
    print(json.dumps({k: rnd(v) for k, v in cues.items()}))

if __name__ == "__main__":
    main()
