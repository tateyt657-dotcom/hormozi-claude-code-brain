# Roof build scroll video: plan

## How it works

The effect is a scroll-scrubbed image sequence, the same trick Apple uses on its product pages. You turn a video into about 150 to 180 still frames. As the visitor scrolls, the page draws the matching frame on a canvas, so scrolling down "plays" the roof build and scrolling up rewinds it.

Note: the 3D and illustrated animations were removed from `index.html`. The page now uses a scroll photo story built from real job photos. If he films a timelapse, the frames can be added back as a new scroll section.

## The correct build order (UK pitched roof)

Note: felt (membrane) goes on **before** the battens. The battens are nailed on top of it.

1. Scaffold up, old roof in view (mossy, slipped tiles)
2. Strip old tiles from the ridge down
3. Remove old felt and old battens
4. Inspect rafters, replace any rotten timber
5. Fit eaves protection, then roll out breathable membrane from the eaves up, each run overlapping the last by about 150mm
6. Fix new treated battens at the gauge for the tile (counter battens first if the spec needs them)
7. Load out tiles, then lay them course by course from the eaves up, with verges done as you go
8. Fit ridge tiles (dry ridge or mortar)
9. Clear gutters and site, scaffold down, finished roof

## Three ways to get "ultra realistic" footage

### Option A: real timelapse of his next job (recommended)

This is the most realistic and the most honest. It's his real team on a real roof.

- Kit: a GoPro or old phone in a weatherproof case, clamped to a scaffold pole or a pole in the garden opposite. Add a power bank.
- Lock the camera. It must not move for the whole job. Frame the full roof slope with the gutter in shot.
- Shoot one photo every 10 to 20 seconds while the team works. A 3 to 5 day job gives a few thousand photos.
- Pick about 180 frames so each step gets screen time (more frames for tiling, fewer for scaffolding).
- Cost: about £0 to £150 for kit. Ask him to set it up on his next new roof.

### Option B: AI-generated video (fastest, but must be labelled)

Generate it with an image-to-video model such as Google Veo, Kling or Runway. Use **first frame / last frame** mode so each clip starts exactly where the last one ended.

1. Make one locked-off still for each stage with the same house, camera and light. Make the first still, then use it as the reference for every next one so nothing drifts.
2. Generate a clip between each pair of stills (8 clips).
3. Join the clips and cut frames (commands below).

Base prompt to put at the start of every still and clip:

> Photorealistic, static locked-off camera, elevated three-quarter view from scaffold height looking at one pitched roof slope of a 1930s red-brick semi-detached house in Staffordshire, England. Overcast soft daylight, no camera movement, no lens change, 35mm, natural colour, documentary style, sharp detail.

Stage prompts to add after it:

1. "Old concrete tiles covered in thick green moss and lichen, a few slipped and broken tiles, blocked gutter, steel scaffold along the eaves."
2. "Two roofers in hi-vis vests and hard hats strip the old tiles from the ridge downwards, stacking them on the scaffold, top half of the roof now bare."
3. "Roof fully stripped. Old black bitumen felt and old battens being pulled off, exposing the timber rafters."
4. "Bare timber rafters exposed, a roofer checking them, one new pale timber rafter replacing a dark rotten one."
5. "Grey breathable roofing membrane being rolled out horizontally from the gutter upwards, each run overlapping the one below, stapled to the rafters."
6. "New treated timber battens being nailed horizontally across the membrane at even spacing from eaves to ridge."
7. "New smooth grey concrete interlocking tiles being laid course by course from the gutter upwards, lower half finished, upper half still showing battens and membrane."
8. "All tiles laid, a roofer fitting half-round ridge tiles along the top."
9. "Finished new roof, clean gutters, scaffold removed, same camera angle, slightly brighter light."

Negative prompt: "camera shake, zoom, pan, cuts, people facing camera, text, logos, warped tiles, melting geometry".

**Important:** don't present AI footage as one of his real jobs. Put a small line under it such as "Illustration of our new roof process". Fake job footage on a trade site breaks consumer protection rules and kills trust if someone spots it. Swap in real footage (Option A) once he has it.

### Option C: 3D render in Blender

Full control, perfect consistency and no AI artefacts. It needs a 3D artist and costs about £300 to £1,500. Only worth it if he wants this as a big ad asset.

## Turning the video into frames

Install ffmpeg, then:

```bash
ffmpeg -i roof-build.mp4 -vf "fps=180/DURATION,scale=1600:-2" -c:v libwebp -quality 72 frames/roof_%04d.webp
```

Replace `DURATION` with the video length in seconds. For a folder of timelapse photos, pick about 180 evenly spaced ones and convert them:

```bash
ls photos/*.jpg | awk 'NR % 20 == 1' | head -180 | nl -nrz -w4 | while read n f; do ffmpeg -loglevel error -i "$f" -vf scale=1600:-2 -quality 72 "frames/roof_$n.webp"; done
```

Aim for 60 to 120KB per frame (about 10 to 20MB total). Serve a 900px-wide set on phones to keep it fast.

## Recommendation

Ship the site with the built-in illustrated version now. It works today, costs nothing and loads instantly. Then sell the real timelapse as part of the £50/month: "We'll film your next roof and turn it into the animation." That makes the monthly fee feel like ongoing marketing, not hosting.
