"""Informe final APE 5 (fase 2) · formato UTA · Grupo 5.

Uso: python _scripts/ape5_fase2_build.py
Lee los datos de resultados/checklist.md (tabla de observación) y docs/preguntas.md (acta),
así que basta con completar esos archivos después de la clase y volver a ejecutarlo.
Genera 06_documento/APE5_Fase2_Informe_Final.docx (y .pdf si Word está disponible).
"""
import os, re, sys, json, subprocess
sys.path.insert(0, 'C:/Users/henry/Documents/UTA/IHC/APE4/_scripts')
from docx_lib import Doc, TNR, run
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
EV = REPO + 'evidencias/'
DOC = REPO + '06_documento/'
W = os.environ.get('TEMP', '/tmp').replace('\\', '/') + '/ape5/fase2/'
os.makedirs(W, exist_ok=True)
os.makedirs(DOC, exist_ok=True)
REPO_URL = 'https://github.com/Hlagua/APE5_IHC'
PEND = '[completar en clase]'


# ---------- lectura de datos de clase ----------
def leer(p):
    return open(REPO + p, encoding='utf8').read()


def vacio(s):
    s = (s or '').strip()
    return s == '' or set(s) <= set('_ ')


def observaciones():
    t = leer('resultados/checklist.md')
    sec = t.split('## 4. Tabla de observación', 1)[1].split('## 5.', 1)[0]
    filas = []
    for line in sec.splitlines():
        if re.match(r'^\|\s*P-\d+', line):
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            filas.append(c)
    return filas


def resumen_obs(filas):
    datos = [f for f in filas if not vacio(f[4])]
    if not datos:
        return None
    num = lambda s: float(s.replace(',', '.'))
    tB = [num(f[4]) for f in datos if f[2] == 'B']
    return {'n': len(datos), 'nB': len(tB), 'tB': (sum(tB) / len(tB)) if tB else None,
            'err': sum(num(f[5]) for f in datos if not vacio(f[5])),
            'ayu': sum(num(f[6]) for f in datos if not vacio(f[6]))}


def acta():
    t = leer('docs/preguntas.md')
    partes = re.split(r'^## ', t, flags=re.M)
    out = []
    for titulo in ('Pregunta técnica 1', 'Pregunta técnica 2', 'Objeción de diseño'):
        p = next(x for x in partes if x.startswith(titulo))
        reg = p.split('**Registro en la sesión:**', 1)[1]
        def campo(et):
            m = re.search(re.escape(et) + r'\s*(.*?)(?:·|\n)', reg)
            v = m.group(1).strip() if m else ''
            return PEND if vacio(v) else v
        val = re.findall(r'[☒✔]\s*([^☐☒✔\n]+)', reg.split('Valoración', 1)[1])
        out.append([titulo,
                    campo('Pregunta textual de G3:') if 'Pregunta' in titulo else campo('Objeción textual de G3:'),
                    campo('Respuesta dada por (integrante):'),
                    val[0].strip() if val else PEND])
    return out


OBS = observaciones()
RES = resumen_obs(OBS)
ACTA = acta()
MED = json.load(open(REPO + '_scripts/_tmp/mediciones.json', encoding='utf8'))
M = {m['archivo'].split('/')[-1]: m for m in MED}


# ---------- figuras compuestas ----------
def font(sz, bold=False):
    for f in ([r'C:\Windows\Fonts\segoeuib.ttf'] if bold else []) + [r'C:\Windows\Fonts\segoeui.ttf']:
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


def fila(archivos, dest, alto=760, gap=28, pad=20):
    ims = []
    for a in archivos:
        im = Image.open(EV + a).convert('RGB')
        ims.append(im.resize((int(im.width * alto / im.height), alto)))
    w = sum(i.width for i in ims) + gap * (len(ims) - 1) + 2 * pad
    lienzo = Image.new('RGB', (w, alto + 2 * pad), 'white')
    x = pad
    for im in ims:
        lienzo.paste(im, (x, pad))
        ImageDraw.Draw(lienzo).rectangle([x - 1, pad - 1, x + im.width, pad + im.height], outline='#9aa3a7', width=2)
        x += im.width + gap
    lienzo.save(dest)
    return dest


