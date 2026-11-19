"""Builds index.html: five fictional roofing firm heroes, all on the Roofman house style
(darkened photo, condensed uppercase headline, 2-step quote form, icon trust strip, motion),
each with its own colourway, layout and header. Run: python3 build.py"""
import pathlib

FIRMS = [
  dict(id="slatewright", name="Slatewright", tag="Roofing &amp; Leadwork", area="Kendal &amp; the Lakes", tel="01632 960418",
       accent="#f2b134", accent_ink="#1a1405", dark="#0f1d2b", img="img/slatewright.jpg", pos="65% 40%",
       ov="linear-gradient(95deg,rgba(10,22,34,.92) 25%,rgba(10,22,34,.6) 55%,rgba(10,22,34,.35))",
       layout="left", header="clear",
       h1="Slate roofs fixed properly. <em>Built to last 60 years.</em>",
       sub="Natural slate repairs and re-roofs by time-served slaters. Free written survey on every job.",
       opts=[("Slate repair","Slipped or broken slates"),("New slate roof","Full re-roof"),("Leadwork","Chimneys, valleys, flashing"),("Not sure","We'll take a look")],
       trust=[("shield","<span class='count' data-to='60'>60</span> YEARS","Natural slate life"),("clock","SINCE <span class='count' data-to='1998'>1998</span>","Family slaters"),("doc","FREE","Written roof survey"),("pin","CUMBRIA","Kendal &amp; the Lakes")]),
  dict(id="ridgeback", name="Ridgeback", tag="Roof Repairs", area="Greater Manchester", tel="0161 496 0731",
       accent="#ffd400", accent_ink="#111", dark="#111214", img="img/ridgeback.jpg", pos="center 35%",
       ov="linear-gradient(265deg,rgba(14,14,16,.92) 30%,rgba(14,14,16,.7) 60%,rgba(14,14,16,.55))",
       layout="right", header="bar",
       h1="Roof leaking? <em>We'll be there today.</em>",
       sub="Call before 2pm for a same-day visit. Tarp up, leak stopped, then a fixed price for the proper fix.",
       opts=[("Leak","Water coming in"),("Storm damage","Tiles or ridge off"),("Flat roof","Garage or extension"),("Something else","Tell us what's up")],
       trust=[("bolt","SAME DAY","Call before 2pm"),("camera","PHOTOS","Of every repair"),("doc","INSURANCE","Claims handled"),("pin","MANCHESTER","And all of GM")]),
  dict(id="halloway", name="Halloway &amp; Sons", tag="Roofing", area="Leeds", tel="0113 496 0254",
       accent="#f3e3c3", accent_ink="#1f3a2c", dark="#16261e", img="img/halloway.jpg", pos="center 45%",
       ov="linear-gradient(180deg,rgba(18,34,26,.78),rgba(18,34,26,.72) 55%,rgba(18,34,26,.9))",
       layout="center", header="centre",
       h1="The roofers your neighbours <em>already use.</em>",
       sub="Three generations of Leeds roofers. We turn up when we say, tidy up after, and explain every job in plain English.",
       opts=[("Roof repair","Leaks, slipped tiles"),("New roof","Full re-roof"),("Guttering","Fascias and soffits"),("Not sure","We'll take a look")],
       trust=[("home","SINCE <span class='count' data-to='1987'>1987</span>","Family-run"),("users","3 GENERATIONS","Of Halloway roofers"),("shield","INSURED","Fully, for every job"),("pin","LEEDS","And West Yorkshire")]),
  dict(id="levelline", name="Levelline", tag="Flat Roofing", area="Birmingham &amp; West Midlands", tel="0121 496 0582",
       accent="#35d0f0", accent_ink="#06233a", dark="#0a2a63", img="img/levelline.jpg", pos="30% 40%",
       ov="linear-gradient(15deg,rgba(6,26,64,.94) 30%,rgba(11,61,145,.55) 70%,rgba(11,61,145,.35))",
       layout="bottom", header="pill",
       h1="A flat roof that stays dry <em>for the next 20 years.</em>",
       sub="Rubber and fibreglass flat roofs for garages, extensions and businesses. Most homes done in one day.",
       opts=[("Rubber (EPDM)","No seams to leak"),("Fibreglass (GRP)","Hard-wearing finish"),("Repair","Leak or blister"),("Not sure","We'll advise")],
       trust=[("bolt","<span class='count' data-to='1'>1</span> DAY","Most home installs"),("shield","<span class='count' data-to='20'>20</span> YEARS","Written guarantee"),("layers","FLAT ROOFS","Only. That's all we do"),("pin","MIDLANDS","Birmingham and around")]),
  dict(id="clearmoss", name="Clearmoss", tag="Roof Care", area="Bristol &amp; Bath", tel="0117 496 0369",
       accent="#9ff0c9", accent_ink="#06302a", dark="#0b3b36", img="img/clearmoss-after.jpg", pos="center",
       ov="none", layout="split", header="minimal",
       h1="Moss off. <em>Roof looking new in a day.</em>",
       sub="Every tile cleared by hand, washed and treated so the moss stays away for years. Most semis from £395.",
       opts=[("Moss removal","Thick moss or lichen"),("Roof clean","Stains and algae"),("Gutters","Cleared and flushed"),("Not sure","We'll take a look")],
       trust=[("leaf","FROM £<span class='count' data-to='395'>395</span>","Most semi-detached"),("clock","<span class='count' data-to='1'>1</span> DAY","Most roofs"),("shield","TREATED","So moss stays away"),("pin","BRISTOL","And Bath")]),
]

