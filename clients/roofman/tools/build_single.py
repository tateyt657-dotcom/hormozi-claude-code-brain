"""Build roofman-mockup.html: index.html with every image and photo texture embedded, so one file works offline."""
import base64,re,pathlib,json
root=pathlib.Path(__file__).resolve().parent.parent
s=(root/'index.html').read_text()
uri=lambda p:'data:%s;base64,%s'%('image/png' if p.suffix=='.png' else 'image/jpeg',base64.b64encode(p.read_bytes()).decode())
s=re.sub(r'(assets/[A-Za-z0-9_]+\.(?:png|jpg))',lambda m:uri(root/m.group(1)),s)
(root/'roofman-mockup.html').write_text(s)
print('roofman-mockup.html',round(len(s)/1e6,1),'MB')