F_A = fila(['A-320.png', 'A-360.png', 'A-768.png'], W + 'fig_A.png')
F_MOV = fila(['B-320.png', 'B-360.png', 'B-360-confirmada.png'], W + 'fig_B_movil.png')
F_ESC = fila(['B-768.png', 'B-1366-confirmada.png'], W + 'fig_B_escritorio.png', alto=700)

# ---------- documento ----------
d = Doc(W)
E = d.E
out = E[0:3]
out.append(d.replace_t(E[3], 'Refactorización con SOLID, Clean Architecture y Patrones Creacionales – Tipo B: Venta de motocicletas',
                       'APE 5. Diseño de interfaces web adaptables · Fase 2: validación técnica, pruebas con usuarios y defensa del prototipo · Grupo 5'))
out.append(E[4])
out.append(d.replace_t(E[5], 'Sexto - A', 'Quinto - A'))
out.append(E[6])
for n in ['Cevallos Goyes Melany Saleth', 'Cobos Taco Alison Marcela', 'Ramos Jacome Carlos Giovanni']:
    out.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="3540"/><w:rPr>%s</w:rPr></w:pPr>%s</w:p>' % (TNR, run(n)))
out.append(d.replace_t(E[7], 'Patrones de Software', 'Interacción Humano Computador'))
out.append(d.replace_t(E[8], 'Ing. Alex Maigua, Mg.', 'Ing. Mg. José Caiza'))
out += E[9:16]
out.append(d.listpara('Desarrollar un diseño de interfaces para una aplicación web: transformar el boceto de escritorio de la pantalla de reserva en una interfaz '
                      'adaptable, validarla técnicamente y con personas, y defender sus decisiones de diseño con evidencia.'))
out += E[17:19]
for s in ['Validar la interfaz en 320, 360, 768 y 1366 px midiendo document.documentElement.scrollWidth frente a innerWidth, con 0 px de desborde como criterio.',
          'Observar a compañeros de otro grupo con una consigna neutral, registrando tiempo, errores de navegación, solicitudes de ayuda y dificultades.',
          'Defender ante el grupo retador G3 el punto de corte, la prevención de duplicados y la gestión del foco, e integrar el trabajo en GitHub con 4 Pull Requests revisados.']:
    out.append(d.bullet(s))
out += E[21:23]
out.append(d.replace_t(E[23], 'Presencial', 'Presencial – trabajo grupal'))
out += E[24:30]
for s in ['**Acciones previas:** ingresar al aula virtual; elaborar el trabajo siguiendo las definiciones, conceptos y procesos aprendidos en clase; desarrollar un diseño con los requerimientos establecidos.',
          '**Paso 1.** Revisar el material entregado por el docente sobre la aplicación de HTML5 y CSS.',
          '**Paso 2.** Generar una base de conocimiento debidamente documentada sobre el desarrollo web (repositorio y carpeta docs/).',
          '**Paso 3.** Determinar los requerimientos mínimos para el diseño de una interfaz web (ficha de aplicación).',
          '**Paso 4.** Aplicar las principales características de diseño web adaptativo (Mobile-First, 48rem) y validarlas.',
          '**Paso 5.** Desarrollar una presentación sobre el desarrollo del prototipo (presentacion/index.html).',
          '**Paso 6.** Elaborar las conclusiones del trabajo.',
          '**Paso 7.** Subir el archivo a la plataforma dentro de la fecha indicada.']:
    out.append(d.listpara(s))
out += E[33:37]
for s in ['Computadora y celular con acceso a internet', 'Aula virtual (Moodle)', 'Herramientas ofimáticas',
          'Chromium con DevTools (barra de dispositivos, zoom al 100 %)', 'GitHub: Issues, ramas y Pull Requests con revisión cruzada',
          'Inteligencia artificial como apoyo en la redacción y revisión, y TAC']:
    out.append(d.bullet(s, num=7))
out.append(E[41])
for k, v in {42: True, 43: False, 44: True, 45: False, 46: False, 47: True}.items():
    out.append(d.check(E[k], v))