ICONS = {
 "shield":'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "doc":'<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h7M9 16h7"/>',
 "pin":'<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "bolt":'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "camera":'<rect x="3" y="6" width="18" height="14" rx="2"/><circle cx="12" cy="13" r="3.5"/><path d="M8 6l1.5-2h5L16 6"/>',
 "home":'<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>',
 "users":'<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="9" r="2.5"/><path d="M15 15c3 0 6 1.5 6 4"/>',
 "layers":'<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "leaf":'<path d="M4 20c0-9 6-15 16-16-1 10-7 16-16 16z"/><path d="M4 20c4-4 7-7 11-10"/>',
}
icon=lambda k,s=26:f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'
PHONE='<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1z"/></svg>'

def logo(f):
    return f'<a class="logo" href="#{f["id"]}"><span class="mark">{icon("home",22)}</span><span>{f["name"]}<small>{f["tag"]}</small></span></a>'
NAV='<ul class="links"><li><a href="#">Services</a></li><li><a href="#">Our Work</a></li><li><a href="#">Prices</a></li><li><a href="#">Areas</a></li></ul>'

def header(f):
    t=f'<a class="tel" href="#">{PHONE}<span>{f["tel"]}</span></a>'
    h=f["header"]
    if h=="clear":   # transparent header sitting on the photo
        return f'<header class="hd hd-clear"><div class="in">{logo(f)}{NAV}{t}</div></header>'
    if h=="bar":     # accent top bar + solid dark header with a call button
        return (f'<div class="topbar"><div class="in"><b>Storm damage? We\'re taking calls now.</b><span>Same-day visits across {f["area"]}</span></div></div>'
                f'<header class="hd hd-solid"><div class="in">{logo(f)}{NAV}<a class="btn sm" href="#">{PHONE} Call {f["tel"]}</a></div></header>')
    if h=="centre":  # white header, logo in the middle
        return (f'<header class="hd hd-white"><div class="in"><ul class="links l"><li><a href="#">Repairs</a></li><li><a href="#">New roofs</a></li></ul>'
                f'{logo(f)}<div class="r"><ul class="links"><li><a href="#">Our Work</a></li></ul>{t}</div></div></header>')
    if h=="pill":    # floating rounded header
        return f'<header class="hd hd-pill"><div class="in"><div class="pill">{logo(f)}{NAV}{t}</div></div></header>'
    return f'<header class="hd hd-min"><div class="in">{logo(f)}<a class="tel ghost" href="#">{PHONE}<span>{f["tel"]}</span></a></div></header>'

