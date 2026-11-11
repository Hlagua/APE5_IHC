"""Informe final APE 5 · formato UTA · Grupo 5 · caso CaféU «Mi pedido».

Uso: python _scripts/ape5_fase2_build.py
(antes, con el servidor encendido: python _scripts/ape5_fase2_evidencias.py, que genera las mediciones)
Lee resultados/checklist.md (tabla de observación) y docs/preguntas.md (acta): basta con completarlos
después de la clase y volver a ejecutarlo. Genera 06_documento/APE5_Fase2_Informe_Final.docx (y .pdf con Word).
"""
import os, re, sys, json, subprocess
sys.path.insert(0, 'C:/Users/henry/Documents/UTA/IHC/APE4/_scripts')
from docx_lib import Doc, TNR, run
from PIL import Image, ImageDraw

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
EV = REPO + 'evidencias/'
DOC = REPO + '06_documento/'
W = os.environ.get('TEMP', '/tmp').replace('\\', '/') + '/ape5/fase2/'
os.makedirs(W, exist_ok=True)
os.makedirs(DOC, exist_ok=True)
REPO_URL = 'https://github.com/Hlagua/APE5_IHC'
PEND = '[completar en clase]'


# ---------- datos de clase ----------
def leer(p):
    return open(REPO + p, encoding='utf8').read()


def vacio(s):
    s = (s or '').strip()
    return s == '' or set(s) <= set('_ ')


def observaciones():
    """Filas de la tabla: Part, Grupo, Versión, Viewport, Tiempo, Errores, Ayudas, Dice n.º y pago, Éxito, Dificultades."""
    sec = leer('resultados/checklist.md').split('## 4. Tabla de observación', 1)[1].split('## 5.', 1)[0]
    return [[x.strip() for x in l.strip().strip('|').split('|')] for l in sec.splitlines() if re.match(r'^\|\s*P-\d+', l)]


def resumen_obs(filas):
    datos = [f for f in filas if not vacio(f[4])]
    if not datos:
        return None
    num = lambda s: float(s.replace(',', '.')) if not vacio(s) else 0.0
    B = [f for f in datos if f[2].upper() == 'B']
    A = [f for f in datos if f[2].upper() == 'A']
    r = {'n': len(datos), 'nB': len(B), 'nA': len(A)}
    if B:
        r.update(tB=sum(num(f[4]) for f in B) / len(B), errB=sum(num(f[5]) for f in B), ayuB=sum(num(f[6]) for f in B),
                 diceB=sum(1 for f in B if f[7].strip().lower().startswith('s')))
    if A:
        r.update(tA=sum(num(f[4]) for f in A) / len(A), errA=sum(num(f[5]) for f in A), ayuA=sum(num(f[6]) for f in A))
    return r


def coma(x):
    return ('%.1f' % x).replace('.', ',')


def pl(n, uno, varios):
    return '%g %s' % (n, uno if n == 1 else varios)


def texto_resumen(r):
    if not r or not r.get('nB'):
        return None
    s = ('en la versión B, %s: tiempo medio de %s s, %s y %s; %d de %d dijeron su número de pedido y si habían pagado sin buscarlo' %
         (pl(r['nB'], 'participante', 'participantes'), coma(r['tB']), pl(r['errB'], 'error de navegación', 'errores de navegación'),
          pl(r['ayuB'], 'solicitud de ayuda', 'solicitudes de ayuda'), r['diceB'], r['nB']))
    if r.get('nA'):
        s += '. Con el boceto A (%s): %s s, %s y %s' % (
            pl(r['nA'], 'participante', 'participantes'), coma(r['tA']), pl(r['errA'], 'error', 'errores'), pl(r['ayuA'], 'ayuda', 'ayudas'))
    return s + '.'


def acta():
    partes = re.split(r'^## ', leer('docs/preguntas.md'), flags=re.M)
    out = []
    for titulo in ('Pregunta técnica 1', 'Pregunta técnica 2', 'Objeción de diseño'):
        reg = next(x for x in partes if x.startswith(titulo)).split('**Registro en la sesión:**', 1)[1]

        def campo(et):
            m = re.search(re.escape(et) + r'\s*(.*?)(?:·|\n)', reg)
            v = m.group(1).strip() if m else ''
            return PEND if vacio(v) else v
        val = re.findall(r'[☒✔]\s*([^☐☒✔\n]+)', reg.split('Valoración', 1)[1])
        out.append([titulo, campo('Pregunta textual de G3:') if 'Pregunta' in titulo else campo('Objeción textual de G3:'),
                    campo('Respuesta dada por (integrante):'), val[0].strip() if val else PEND])
    return out


