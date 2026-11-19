"""Builds the reel's soundtrack and timeline.

Outputs:
  timeline.json  scene start times, per-word times, beat grid, duration
  mix.wav        voiceover + original music + sound effects, mixed

Needs models/kokoro.onnx and models/voices-v1.0.bin (Kokoro TTS, from
github.com/thewh1teagle/kokoro-onnx releases, tag model-files-v1.0).
"""
import json, os, re
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, resample_poly, fftconvolve

SR = 48000
BPM = 120
BEAT = 60 / BPM
VOICE, SPEED = "bm_george", 1.28
rng = np.random.default_rng(7)

# ---------------------------------------------------------------- script
SCENES = [
    ["UK roofers.", "Lads sat in the van with no work?"],
    ["Word of mouth dries up.", "Homeowners search Google every day."],
    ["One roofer spent two and a half grand on ads.", "Got fifty-eight grand in jobs.", "Three months."],
    ["Jobs guaranteed in ninety days.", "No monthly fee till we hit your target."],
    ["One roofer per area.", "Tap below to check yours."],
]
GAP_SENT, GAP_SCENE, LEAD_IN, TAIL = 0.1, 0.3, 0.15, 1.5

# ---------------------------------------------------------------- helpers
def filt(x, kind, f, order=2):
    return sosfilt(butter(order, f, btype=kind, fs=SR, output="sos"), x)

def env_exp(n, tau):
    return np.exp(-np.arange(n) / (tau * SR))

def place(buf, x, t, gain=1.0):
    i = int(round(t * SR))
    if i < 0:
        x, i = x[-i:], 0
    j = min(len(buf), i + len(x))
    if j > i:
        buf[i:j] += x[: j - i] * gain

