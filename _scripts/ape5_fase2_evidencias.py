"""Capturas de evidencia de la fase 2 (APE 5) en cuatro viewports.

Uso: con un servidor local sirviendo la raíz del repositorio,
    python -m http.server 8766 --directory <repo>
ejecutar:
    python _scripts/ape5_fase2_evidencias.py

Cada página se carga dentro de un iframe del tamaño exacto del viewport (Chrome headless
no permite ventanas de menos de ~500 px). El script del iframe mide
document.documentElement.scrollWidth e innerWidth y los imprime en la captura.
"""
import os, subprocess, json, re
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVID = os.path.join(REPO, 'evidencias')
TMP = os.path.join(REPO, '_scripts', '_tmp')
os.makedirs(EVID, exist_ok=True)
os.makedirs(TMP, exist_ok=True)
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
BASE = 'http://127.0.0.1:8766/'

VIEWPORTS = [(320, 720), (360, 800), (768, 1024), (1366, 768)]

HARNESS = '''<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fff">
<iframe id="f" src="{src}" style="width:{w}px;height:{h}px;border:0;display:block"></iframe>
<pre id="out"></pre>
<script>
const f = document.getElementById('f');
f.addEventListener('load', () => setTimeout(() => {{
  const w = f.contentWindow, d = w.document;
  try {{ w.sessionStorage.clear(); }} catch (e) {{}}
  // Sin transiciones: la captura headless no espera a que terminen (0,2 s).
  const s = d.createElement('style'); s.textContent = '*{{transition:none!important}}'; d.head.appendChild(s);
  {accion}
  setTimeout(() => {{
    const g = d.querySelector('.disposicion');
    document.getElementById('out').textContent = JSON.stringify({{
      innerWidth: w.innerWidth, scrollWidth: d.documentElement.scrollWidth,
      columnas: g ? w.getComputedStyle(g).gridTemplateColumns : null
    }});
  }}, 300);
}}, 300));
</script>'''


def font(sz, bold=False):
    for f in ([r'C:\Windows\Fonts\segoeuib.ttf'] if bold else []) + [r'C:\Windows\Fonts\segoeui.ttf', r'C:\Windows\Fonts\arial.ttf']:
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


def capturar(src, w, h, nombre, accion=''):
    harness = os.path.join(TMP, 'h.html')
    with open(harness, 'w', encoding='utf8') as fh:
        fh.write(HARNESS.format(src=src, w=w, h=h, accion=accion))
    url = BASE + '_scripts/_tmp/h.html'
    raw = os.path.join(TMP, 'raw.png')
    common = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=3000',
              '--window-size=%d,%d' % (w + 220, h + 80)]
    dom = subprocess.run(common + ['--dump-dom', url], capture_output=True, text=True, encoding='utf8').stdout
    m = json.loads(re.search(r'<pre id="out">(.*?)</pre>', dom, re.S).group(1).replace('&quot;', '"'))
    subprocess.run(common + ['--screenshot=' + raw, url], capture_output=True)
    shot = Image.open(raw).convert('RGB').crop((0, 0, w, h))
    desborde = m['scrollWidth'] - m['innerWidth']
    barra = 58
    lienzo = Image.new('RGB', (w, h + barra), '#1f2629' if desborde <= 0 else '#8a1c1c')
    lienzo.paste(shot, (0, barra))
    dr = ImageDraw.Draw(lienzo)
    dr.text((10, 6), 'Viewport %d × %d · desborde %+d px' % (w, h, desborde), fill='white', font=font(16, True))
    dr.text((10, 30), 'scrollWidth %d · innerWidth %d' % (m['scrollWidth'], m['innerWidth']), fill='white', font=font(15))
    destino = os.path.join(EVID, nombre)
    lienzo.save(destino)
    m.update(viewport='%dx%d' % (w, h), desborde=desborde, archivo='evidencias/' + nombre)
    return m


if __name__ == '__main__':
    resultados = []
    for w, h in VIEWPORTS:
        resultados.append(capturar('../../src/index.html', w, h, 'B-%d.png' % w))
    resultados.append(capturar('../../src/index.html', 360, 800, 'B-360-confirmada.png',
                               "d.getElementById('btn-reservar').click();"))
    resultados.append(capturar('../../src/index.html', 1366, 768, 'B-1366-confirmada.png',
                               "d.getElementById('btn-reservar').click();"))
    for w, h in VIEWPORTS:
        resultados.append(capturar('../../prototipos/prototipo-A.html', w, h, 'A-%d.png' % w))
    with open(os.path.join(TMP, 'mediciones.json'), 'w', encoding='utf8') as fh:
        json.dump(resultados, fh, ensure_ascii=False, indent=1)
    for r in resultados:
        print(r['archivo'], r['viewport'], 'sw', r['scrollWidth'], 'iw', r['innerWidth'], 'desborde', r['desborde'], r['columnas'])