OBS = observaciones()
RES = resumen_obs(OBS)
RESUMEN = texto_resumen(RES)
ACTA = acta()
M = {m['archivo'].split('/')[-1]: m for m in json.load(open(REPO + '_scripts/_tmp/mediciones.json', encoding='utf8'))}


# ---------- figuras compuestas ----------
def fila(archivos, dest, alto=760, gap=28, pad=20):
    ims = []
    for a in archivos:
        im = Image.open(EV + a).convert('RGB')
        ims.append(im.resize((int(im.width * alto / im.height), alto)))
    lienzo = Image.new('RGB', (sum(i.width for i in ims) + gap * (len(ims) - 1) + 2 * pad, alto + 2 * pad), 'white')
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
                       'APE 5. Diseño de interfaces web adaptables · caso CaféU «Mi pedido»: validación técnica, pruebas con usuarios y defensa · Grupo 5'))
out.append(E[4])
out.append(d.replace_t(E[5], 'Sexto - A', 'Quinto - A'))
out.append(E[6])
for n in ['Cevallos Goyes Melany Saleth', 'Cobos Taco Alison Marcela', 'Ramos Jacome Carlos Giovanni']:
    out.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="3540"/><w:rPr>%s</w:rPr></w:pPr>%s</w:p>' % (TNR, run(n)))
out.append(d.replace_t(E[7], 'Patrones de Software', 'Interacción Humano Computador'))
out.append(d.replace_t(E[8], 'Ing. Alex Maigua, Mg.', 'Ing. Mg. José Caiza'))
out += E[9:16]
out.append(d.listpara('Desarrollar un diseño de interfaces para una aplicación web: llevar la pantalla «Mi pedido» de CaféU (APE 4) a una interfaz web adaptable, '
                      'validarla técnicamente y con personas, y defender sus decisiones de diseño con evidencia.'))
out += E[17:19]
for s in ['Validar la interfaz en 320, 360, 768 y 1366 px midiendo document.documentElement.scrollWidth frente a innerWidth, con 0 px de desborde como criterio.',
          'Observar a compañeros de otros grupos con una consigna neutral, registrando tiempo, errores de navegación, solicitudes de ayuda y si dicen su número de pedido y si pagaron.',
          'Defender ante el grupo retador G3 el punto de corte, el cobro único y la gestión del foco, e integrar el trabajo en GitHub con 4 Pull Requests revisados.']:
    out.append(d.bullet(s))
out += E[21:23]
out.append(d.replace_t(E[23], 'Presencial', 'Presencial – trabajo grupal'))
out += E[24:30]
for s in ['**Acciones previas:** ingresar al aula virtual; elaborar el trabajo siguiendo las definiciones, conceptos y procesos aprendidos en clase; desarrollar un diseño con los requerimientos establecidos.',
          '**Paso 1.** Revisar el material entregado por el docente sobre la aplicación de HTML5 y CSS.',
          '**Paso 2.** Generar una base de conocimiento debidamente documentada sobre el desarrollo web (repositorio y carpeta docs/).',
          '**Paso 3.** Determinar los requerimientos mínimos para el diseño de una interfaz web (ficha de aplicación de CaféU).',
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
          '2 · Observación con usuarios en aula: consigna neutral a compañeros de otros grupos; tiempo, errores, ayudas y dificultades.',
          '3 · Defensa cruzada QA/UX ante G3: pregunta técnica 1 (corte CSS y Tab), pregunta técnica 2 (cobro único y foco) y objeción de diseño.',
          '4 · Cierre colaborativo en GitHub (4 Issues, 4 PRs revisados) y conclusiones finales.']:
    out.append(d.actividad(s))
out += E[58:60]

R = []
R.append(d.para('El presente informe documenta el APE 5 del **Grupo 5** sobre **CaféU**, la aplicación de pedidos de la cafetería universitaria que el grupo diseñó y probó '
                'en el APE 4. La pantalla trabajada es **«Mi pedido → Confirmar y pagar»**: la versión A es un boceto de escritorio con 960 px fijos y la versión B es la '
                'interfaz web adaptable. Se validó la versión B en cuatro resoluciones, se preparó la observación con compañeros y la defensa ante el grupo retador G3.'))