out += E[48:51]
for s in ['1 · Pruebas técnicas en navegador: 320 × 720, 360 × 800, 768 × 1024 y 1366 × 768 px; scrollWidth <= innerWidth; capturas en evidencias/.',
          '2 · Observación con usuarios en aula: consigna neutral a un compañero de otro grupo; tiempo, errores, ayudas y dificultades.',
          '3 · Defensa cruzada QA/UX ante G3: pregunta técnica 1 (corte CSS y Tab), pregunta técnica 2 (disabled y foco) y objeción de diseño.',
          '4 · Cierre colaborativo en GitHub (4 Issues, 4 PRs revisados) y conclusiones finales.']:
    out.append(d.actividad(s))
out += E[58:60]

R = []
R.append(d.para('El presente informe documenta la fase 2 del APE 5 del **Grupo 5**. La pantalla trabajada es «Elige tu taller» (caso **Aula Abierta**): '
                'la versión A es un boceto de escritorio con 960 px fijos y la versión B es la interfaz adaptable construida en la fase 1. En esta fase se '
                'validó la versión B en cuatro resoluciones, se observó a compañeros de otro grupo usándola y se defendieron sus decisiones ante el grupo retador G3. '
                'El mismo patrón se aplica a la pantalla «Bitácora de observaciones» del proyecto del grupo, Usability Test Dashboard 2.0.'))
R.append(d.table([2300, 1600, 1700, 1300, 1244], [
    ['Integrante', 'Rol', 'Usuario GitHub', 'Rama · Issue', 'Revisado por'],
    ['Henry Daniel Lagua Flores (coordinador)', 'QA / Arquitecto', '@Hlagua', 'plan-clases · #1', 'Melany (#5)'],
    ['Melany Saleth Cevallos Goyes', 'Front-End', '@SalyC15', 'prototipo-html · #2', 'Alison (#6)'],
    ['Alison Marcela Cobos Taco', 'Back-End', '@Itsuna18', 'interfaz-responsive · #3', 'Carlos (#7)'],
    ['Carlos Giovanni Ramos Jácome', 'Tester', '@carlitosgiovanniramos', 'pruebas-informe · #4', 'Henry (#8)'],
]))
R.append(d.link_para('Repositorio de GitHub: ', REPO_URL))

# 1
R.append(d.sub('1. Diagnóstico y ficha de aplicación'))
R.append(d.para('El boceto A fija body { width: 960px } con columnas de 580 px y 360 px. En un teléfono de 360 px se pierde el panel «Mi reserva», que empieza en x = 600 px. '
                'La medición muestra **dos formas de fallo**. Sin emulación móvil, scrollWidth = 960 frente a innerWidth = 360, es decir, **+600 px de desborde**. '
                'Con la emulación de dispositivo móvil, Chromium aleja la página a una escala de **0,375** y el texto de 18 px se ve de **6,8 px**: cabe, pero es ilegible.'))
R.append(d.figure(F_A, 6.0, 'Figura 1. Boceto A a 320, 360 y 768 px: desborde de +640, +600 y +192 px; «Mi reserva» queda fuera de la pantalla.'))
R.append(d.table([2000, 3100, 3044], [
    ['Campo', 'Proyecto: Usability Test Dashboard', 'Caso de clase: Aula Abierta'],
    ['Actor', 'Moderador/a de la prueba', 'Estudiante'],
    ['Tarea principal', 'Registrar el desempeño de un participante', 'Reservar un lugar en un taller'],
    ['Dato clave', 'Éxito, tiempo (s) y número de errores', 'Horario, lugar y cupos (<dl>)'],
    ['Acción principal', '«Agregar al backlog»', '«Reservar un lugar»'],
    ['Resultado visible', 'Confirmación en <p role="status">', '«Reserva confirmada…» en role="status", cupos 12 → 11'],
    ['Mecanismo para corregir o cancelar', 'Editar la fila; errores < 0 → 0, tiempo < 1 → 1', 'Botón «Cancelar mi reserva» (cupos 11 → 12)'],
]))
R.append(d.para('**Regla de interacción:** impedir reservas duplicadas. **Criterio medible:** con la reserva confirmada, 5 intentos de activar «Reservar» dejan 11 cupos '
                '(0 duplicados en 5 de 5), y un doble Enter no cancela la reserva recién hecha.'))

