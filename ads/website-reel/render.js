// Renders reel.html frame by frame and muxes mix.wav into a 1080x1920 MP4.
// Run build_audio.py first (it writes timeline.json and mix.wav).
// Usage: node render.js [out.mp4] [--stills]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const FPS = 30;
const tl = JSON.parse(fs.readFileSync(path.join(__dirname, 'timeline.json'), 'utf8'));
const out = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : path.join(__dirname, 'website-reel.mp4');
const stills = process.argv.includes('--stills');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'reel.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(tl => setup(tl), tl);

  if (stills) {
    const ts = process.argv.filter(a => /^\d+(\.\d+)?$/.test(a)).map(Number);
    for (const t of ts) {
      await page.evaluate(t => render(t), t);
      await page.screenshot({ path: path.join(__dirname, `still-${t}.png`) });
    }
    await browser.close();
    return;
  }

  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error',
    '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-i', path.join(__dirname, 'mix.wav'),
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p',
    '-af', 'loudnorm=I=-14:TP=-1.5:LRA=9', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
    '-shortest', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });

  const frames = Math.round(tl.duration * FPS);
  for (let f = 0; f < frames; f++) {
    await page.evaluate(t => render(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('wrote', out);
})();