def syllables(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    return max(1, len(re.findall(r"[aeiouy]+", w)) - (1 if w.endswith("e") and len(w) > 3 else 0))

def trim(a, thr=0.012, pad=0.02):
    e = np.convolve(np.abs(a), np.ones(240) / 240, "same")
    idx = np.where(e > thr)[0]
    s, t = max(0, idx[0] - int(pad * SR)), min(len(a), idx[-1] + int(pad * SR))
    return a[s:t]

# ---------------------------------------------------------------- voiceover
def build_vo():
    from kokoro_onnx import Kokoro
    md = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    k = Kokoro(os.path.join(md, "kokoro.onnx"), os.path.join(md, "voices-v1.0.bin"))
    t = LEAD_IN
    scenes, clips = [], []
    for si, sents in enumerate(SCENES):
        if si > 0:
            t += GAP_SCENE - GAP_SENT
        sc = {"start": 0.0 if si == 0 else round(t - 0.12, 3), "sentences": []}
        for s in sents:
            a, sr = k.create(s, voice=VOICE, speed=SPEED, lang="en-gb")
            a = trim(resample_poly(a, SR, sr).astype(np.float64))
            dur = len(a) / SR
            words = s.split()
            wts = [syllables(w) + 0.6 for w in words]
            cum = np.concatenate([[0], np.cumsum(wts)]) / sum(wts)
            sc["sentences"].append({
                "text": s, "start": round(t, 3), "end": round(t + dur, 3),
                "words": [{"w": w, "t": round(t + c * dur * 0.97, 3)} for w, c in zip(words, cum[:-1])],
            })
            clips.append((a, t))
            t += dur + GAP_SENT
        scenes.append(sc)
    total = t - GAP_SENT + TAIL
    vo = np.zeros(int(total * SR) + SR)
    for a, st in clips:
        place(vo, a, st)
    # Voice polish: rumble cut, gentle presence lift, soft compression.
    vo = filt(vo, "highpass", 90)
    vo = vo + 0.25 * filt(vo, "bandpass", [2500, 6000])
    vo = vo / np.max(np.abs(vo))
    vo = np.tanh(vo * 1.8) / np.tanh(1.8)
    return vo, scenes, total

# ---------------------------------------------------------------- instruments
def kick():
    n = int(0.45 * SR); tt = np.arange(n) / SR
    f = 45 + 95 * np.exp(-tt / 0.035)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(n, 0.16)
    click = filt(rng.standard_normal(n), "highpass", 3000) * env_exp(n, 0.004) * 0.3
    return np.tanh((body + click) * 1.6)

def clap():
    n = int(0.3 * SR)
    nz = filt(rng.standard_normal(n), "bandpass", [900, 5000])
    e = env_exp(n, 0.06)
    for d in (0.0, 0.011, 0.022):  # three quick hand slaps
        i = int(d * SR); e[i:i + 200] += np.exp(-np.arange(200) / 60)
    tone = np.sin(2 * np.pi * 190 * np.arange(n) / SR) * env_exp(n, 0.04) * 0.4
    return (nz * e * 0.6 + tone)

def hat(open_=False):
    n = int((0.18 if open_ else 0.05) * SR)
    return filt(rng.standard_normal(n), "highpass", 7500) * env_exp(n, 0.06 if open_ else 0.012) * 0.5

def saw(f, n, detune=(0,)):
    tt = np.arange(n) / SR; out = np.zeros(n)
    for d in detune:
        ph = (tt * f * (1 + d)) % 1.0
        out += 2 * ph - 1
    return out / len(detune)

def note(m):
    return 440 * 2 ** ((m - 69) / 12)

# A minor: Am F C G (one chord per bar)
CHORDS = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
ROOTS = [45, 41, 48, 43]

def reverb(x, secs=1.4, mix=0.22):
    n = int(secs * SR)
    ir = rng.standard_normal(n) * env_exp(n, secs / 5)
    ir = filt(ir, "lowpass", 5000)
    wet = fftconvolve(x, ir)[: len(x)]
    wet *= np.max(np.abs(x)) / (np.max(np.abs(wet)) + 1e-9)
    return x * (1 - mix) + wet * mix

def build_music(total, drop_t, open_t):
    N = int(total * SR) + SR
    drums, bass, pad, pluck = (np.zeros(N) for _ in range(4))
    K, C, H, HO = kick(), clap(), hat(), hat(True)
    nbeats = int(total / BEAT) + 1
    kicks = []
    for b in range(nbeats):
        t = b * BEAT
        place(drums, K, t, 0.95); kicks.append(t)
        if b % 2 == 1:
            place(drums, C, t, 0.55)
        place(drums, H, t + BEAT / 2, 0.35)
        if t >= drop_t:  # busier hats after the drop
            place(drums, H, t + BEAT / 4, 0.18); place(drums, H, t + 3 * BEAT / 4, 0.18)
            if b % 4 == 3:
                place(drums, HO, t + BEAT / 2, 0.3)
    bar = 4 * BEAT
    for bi in range(int(total / bar) + 1):
        t0 = bi * bar; ci = bi % 4
        n = int(bar * SR)
        # pad: detuned saws, dark, slow attack
        p = sum(saw(note(m), n, (-0.004, 0, 0.005)) for m in CHORDS[ci])
        att = np.minimum(1, np.arange(n) / (0.25 * SR))
        place(pad, filt(p, "lowpass", 1800) * att * 0.12, t0)
        # bass: eighth-note root pulses
        for e in range(8):
            m = ROOTS[ci] - 12 if e % 2 == 0 else ROOTS[ci]
            nn = int(BEAT / 2 * SR)
            tt = np.arange(nn) / SR
            s = np.sin(2 * np.pi * note(m) * tt) + 0.3 * filt(saw(note(m), nn), "lowpass", 600)
            place(bass, s * env_exp(nn, 0.18) * 0.5, t0 + e * BEAT / 2)
        # pluck arp after drop
        if t0 + bar > drop_t:
            arp = CHORDS[ci] + [CHORDS[ci][0] + 12]
            for s16 in range(16):
                t = t0 + s16 * BEAT / 4
                if t < drop_t:
                    continue
                m = arp[[0, 2, 1, 3][s16 % 4]] + 12
                nn = int(0.25 * SR); tt = np.arange(nn) / SR
                tri = 2 * np.abs(2 * ((tt * note(m)) % 1) - 1) - 1
                place(pluck, tri * env_exp(nn, 0.07) * 0.16, t)
    # sidechain pad and bass to the kick
    sc = np.ones(N)
    for t in kicks:
        i = int(t * SR); n = min(int(0.3 * SR), N - i)
        sc[i:i + n] = np.minimum(sc[i:i + n], 1 - 0.7 * env_exp(n, 0.09))
    mus = drums + (bass + pad) * sc + reverb(pluck, 1.2, 0.3)
    # Story arc: muffled during the problem, opens up, full at the proof drop.
    lo = filt(mus, "lowpass", 650, 4)
    mid = filt(mus, "lowpass", 2200, 4)
    tt = np.arange(N) / SR
    a = np.clip((tt - open_t) / 0.08, 0, 1)
    b = np.clip((tt - drop_t) / 0.05, 0, 1)
    mus = lo * (1 - a) + mid * a * (1 - b) + mus * b
    return mus

# ---------------------------------------------------------------- sound effects
def whoosh(d=0.5):
    n = int(d * SR); x = rng.standard_normal(n)
    y = np.zeros(n); s = 0.0
    for i in range(n):  # rising one-pole lowpass
        a = 0.02 + 0.5 * (i / n) ** 2
        s += a * (x[i] - s); y[i] = s
    e = np.sin(np.pi * np.clip(np.arange(n) / n * 1.1, 0, 1)) ** 2
    return filt(y, "highpass", 200) * e * 1.4

def impact(d=1.4, f0=85):
    n = int(d * SR); tt = np.arange(n) / SR
    f = 32 + f0 * np.exp(-tt / 0.08)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(n, 0.35)
    nz = filt(rng.standard_normal(n), "lowpass", 3000) * env_exp(n, 0.05) * 0.5
    return reverb(np.tanh((boom + nz) * 2.2), 1.6, 0.25)

def tick(f=2200):
    n = int(0.025 * SR)
    return np.sin(2 * np.pi * f * np.arange(n) / SR) * env_exp(n, 0.006)

def key_click():
    n = int(0.03 * SR)
    return filt(rng.standard_normal(n), "bandpass", [1500, 6000]) * env_exp(n, 0.005) * 0.6

def ding(f=1318.5, d=1.6):
    n = int(d * SR); tt = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * r * tt) * env_exp(n, d / k)
            for a, r, k in [(1, 1, 3), (0.5, 2.76, 6), (0.25, 5.4, 10)])
    return reverb(x * 0.5, 1.5, 0.3)