R.append(d.table([2300, 1600, 1700, 1300, 1244], [
    ['Integrante', 'Rol', 'Usuario GitHub', 'Rama', 'Revisado por'],
    ['Henry Daniel Lagua Flores (coordinador)', 'QA / Arquitecto', '@Hlagua', 'plan-clases', 'Melany'],
    ['Melany Saleth Cevallos Goyes', 'Front-End', '@SalyC15', 'prototipo-html', 'Alison'],
    ['Alison Marcela Cobos Taco', 'Back-End', '@Itsuna18', 'interfaz-responsive', 'Carlos'],
    ['Carlos Giovanni Ramos Jácome', 'Tester', '@carlitosgiovanniramos', 'pruebas-informe', 'Henry'],
]))
R.append(d.link_para('Repositorio de GitHub: ', REPO_URL))

# 1
R.append(d.sub('1. Diagnóstico y ficha de aplicación'))
R.append(d.para('En el APE 4, CaféU se probó como prototipo móvil y el riesgo principal para el usuario fue el **temor a pagar dos veces** (D1). El boceto A de «Mi pedido» '
                'fija body { width: 960px } con columnas de 580 px y 360 px: en un teléfono de 360 px, el panel «Estado del pedido» empieza en x = 600 px, así que el estudiante '
                'paga y no ve si se cobró. Sin emulación móvil, scrollWidth = 960 frente a innerWidth = 360 (**+600 px**). Con emulación de dispositivo móvil, Chromium '
                'aleja la página a una escala de **0,375** y el texto de 18 px se ve de **6,75 px**: cabe, pero es ilegible.'))
R.append(d.figure(F_A, 6.0, 'Figura 1. Boceto A de «Mi pedido» a 320, 360 y 768 px: desborde de +640, +600 y +192 px; el estado del pedido queda fuera de la pantalla.'))
R.append(d.table([2400, 5744], [
    ['Campo', 'CaféU · «Mi pedido»'],
    ['Actor', 'Estudiante universitario con poco tiempo entre clases que pide desde el celular'],
    ['Tarea principal', 'Confirmar y pagar su pedido para retirarlo sin hacer fila'],
    ['Dato clave', 'Productos, total $4.25, retiro en el Edificio central (10 min) y tarjeta universitaria con su saldo (<dl>)'],
    ['Acción principal', '«Confirmar y pagar · $4.25»'],
    ['Resultado visible', '«Pedido #A24 confirmado y pagado ($4.25)…» en role="status", panel verde, saldo $10.00 → $5.75 y botón «Pedido #A24 pagado» deshabilitado'],
    ['Mecanismo para corregir o cancelar', 'Antes de pagar, «Editar» (W5 del APE 4); después, «Cancelar pedido», que devuelve los $4.25'],
]))
R.append(d.para('**Requisito (RF-PED-01):** confirmar y pagar una sola vez, ver de inmediato el número de pedido y cuándo retirarlo, y cancelar con devolución. '
                '**Regla:** un pedido se cobra una sola vez. **Criterio medible:** con el pedido pagado, 5 intentos de pagar dejan el saldo en $5.75 (0 cobros duplicados en 5 de 5), '
                'y un doble Enter no cancela el pedido recién pagado.'))

# 2
R.append(d.sub('2. Versión B: HTML5 semántico, CSS Mobile-First e interacción'))
R.append(d.table([2400, 5744], [
    ['Archivo', 'Decisión implementada'],
    ['src/index.html', '<header>, <main>, <article> con los productos y un <dl> (Total, Retiro, Pago) antes del <button>, y <section> «Estado de tu pedido» con <p role="status" aria-live="polite"> y «Cancelar pedido».'],
    ['src/estilos.css', '1 columna base; @media (min-width: 48rem) → 3fr 2fr sin order ni posicionamiento; paleta CaféU del APE 4; botones de 44 px; :focus-visible de 3 px; prefers-reduced-motion.'],
    ['src/interaccion.js', 'Pendiente → Confirmado → Cancelado. Al pagar: disabled, «Pedido #A24 pagado» y btnCancelar.focus(). Al cancelar: hidden y btnConfirmar.focus(). Margen de 600 ms contra el doble Enter (H-01).'],
    ['src/api.js', 'PedidoAPI: rechaza el segundo cobro, devuelve el total al cancelar y guarda el estado en sessionStorage.'],
]))

