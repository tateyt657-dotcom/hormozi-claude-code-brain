"""Build roofman-mockup.html: index.html with images embedded as data URIs."""
import base64,re,pathlib,sys
root=pathlib.Path(__file__).resolve().parent.parent
s=(root/'index.html').read_text()
def rep(m):
    p=root/m.group(1); mime='image/png' if p.suffix=='.png' else 'image/jpeg'
    return 'data:%s;base64,%s'%(mime,base64.b64encode(p.read_bytes()).decode())
s=re.sub(r'(assets/[A-Za-z0-9_]+\.(?:png|jpg))',rep,s)
(root/'roofman-mockup.html').write_text(s)
