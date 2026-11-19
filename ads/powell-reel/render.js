// Renders reel.html frame by frame into a 1080x1920 MP4.
// Usage: node render.js [out.mp4] [--stills]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');

const FPS = 30, DUR = 20;
const out = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : path.join(__dirname, 'powell-reel.mp4');
const stills = process.argv.includes('--stills');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'reel.html'));
  await page.evaluate(() => document.fonts.ready);

  if (stills) {
    for (const t of [1.5, 2.6, 5.8, 8.4, 10.8, 13.2, 15.6, 19.0]) {
      await page.evaluate(t => render(t), t);
      await page.screenshot({ path: path.join(__dirname, `still-${t}.png`) });
    }
    await browser.close();
    return;
  }

  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error',
    '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-shortest', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });

  for (let f = 0; f < FPS * DUR; f++) {
    await page.evaluate(t => render(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('wrote', out);
})();