# 3
R.append(d.sub('3. Pruebas técnicas en navegador'))
R.append(d.para('Método: Chromium, DevTools en modo Responsive, zoom al 100 % y fuente predeterminada. En cada viewport se comparó '
                'document.documentElement.scrollWidth con innerWidth. Las capturas tienen la medición impresa en la franja superior.', keep=True))
filas = [['Viewport', 'innerWidth', 'scrollWidth', 'Desborde', 'Columnas', 'Resultado']]
for w in (320, 360, 768, 1366):
    m = M['B-%d.png' % w]
    filas.append([m['viewport'].replace('x', ' × '), str(m['innerWidth']), str(m['scrollWidth']), '%d px' % m['desborde'],
                  '1' if len(m['columnas'].split()) == 1 else '2', 'Aprobado' if m['desborde'] <= 0 else 'Falla'])
R.append(d.table([1500, 1300, 1300, 1200, 1200, 1644], filas))
R.append(d.para('El boceto A desborda **%+d**, **%+d** y **%+d px** a 320, 360 y 768 px. En la versión B, a 767 px la cuadrícula sigue en 1 columna y a 768 px pasa a 2; '
                'un producto de 88 caracteres a 320 px tampoco desborda (scrollWidth = 320).' % (M['A-320.png']['desborde'], M['A-360.png']['desborde'], M['A-768.png']['desborde'])))
R.append(d.figure(F_MOV, 5.2, 'Figura 2. «Mi pedido» en móvil: 320 px, 360 px y 360 px con el pedido #A24 pagado (desborde 0 px).'))
R.append(d.figure(F_ESC, 6.2, 'Figura 3. «Mi pedido» a 768 px (punto de corte, 2 columnas) y a 1366 px con el pedido pagado (desborde 0 px).'))
R.append(d.para('**Teclado, cobro único y foco (360 × 800, pulsaciones reales):**', keep=True))
R.append(d.table([700, 1800, 1700, 1600, 2344], [
    ['Paso', 'Tecla', 'Foco resultante', 'Estado · saldo', 'Observación'],
    ['1', 'Tab', '#btn-confirmar', 'pendiente · $10.00', 'Primer control de la tarea'],
    ['2', 'Enter Enter (doble)', '#btn-cancelar', 'confirmado · $5.75', 'Pedido #A24; un solo cobro'],
    ['3', 'Shift + Tab', '#btn-cancelar', 'confirmado · $5.75', 'El botón deshabilitado se omite'],
    ['4', 'Espacio (1 s después)', '#btn-confirmar', 'cancelado · $10.00', 'Se devuelven $4.25'],
    ['5', 'Enter', '#btn-cancelar', 'confirmado · $5.75', 'Nuevo pedido #A25'],
]))
R.append(d.para('**Hallazgo H-01:** sin margen, Tab → Enter → Enter pagaba y cancelaba al instante, porque el segundo Enter caía sobre «Cancelar pedido» '
                '(resultado: cancelado, saldo $10.00). Con un margen de 600 ms en el que «Cancelar pedido» ignora activaciones, el resultado es confirmado con $5.75, '
                'y cancelar un segundo después funciona normalmente (Nielsen H5). La suite automática tests/test_runner.html da **10 de 10**.'))

# 4
R.append(d.sub('4. Observación con usuarios en aula'))
R.append(d.para('**Consigna neutral:** «Ya elegiste tu café y tu sánduche en la app de la cafetería. Termina tu compra para poder retirarla, y después dime tu número de '
                'pedido y si ya pagaste. Luego imagina que te equivocaste: deshaz la compra.» No se mencionan los nombres de los botones y el estado se reinicia entre participantes.', keep=True))
obs_rows = [['Part.', 'Gr.', 'Vers.', 'Viewport', 'Tiempo (s)', 'Err.', 'Ayud.', 'N.º y pago', 'Éxito', 'Dificultades']]
for f in OBS:
    obs_rows.append([c if not vacio(c) else '—' for c in (f + [''] * 10)[:10]])
R.append(d.table([600, 500, 550, 1000, 750, 550, 600, 850, 600, 2144], obs_rows))
R.append(d.para('**Resumen:** ' + (RESUMEN if RESUMEN else PEND + ' (los datos se registran durante la sesión en resultados/checklist.md).')))