# 2
R.append(d.sub('2. Versión B: HTML5 semántico, CSS Mobile-First e interacción'))
R.append(d.table([2600, 5544], [
    ['Archivo', 'Decisión implementada'],
    ['src/index.html', '<header>, <main>, <article> con <dl> (Horario, Lugar, Cupos) antes del <button>, <section> «Mi reserva» con <p role="status" aria-live="polite"> y botón para cancelar.'],
    ['src/estilos.css', 'Base de 1 columna (grid-template-columns: 1fr); @media (min-width: 48rem) → 3fr 2fr, sin order ni posicionamiento; botones de 44 px; :focus-visible ámbar de 3 px; prefers-reduced-motion.'],
    ['src/interaccion.js', 'Disponible → Confirmada → Cancelada. Al confirmar: disabled, texto «Ya tienes un lugar» y btnCancelar.focus(). Al cancelar: hidden y btnReservar.focus(). Margen de 600 ms contra el doble Enter (H-01).'],
    ['src/api.js', 'Valida cupos, rechaza la segunda confirmación y guarda el estado en sessionStorage.'],
]))

# 3
R.append(d.sub('3. Pruebas técnicas en navegador'))
R.append(d.para('Método: Chromium, DevTools en modo Responsive, zoom al 100 % y fuente predeterminada. En cada viewport se ejecutó '
                'document.documentElement.scrollWidth y se comparó con innerWidth. Las capturas tienen la medición impresa en la franja superior.', keep=True))
filas = [['Viewport', 'innerWidth', 'scrollWidth', 'Desborde', 'Columnas', 'Resultado']]
for w in (320, 360, 768, 1366):
    m = M['B-%d.png' % w]
    cols = '1' if len(m['columnas'].split()) == 1 else '2'
    filas.append([m['viewport'].replace('x', ' × '), str(m['innerWidth']), str(m['scrollWidth']), '%d px' % m['desborde'], cols, 'Aprobado' if m['desborde'] <= 0 else 'Falla'])
R.append(d.table([1500, 1300, 1300, 1200, 1200, 1644], filas))
R.append(d.para('Como comparación, el boceto A desborda **%+d**, **%+d** y **%+d px** a 320, 360 y 768 px. Con la versión B, a 767 px la cuadrícula sigue en 1 columna y a 768 px pasa a 2. '
                'Un título de 81 caracteres a 320 px tampoco desborda (scrollWidth = 320).' % (M['A-320.png']['desborde'], M['A-360.png']['desborde'], M['A-768.png']['desborde'])))
R.append(d.figure(F_MOV, 5.2, 'Figura 2. Versión B en móvil: 320 px, 360 px y 360 px con la reserva confirmada (desborde 0 px).'))
R.append(d.figure(F_ESC, 6.2, 'Figura 3. Versión B en 768 px (punto de corte, 2 columnas) y 1366 px con la reserva confirmada (desborde 0 px).'))
R.append(d.para('**Teclado, duplicados y foco (360 × 800, pulsaciones reales):**', keep=True))
R.append(d.table([700, 1700, 1800, 1500, 2444], [
    ['Paso', 'Tecla', 'Foco resultante', 'Estado · cupos', 'Observación'],
    ['1', 'Tab', '#btn-reservar', 'disponible · 12', 'Primer control de la tarea'],
    ['2', 'Enter', '#btn-cancelar', 'confirmada · 11', 'Reservar queda disabled'],
    ['3', 'click() forzado', '#btn-cancelar', 'confirmada · 11', '0 duplicados'],
    ['4', 'Shift + Tab', '#btn-cancelar', 'confirmada · 11', 'El botón deshabilitado se omite'],
    ['5', 'Espacio', '#btn-reservar', 'cancelada · 12', 'Cupo restituido y foco devuelto'],
]))
R.append(d.para('**Hallazgo H-01 y corrección:** en las pruebas con teclado, Tab → Enter Enter reservaba y cancelaba al instante, porque el segundo Enter caía sobre «Cancelar». '
                'Resultado antes: cancelada con 12 cupos. Se añadió un margen de 600 ms en el que «Cancelar» ignora activaciones. Resultado después: confirmada con 11 cupos. '
                'Un Enter un segundo más tarde sigue cancelando con normalidad (Nielsen H5, prevención de errores).'))

