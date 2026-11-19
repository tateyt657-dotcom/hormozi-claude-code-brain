"""Build roofman-mockup.html: index.html with every image and photo texture embedded, so one file works offline."""
import base64,re,pathlib,json
root=pathlib.Path(__file__).resolve().parent.parent
s=(root/'index.html').read_text()
uri=lambda p:'data:%s;base64,%s'%('image/png' if p.suffix=='.png' else 'image/jpeg',base64.b64encode(p.read_bytes()).decode())
s=re.sub(r'(assets/[A-Za-z0-9_]+\.(?:png|jpg))',lambda m:uri(root/m.group(1)),s)
def small(p,w):
    # the single file is for sending around, so heavy images go in at a lower resolution
    import io;from PIL import Image
    im=Image.open(p);im.thumbnail((w,w));b=io.BytesIO();im.convert('RGB').save(b,'JPEG',quality=78)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
tex={p.name:(small(p,2048) if p.name=='sky_4k.jpg' else small(p,768)) for p in sorted((root/'textures').glob('*.jpg'))}
s=s.replace('<script src="https://cdnjs','<script>window.ROOF_TEX='+json.dumps(tex)+';</script>\n<script src="https://cdnjs',1)
(root/'roofman-mockup.html').write_text(s)
print('roofman-mockup.html',round(len(s)/1e6,1),'MB')