def pop(f0=900, f1=220):
    n = int(0.09 * SR); tt = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-tt / 0.02)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(n, 0.03)

def riser(d):
    n = int(d * SR); tt = np.arange(n) / SR
    f = 180 * 2 ** (2.5 * tt / d)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.25
    nz = filt(rng.standard_normal(n), "highpass", 2500) * 0.35
    return (tone + nz) * (tt / d) ** 2

def stamp():
    return impact(0.9, 140) * 0.9 + np.pad(filt(rng.standard_normal(int(0.08 * SR)), "bandpass", [300, 3000]) * env_exp(int(0.08 * SR), 0.015), (0, int(0.82 * SR)))

# ---------------------------------------------------------------- main
def main():
    vo, scenes, total = build_vo()

    def W(s, j, w):  # time of word w in sentence j of scene s (1-based scene)
        return scenes[s - 1]["sentences"][j]["words"][w]["t"]

    cues = {
        "drop": W(3, 1, 2),          # £58,000 lands on "grand"
        "open": scenes[1]["start"],
        "count_start": W(3, 1, 0),
        "type_start": W(2, 1, 1), "type_end": W(2, 1, 2) + 0.45,
        "pound2500": W(3, 0, 3),
        "chips": [W(3, 2, 0) - 0.44, W(3, 2, 0) - 0.22, W(3, 2, 0)],
        "stamp": W(4, 0, 1), "ninety": W(4, 0, 3),
        "bar_start": W(4, 1, 0), "bar_end": W(4, 1, 7),
        "pin": W(5, 0, 3),
        "cta": W(5, 1, 0),
        "logo": scenes[4]["sentences"][1]["end"] + 0.15,
    }

    mus = build_music(total, cues["drop"], cues["open"])
    sfx = np.zeros_like(mus)
    place(sfx, impact(), W(1, 0, 0) - 0.02, 0.9)
    place(sfx, pop(1200, 300), W(1, 0, 1), 0.35)
    for s in scenes[1:]:
        place(sfx, whoosh(0.5), s["start"] - 0.38, 0.55)
    q = "roofer near me"
    for i in range(len(q)):
        place(sfx, key_click(), cues["type_start"] + i * (cues["type_end"] - cues["type_start"]) / len(q), 0.5)
    place(sfx, pop(), W(3, 0, 3), 0.4)
    t, i = cues["count_start"], 0
    while t < cues["drop"] - 0.05:
        place(sfx, tick(1500 + 60 * i), t, 0.22); t += 0.065; i += 1
    place(sfx, riser(cues["drop"] - cues["count_start"]), cues["count_start"], 0.4)
    place(sfx, impact(1.6, 70), cues["drop"], 1.0)
    place(sfx, ding(1568), cues["drop"], 0.35)
    for k, tt in enumerate(cues["chips"]):
        place(sfx, pop(700 + 150 * k, 250), tt, 0.4)
    place(sfx, stamp(), cues["stamp"], 0.9)
    place(sfx, riser(cues["bar_end"] - cues["bar_start"]), cues["bar_start"], 0.18)
    place(sfx, ding(1318.5), cues["bar_end"], 0.4)
    place(sfx, pop(500, 120), cues["pin"], 0.6)
    place(sfx, impact(0.8, 60), cues["pin"], 0.35)
    for k, f in enumerate([1046.5, 1318.5, 1568, 2093]):
        place(sfx, ding(f, 1.2), cues["cta"] + k * 0.06, 0.16)
    place(sfx, impact(2.0, 60), cues["logo"], 0.6)

    # Duck the music under the voice.
    env = np.convolve(np.abs(vo), np.ones(2400) / 2400, "same")
    duck = np.clip(env / 0.04, 0, 1)
    duck = np.convolve(duck, np.ones(4800) / 4800, "same")
    n = len(vo)
    mus, sfx = mus[:n], sfx[:n]
    mus = mus / np.max(np.abs(mus)) * (1 - 0.55 * duck)
    tt = np.arange(n) / SR
    fade = np.clip((total - tt) / 0.9, 0, 1)
    mix = vo * 1.0 + mus * 0.32 * fade + sfx * 0.5
    mix = mix[: int(total * SR)]
    mix = np.tanh(mix / np.max(np.abs(mix)) * 1.3) * 0.95
    sf.write("mix.wav", np.stack([mix, mix], 1).astype(np.float32), SR)

    beats = [round(b * BEAT, 3) for b in range(int(total / BEAT) + 1)]
    json.dump({"duration": round(total, 3), "bpm": BPM, "beats": beats, "cues": {k: (round(v, 3) if not isinstance(v, list) else [round(x, 3) for x in v]) for k, v in cues.items()},
               "scenes": scenes}, open("timeline.json", "w"), indent=1)
    print(f"duration {total:.2f}s")
    for i, s in enumerate(scenes, 1):
        print(i, s["start"], [x["text"] for x in s["sentences"]])

if __name__ == "__main__":
    main()