# 4
R.append(d.sub('4. Observación con usuarios en aula'))
R.append(d.para('**Consigna neutral:** «Necesitas asistir al taller del jueves. Averigua a qué hora y dónde se dicta, aparta un lugar y luego deshaz esa acción. '
                'Avísame cuando creas que terminaste.» No se mencionaron los nombres de los botones. Entre participantes se reinició el estado con una pestaña nueva.', keep=True))
obs_rows = [['Part.', 'Grupo', 'Versión', 'Viewport', 'Tiempo (s)', 'Errores', 'Ayudas', 'Éxito', 'Dificultades']]
for f in OBS:
    obs_rows.append([c if not vacio(c) else '—' for c in f[:9]])
R.append(d.table([600, 650, 700, 1050, 800, 750, 750, 650, 2194], obs_rows))
if RES:
    R.append(d.para('**Resumen:** %d participantes; tiempo medio en la versión B de %s s; %g errores de navegación y %g solicitudes de ayuda en total.' %
                    (RES['n'], ('%.1f' % RES['tB']).replace('.', ',') if RES['tB'] is not None else '—', RES['err'], RES['ayu'])))
else:
    R.append(d.para('**Resumen:** %s (los datos se registran durante la sesión en resultados/checklist.md).' % PEND))

# 5
R.append(d.sub('5. Defensa cruzada ante el grupo retador G3'))
R.append(d.table([1900, 2900, 1800, 1544], [['Punto', 'Planteamiento de G3', 'Respondió', 'Valoración']] + ACTA))
R.append(d.para('**Pregunta técnica 1 (corte en 48rem y Tab):** al cruzar 48rem solo cambia grid-template-columns de 1fr a 3fr 2fr. No se usa order ni posicionamiento, '
                'así que el orden visual coincide con el del DOM y con el de Tab (#btn-reservar → #btn-cancelar), medido a 360, 768 y 1366 px (WCAG 1.3.2 y 2.4.3).'))
R.append(d.para('**Pregunta técnica 2 (duplicados y foco):** disabled bloquea el botón (no recibe foco ni click), el controlador sale si el estado ya es confirmada '
                'y la API rechaza la segunda confirmación. El foco pasa a «Cancelar» al confirmar y vuelve a «Reservar» al cancelar; el margen de 600 ms evita la cancelación accidental (H-01).'))
R.append(d.para('**Objeción (ajuste frente a comprensión):** el 0 px de desborde es necesario pero no suficiente. El boceto A también «cabe» en emulación móvil, '
                'pero con texto de 6,8 px. Por eso la evidencia técnica (resultados/pruebas.md) se complementa con la observación de personas (resultados/checklist.md).'))

# 6
R.append(d.sub('6. Integración colaborativa en GitHub'))
R.append(d.table([1900, 2300, 1000, 1000, 1944], [
    ['Rama', 'Contenido', 'Issue', 'PR', 'Revisión cruzada'],
    ['plan-clases', 'README, planificación, plan de GitHub y diapositivas', '#1', '#5', 'Melany Cevallos'],
    ['prototipo-html', 'Boceto A de referencia y ficha de aplicación', '#2', '#6', 'Alison Cobos'],
    ['interfaz-responsive', 'interaccion.js, corrección H-01, CSS y respuestas de defensa', '#3', '#7', 'Carlos Ramos'],
    ['pruebas-informe', 'Mediciones, evidencias, observación, conclusiones e informe', '#4', '#8', 'Henry Lagua'],
]))
R.append(d.para('Cada rama modifica archivos distintos, así que los cuatro Pull Requests se fusionan en main sin conflictos y cada uno cierra su Issue con «Closes #N».'))
R.append(d.EMPTY)
out += R

out += E[110:113]
for k, v in {113: True, 114: True, 115: True, 116: False, 117: True, 118: False, 119: False, 120: False, 121: True}.items():
    out.append(d.check(E[k], v))
out += E[122:124]
dato_personas = ('con %d participantes de otros grupos, el tiempo medio en la versión B fue de %s s, con %g errores y %g ayudas.' %
                 (RES['n'], ('%.1f' % RES['tB']).replace('.', ',') if RES['tB'] is not None else '—', RES['err'], RES['ayu'])) if RES else \
                'la observación en aula se registra en resultados/checklist.md.'