# 5
R.append(d.sub('5. Defensa cruzada ante el grupo retador G3'))
R.append(d.table([1900, 2900, 1800, 1544], [['Punto', 'Planteamiento de G3', 'Respondió', 'Valoración']] + ACTA))
R.append(d.para('**Pregunta técnica 1 (corte en 48rem y Tab):** al cruzar 48rem solo cambia grid-template-columns de 1fr a 3fr 2fr. Sin order ni posicionamiento, el orden visual '
                'coincide con el del DOM y con el de Tab (#btn-confirmar → #btn-cancelar) en 320, 360, 768 y 1366 px (WCAG 1.3.2 y 2.4.3).'))
R.append(d.para('**Pregunta técnica 2 (pago duplicado y foco):** disabled bloquea el botón, el controlador sale si el pedido ya está confirmado y PedidoAPI rechaza el segundo cobro. '
                'El foco pasa a «Cancelar pedido» al pagar y vuelve a «Confirmar y pagar» al cancelar; el margen de 600 ms evita la cancelación accidental (H-01).'))
R.append(d.para('**Objeción (ajuste frente a comprensión):** el 0 px de desborde es necesario pero no suficiente. El boceto A también «cabe» en emulación móvil, '
                'pero con texto de 6,75 px. Por eso la evidencia técnica (resultados/pruebas.md) se complementa con la observación de personas (resultados/checklist.md).'))

# 6
R.append(d.sub('6. Integración colaborativa en GitHub'))
R.append(d.table([1900, 3300, 1300, 1644], [
    ['Rama', 'Contenido', 'Integrante', 'Revisión cruzada'],
    ['plan-clases', 'README, planificación, plan de GitHub y diapositivas', 'Henry Lagua', 'Melany Cevallos'],
    ['prototipo-html', 'Boceto A de «Mi pedido» y ficha de aplicación', 'Melany Cevallos', 'Alison Cobos'],
    ['interfaz-responsive', 'HTML, CSS, API, interacción con cobro único, suite y respuestas de defensa', 'Alison Cobos', 'Carlos Ramos'],
    ['pruebas-informe', 'Mediciones, evidencias, observación, conclusiones e informe', 'Carlos Ramos', 'Henry Lagua'],
]))
R.append(d.para('Cada rama modifica archivos distintos, así que los cuatro Pull Requests se fusionan sin conflictos; cada uno cierra su Issue con «Closes #N» y se fusiona '
                'después de la aprobación del revisor desde su propia cuenta (docs/github.md).'))
R.append(d.EMPTY)
out += R

out += E[110:113]
for k, v in {113: True, 114: True, 115: True, 116: False, 117: True, 118: False, 119: False, 120: False, 121: True}.items():
    out.append(d.check(E[k], v))
out += E[122:124]
for s in ['**Requisito y decisión.** Para que el estudiante pague su pedido de CaféU desde el teléfono y sepa si ya pagó, llevamos «Mi pedido» del prototipo móvil del APE 4 a una '
          'interfaz Mobile-First en HTML5 semántico, con el estado en role="status", un cobro único y un camino visible para cancelar con devolución.',
          '**Dato observado.** En el laboratorio medimos 0 px de desborde en 320, 360, 768 y 1366 px (el boceto A desborda +640, +600 y +192 px), la tarea completa con teclado, '
          '0 cobros duplicados y la suite en 10 de 10. Con personas: ' + (RESUMEN if RESUMEN else 'la observación en aula se registra en resultados/checklist.md.'),
          '**Limitación y siguiente iteración.** La muestra es pequeña, no se probó con lectores de pantalla reales y el pago es simulado en el navegador. Siguiente iteración: '
          '5 participantes en teléfonos reales con NVDA y TalkBack, cobro único en el servidor y el estado de pago rechazado del APE 4 con el mismo patrón adaptable.']:
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
print('ok', dest, '| observación:', 'con datos' if RESUMEN else 'pendiente', '| acta:', sum(1 for a in ACTA if PEND not in a[1]), '/ 3')

ps = ("$w=New-Object -ComObject Word.Application;$w.Visible=$false;try{$d=$w.Documents.Open('%s',$false,$true);"
      "$d.SaveAs([ref]'%s',[ref]17);$d.Close($false)}finally{$w.Quit()}") % (dest.replace('/', '\\'), dest.replace('/', '\\')[:-5] + '.pdf')
r = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True)
print('pdf', 'ok' if r.returncode == 0 else 'no generado: ' + r.stderr[:200])