def form(f):
    i=f["id"]
    opts="".join(f'<button type="button" class="opt" data-v="{a}" aria-pressed="false"><b>{a}</b><span>{b}</span></button>' for a,b in f["opts"])
    return f'''<div class="qcard" id="q-{i}">
  <form class="qform" novalidate>
    <div class="qhead"><h3>Get your free quote</h3><span class="qstep">Step 1 of 2</span></div>
    <div class="qbar" aria-hidden="true"><i></i></div>
    <fieldset class="p1"><legend>What do you need?</legend><div class="opts">{opts}</div><p class="fine">Takes about 20 seconds. No obligation.</p></fieldset>
    <fieldset class="p2" hidden><legend class="sr">Your details</legend>
      <div class="chosen"><span>You chose: <b class="ch"></b></span><button type="button" class="back">Change</button></div>
      <div class="field"><label for="pc-{i}">Postcode</label><input id="pc-{i}" autocomplete="postal-code" autocapitalize="characters" placeholder="e.g. AB1 2CD"></div>
      <div class="field"><label for="n-{i}">First name</label><input id="n-{i}" autocomplete="given-name"></div>
      <div class="field"><label for="p-{i}">Mobile number</label><input id="p-{i}" type="tel" inputmode="tel" autocomplete="tel" placeholder="07..."></div>
      <button class="btn wide" type="submit">Get my free quote</button>
      <p class="fine done" aria-live="polite"></p>
    </fieldset>
    <div class="callalt">Rather talk? Call free on <b>{f["tel"]}</b></div>
  </form>
</div>'''

def trust(f):
    cells="".join(f'<div>{icon(ic)}<b>{big}</b><span>{small}</span></div>' for ic,big,small in f["trust"])
    return f'<div class="trust"><div class="in">{cells}</div></div>'

def hero(n,f):
    style=f'--accent:{f["accent"]};--accent-ink:{f["accent_ink"]};--dark:{f["dark"]};--img:url({f["img"]});--pos:{f["pos"]};--ov:{f["ov"]}'
    copy=f'''<div class="copy"><h1>{f["h1"]}</h1><p class="sub">{f["sub"]}</p><a class="seework" href="#">See our work <span aria-hidden="true">&rarr;</span></a></div>'''
    if f["layout"]=="split":
        body=f'''<div class="split"><div class="panel"><div class="panel-in">{copy}{form(f)}</div></div><div class="photo"><div class="bg"></div></div></div>'''
        return f'''<section class="firm lay-split hdr-{f["header"]}" id="{f["id"]}" style="{style}" aria-label="Concept {n}: {f["name"]}">{header(f)}{body}{trust(f)}</section>'''
    body=f'<div class="in grid">{copy}{form(f)}</div>'
    return (f'<section class="firm lay-{f["layout"]} hdr-{f["header"]}" id="{f["id"]}" style="{style}" aria-label="Concept {n}: {f["name"]}">'
            f'<div class="hero"><div class="bg"></div><div class="ov"></div>{header(f)}{body}</div>{trust(f)}</section>')

LABEL={"left":"Text left, form right","right":"Form left, text right","center":"Centred text, wide form","bottom":"Text low, form overlaps strip","split":"Split screen"}
HDR={"clear":"See-through header","bar":"Top bar + solid header","centre":"Centred logo header","pill":"Floating pill header","minimal":"Minimal header"}

css=pathlib.Path(__file__).with_name('style.css').read_text()
js=pathlib.Path(__file__).with_name('app.js').read_text()
sections="".join(f'''<div class="in label"><b>Concept {n}</b><span>{f["name"]} {f["tag"]}</span><span>{f["area"]}</span><span>{LABEL[f["layout"]]}</span><span>{HDR[f["header"]]}</span></div>
<div class="in"><div class="frame">{hero(n,f)}</div></div>
''' for n,f in enumerate(FIRMS,1))
html=f'''<title>Roofing Hero Concepts</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@600;700;800&display=swap" rel="stylesheet">
<style>{css}</style>
<div class="in intro"><h1>Roofing hero concepts</h1><p>Five fictional UK roofing firms on the same proven homepage design: darkened roof photo, bold headline, 2-step quote form and trust strip. Each has its own colours, layout and header. Names and numbers are made up; the phone numbers use Ofcom's drama ranges, so they ring no one.</p></div>
{sections}
<div class="in foot">All five businesses are fictional, made for portfolio and pitch use. Photos are public domain (CC0) from rawpixel and the WordPress Photo Directory.</div>
<script>{js}</script>'''
pathlib.Path(__file__).with_name('index.html').write_text(html)
print('built index.html', len(html)//1024, 'KB')