for s in ['**Requisito y decisión.** Para que una estudiante reserve un taller desde su teléfono, cambiamos la cuadrícula fija de 960 px por un diseño Mobile-First en HTML5 semántico, con el estado en role="status" y un camino visible para deshacer.',
          '**Dato observado.** En el laboratorio medimos 0 px de desborde en 320, 360, 768 y 1366 px (el boceto A desborda +640, +600 y +192 px), la tarea completa con teclado y 0 duplicados; con personas, ' + dato_personas,
          '**Limitación y siguiente iteración.** La muestra es pequeña, no se probó con lectores de pantalla reales y los cupos se guardan solo en el navegador. La siguiente iteración: 5 participantes en teléfonos reales con NVDA y TalkBack, y control de cupos en un servidor.']:
    out.append(d.concl(s))
out += E[127:129]
for s in ['Medir siempre scrollWidth frente a innerWidth en el ancho más pequeño (320 px) antes de dar por terminado un diseño.',
          'Probar cada cambio de estado con teclado real, incluida la doble pulsación, y no solo con clics.',
          'Separar la evidencia técnica de la evidencia con personas y registrar solo datos observados.']:
    out.append(d.concl(s, 426))
out.append(d.EMPTY)
out.append(E[128].replace('Recomendaciones', 'Bibliografía'))
for s in ['[1] J. J. Cañas Delgado, T. Granollers i Saltiveri, y J. Lorés Vidal, *Diseño de sistemas interactivos centrados en el usuario*. Barcelona, España: Editorial UOC, 2012.',
          '[2] J. Ferrer Martínez, *Desarrollo de interfaces*. Madrid, España: RA-MA Editorial, 2015.',
          '[3] B. Shneiderman, *Diseño de interfaces de usuario*, 4.ª ed. Madrid, España: Pearson Educación, 2006.',
          '[4] R. S. Pressman, *Ingeniería del software: un enfoque práctico*, 7.ª ed. México D.F., México: McGraw-Hill, 2010.',
          '[5] H. Beati, *HTML5 y CSS3 para diseñadores*, 1.ª ed. Buenos Aires, Argentina: Alfaomega, 2015.',
          '[6] J. E. Córcoles Tendero y F. Montero Simarro, *Diseño de interfaces web*. Madrid, España: RA-MA Editorial, 2015.',
          '[7] J. Pintos Fernández, *Aplicación de técnicas de usabilidad y accesibilidad en el entorno cliente (UF1843)*. La Rioja, España: Tutor Formación, 2024.',
          '[8] J. Nielsen, "10 Usability Heuristics for User Interface Design," *Nielsen Norman Group*, 2024. [En línea]. Disponible: https://www.nngroup.com/articles/ten-usability-heuristics/',
          '[9] World Wide Web Consortium (W3C), "Web Content Accessibility Guidelines (WCAG) 2.2," *W3C Recommendation*, Oct. 2023. [En línea]. Disponible: https://www.w3.org/TR/WCAG22/']:
    out.append(d.ref(s))
out.append(d.EMPTY)
out.append(d.sub('Firmas de los integrantes'))
out.append(d.table([3600, 2200, 2344], [
    ['Integrante', 'Cédula', 'Firma'],
    ['Henry Daniel Lagua Flores', '', ''],
    ['Melany Saleth Cevallos Goyes', '', ''],
    ['Alison Marcela Cobos Taco', '', ''],
    ['Carlos Giovanni Ramos Jácome', '', ''],
]))
out.append(E[132])
dest = d.save(out, DOC + 'APE5_Fase2_Informe_Final.docx')
print('ok', dest, '| observación:', 'con datos' if RES else 'pendiente', '| acta:', sum(1 for a in ACTA if PEND not in a[1]), '/ 3')

# PDF con Word (opcional)
ps = ("$w=New-Object -ComObject Word.Application;$w.Visible=$false;try{$d=$w.Documents.Open('%s',$false,$true);"
      "$d.SaveAs([ref]'%s',[ref]17);$d.Close($false)}finally{$w.Quit()}") % (dest.replace('/', '\\'), dest.replace('/', '\\')[:-5] + '.pdf')
r = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True)
print('pdf', 'ok' if r.returncode == 0 else 'no generado: ' + r.stderr[:200])
