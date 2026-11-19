"""Build a de-branded demo copy (placeholder brand, no real photos or reviews) for sharing as a link.
Usage: python3 tools/build_demo.py OUTPUT.html"""
import re,sys,pathlib
root=pathlib.Path(__file__).resolve().parent.parent
s=(root/'index.html').read_text()
s=re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>\s*','',s,flags=re.I)
s=re.sub(r'<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*','',s)
s=s.replace('</head>\n<body>','').replace('</body>\n</html>','')
s=re.sub(r'<title>.*?</title>','<title>Roofer Homepage Demo</title>',s)
s=s.replace('<img src="assets/logo.png" alt="Roofman Nationwide">','<span class="txtlogo"><b>Your</b>Roofing Co</span>')
s=s.replace('header img{height:40px;width:auto}','header img{height:40px;width:auto}\nheader a{text-decoration:none}\n.txtlogo{font-family:"Barlow Condensed";font-weight:800;font-size:30px;color:var(--slate)}.txtlogo b{color:var(--green)}')
s=s.replace('header img{height:30px}','.txtlogo{font-size:24px}')
s=s.replace('background:url(assets/RoofCleaning1after.jpg) center 30%/cover;opacity:.38','background:repeating-linear-gradient(170deg,#3a3f42 0 18px,#2d3235 18px 22px);opacity:.5')
ph=lambda t:f'<div class="ph">{t}</div>'
s=re.sub(r'<img src="assets/RoofCleaning1before.jpg"[^>]*>',ph('Before photo goes here'),s)
s=re.sub(r'<img src="assets/[A-Za-z0-9]+\.jpg"[^>]*>',ph('Real job photo goes here'),s)
s=s.replace('/* Gallery */','.ph{aspect-ratio:4/3;display:grid;place-items:center;text-align:center;padding:16px;background:repeating-linear-gradient(45deg,#e4e9e1 0 12px,#edf1ea 12px 24px);color:var(--slate);font-weight:700}\n/* Gallery */')
s=re.sub(r'<blockquote>.*?</blockquote>\s*<cite>.*?</cite>','<blockquote>"My best quote was <mark>£9,000</mark>. These lads did it for a quarter of the price!"</blockquote><cite>Sample review: swap in a real customer quote</cite>',s,flags=re.S)
s=re.sub(r'<div class="rev">.*?</div>(?=\s*(<div class="rev">|</div>\s*</div></section>))','<div class="rev"><div class="stars">★★★★★</div><p>"Sample review. Your real customer quote goes here, with their first name and town."</p><b>Customer name</b><small>Town</small></div>',s,flags=re.S)
rep={'0800 038 5724':'0800 000 0000','tel:08000385724':'tel:08000000000','Chris or one of the team':'One of the team','Family team from Leek, Staffs':'Local family team',
 'Based in Leek, Staffordshire, with teams travelling nationwide.':'Local teams covering towns across the UK.',
 'Roofman Ltd. Leek, Staffordshire, ST13 5LS':'Your Roofing Co','hello@roofman.co.uk':'hello@yourroofingco.co.uk','Mock-up preview':'Demo: placeholder brand',
 '<a href="#">Leek</a>':'','<a href="#">Alderley Edge</a>':'','We cover over 900 towns across the UK':'We cover towns across the UK',
 'Then the roof gets cleaned':'Then your roof gets cleaned','The Roofman promise':'Our promise'}
for a,b in rep.items(): s=s.replace(a,b)
left=re.findall(r'(?i)roofman|leek|chris|harrison|lawton|neil|assets/|ST13|038 5724',s)
if left: sys.exit(f'Leftover identifiers: {set(left)}')
pathlib.Path(sys.argv[1]).write_text(s)
