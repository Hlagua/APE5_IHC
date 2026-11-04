"""Informe APE 5 · Fase 1 (formato UTA, mismo que APE 4). Uso: python ape5_fase1_build.py"""
import sys, os
sys.path.insert(0, 'C:/Users/henry/Documents/UTA/IHC/APE4/_scripts')
from docx_lib import Doc, TNR, run
from PIL import Image, ImageDraw, ImageFont

W = 'C:/Users/henry/AppData/Local/Temp/ape5/fase1/'
os.makedirs(W, exist_ok=True)
B = 'C:/Users/henry/Documents/UTA/IHC/APE5/APE5_Fase1/'
CAP = B + '04_capturas/'
DOC = B + '06_documento/'
os.makedirs(DOC, exist_ok=True)


# ---------- composiciones de figuras ----------
def font(sz, bold=False):
    for f in (['C:/Windows/Fonts/segoeuib.ttf'] if bold else []) + ['C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/arial.ttf']:
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


def compose(items, dest, gap=40, pad=24, title_h=46):
    ims = [Image.open(CAP + f).convert('RGB') for f, _ in items]
    h = max(i.height for i in ims)
    w = sum(i.width for i in ims) + gap * (len(ims) - 1) + 2 * pad
    canvas = Image.new('RGB', (w, h + title_h + 2 * pad), 'white')
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, (_, label) in zip(ims, items):
        d.text((x, pad), label, fill='#1f2629', font=font(22, True))
        canvas.paste(im, (x, pad + title_h))
        d.rectangle([x - 1, pad + title_h - 1, x + im.width, pad + title_h + im.height], outline='#9aa3a7', width=2)
        x += im.width + gap
    canvas.save(dest)
    return dest


FIG_ANTES = compose([('boceto-A-360.png', 'Antes · boceto A a 360 px'), ('movil-360-disponible.png', 'Después · prototipo a 360 px')], W + 'antes_despues.png')
FIG_ESTADOS = compose([('movil-360-disponible.png', '1 · Disponible'), ('movil-360-confirmada.png', '2 · Confirmada'),
                       ('movil-360-cancelada.png', '3 · Cancelada')], W + 'estados.png')
FIG_ESCRITORIO = CAP + 'escritorio-1366-confirmada.png'
FIG_768 = CAP + 'escritorio-768-confirmada.png'

# ---------- documento ----------
d = Doc(W)
E = d.E
out = E[0:3]
out.append(d.replace_t(E[3], 'Refactorización con SOLID, Clean Architecture y Patrones Creacionales – Tipo B: Venta de motocicletas',
                       'APE 5. Fase 1 · Del boceto a la interfaz web adaptable (HTML5, CSS Mobile-First e interacción) · caso Aula Abierta y Usability Test Dashboard'))
out.append(E[4])
out.append(d.replace_t(E[5], 'Sexto - A', 'Quinto - A'))
out.append(E[6])
for n in ['Cobos Taco Alison Marcela', 'Cevallos Goyes Melany Saleth', 'Ramos Jacome Carlos Giovanni']:
    out.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="3540"/><w:rPr>%s</w:rPr></w:pPr>%s</w:p>' % (TNR, run(n)))
out.append(d.replace_t(E[7], 'Patrones de Software', 'Interacción Humano Computador'))
out.append(d.replace_t(E[8], 'Ing. Alex Maigua, Mg.', 'Ing. Mg. José Caiza'))
out += E[9:16]
out.append(d.listpara('Transformar un boceto estático de escritorio en una pantalla web adaptable, accesible e interactiva para reservar un taller, '
                      'conservando los principios HCI de jerarquía, visibilidad y control al pasar del dibujo al navegador.'))
out += E[17:19]
for s in ['Analizar el boceto A a 360 px e identificar dónde se materializan (o se pierden) la jerarquía, la visibilidad del estado y el control del usuario.',
          'Construir la pantalla con HTML5 semántico y una cuadrícula CSS que parte de una columna y pasa a dos desde 48rem, sin alterar el orden de lectura.',
          'Implementar los tres momentos de la reserva (disponible, confirmada y cancelada) con anuncio de estado, bloqueo de la segunda reserva y gestión del foco por teclado.']:
    out.append(d.bullet(s))
out += E[21:23]
out.append(d.replace_t(E[23], 'Presencial', 'Presencial – trabajo grupal'))
out += E[24:26]
out.append(E[26].replace('<w:t>4</w:t>', '<w:t>3 (180 min)</w:t>'))
out += E[27:30]
for s in ['**Acciones previas:** ingresar al aula virtual; revisar la presentación «Fase 1 · Del boceto al navegador» y el boceto A (prototipo-A.html).',
          '**Paso 1.** Abrir el boceto A a 360 px y localizar el estado de la reserva sin cambiar el zoom.',
          '**Paso 2.** Señalar en el boceto los tres principios HCI y marcar los límites de cada componente (tarjeta y resumen).',
          '**Paso 3.** Completar la ficha de aplicación (docs/proyecto.md) con una pantalla del proyecto del equipo.',
          '**Paso 4.** Construir la estructura HTML5, la cuadrícula CSS y la interacción de la reserva; probar con teclado y a 767/768 px.',
          '**Paso 5.** Realizar la revisión entre pares y subir a Moodle la carpeta APE5_Fase1, las capturas y este PDF.']:
    out.append(d.listpara(s))
out += E[33:37]
for s in ['Computadora y celular con acceso a internet', 'Aula virtual (Moodle)', 'Herramientas ofimáticas',
          'Navegador con herramientas de desarrollo (emulación de 360, 767 y 768 px)', 'Editor de código: HTML5, CSS y JavaScript sin dependencias',
          'Inteligencia artificial como apoyo en la redacción y revisión, y TAC']:
    out.append(d.bullet(s, num=7))
out.append(E[41])
for k, v in {42: True, 43: False, 44: True, 45: False, 46: False, 47: True}.items():
    out.append(d.check(E[k], v))
out += E[48:51]
for s in ['01 · Reto de transformación: abrir el boceto A a 360 px y localizar el estado sin cambiar el zoom.',
          '02 · Tres principios HCI: señalar en parejas dónde se materializan jerarquía, visibilidad y control.',
          '03 · Leer la pantalla: marcar los límites de cada componente y justificar el orden de lectura.',
          '04 · Ficha de aplicación: completar docs/proyecto.md con la ruta y una regla real de la aplicación.',
          '05 · Taller de HTML5: construir la estructura y comprobar que se entiende sin estilos.',
          '06 · Taller de CSS: una columna antes que dos; probar 767 y 768 px con la fuente predeterminada.',
          '07 · Taller de interacción: disponible → confirmada → cancelada; recorrer con Tab y Enter.',
          '08 · Revisión entre pares: otra pareja localiza el horario, reserva y cancela en móvil y escritorio.']:
    out.append(d.actividad(s))
out += E[58:60]

R = []
R.append(d.para('El presente informe documenta la Fase 1 de la práctica APE 5, cuyo reto es llevar el **boceto A** de la pantalla «Elige tu taller» '
                '(caso **Aula Abierta**) desde un dibujo estático de escritorio hasta una página que funcione en el navegador del teléfono y del computador. '
                'La pregunta guía fue: «una estudiante quiere reservar un taller desde su teléfono; ¿dónde busca el horario y cómo descubre que ya tiene un lugar?»'))

R.append(d.table([2400, 2200, 1800, 1744], [
    ['Integrante', 'Rol Oficial', 'Usuario GitHub', 'Responsabilidad en la fase'],
    ['Alison Marcela Cobos Taco', 'Desarrollador Back-End', '@Itsuna18', 'Lógica de estados de la reserva (reserva.js)'],
    ['Melany Saleth Cevallos Goyes', 'Desarrollador Front-End', '@SalyC15', 'Cuadrícula adaptable y estilos (estilos.css)'],
    ['Carlos Giovanni Ramos Jácome', 'Tester', '@carlitosgiovanniramos', 'Pruebas a 360/767/768 px, teclado y revisión entre pares'],
    ['Henry Daniel Lagua Flores', 'QA / Arquitecto', '@Hlagua', 'Estructura HTML5, ficha de aplicación e informe'],
]))

# 1. Diagnóstico
R.append(d.sub('1. Diagnóstico del boceto A (reto de transformación)'))
R.append(d.para('Al abrir el boceto A a 360 px sin cambiar el zoom, el resumen «Mi reserva» queda fuera de la pantalla: el estado no se puede localizar. '
                'La revisión identificó cinco problemas priorizados por Gravedad (G: 1-4) × Frecuencia (F: 1-3):', keep=True))
R.append(d.table([600, 3300, 2400, 800, 1044], [
    ['N.º', 'Problema identificado en el boceto A', 'Principio / Criterio', 'G × F', 'Prioridad'],
    ['D1', 'Ancho fijo body{width:960px} y columnas 580px/360px: a 360 px hay scroll horizontal y «Mi reserva» queda oculto.', 'Visibilidad · WCAG 1.4.10 (Reajuste)', '4 × 3', 'Alta'],
    ['D2', 'El botón «Reservar un lugar» está deshabilitado (disabled): la tarea no se puede completar.', 'Control · H3 Libertad del usuario', '4 × 3', 'Alta'],
    ['D3', 'El cambio de estado no se anuncia: no existe una región role="status".', 'Visibilidad · H1 · WCAG 4.1.3', '3 × 3', 'Alta'],
    ['D4', 'No hay forma de cancelar una reserva confirmada.', 'Control · H3 Deshacer', '3 × 2', 'Media'],
    ['D5', 'Horario y lugar están en un solo párrafo, sin estructura de datos (sin etiquetas «Horario» / «Lugar»).', 'Jerarquía · H6 Reconocer', '2 × 2', 'Media'],
]))
R.append(d.figure(FIG_ANTES, 4.6, 'Figura 1. Antes y después a 360 px: en el boceto A el resumen queda fuera; en el prototipo se lee debajo de la tarjeta.'))

# 2. Principios
R.append(d.sub('2. Tres principios HCI que deben sobrevivir al cambio'))
R.append(d.table([1700, 3100, 3344], [
    ['Principio', 'Qué exige', 'Dónde se materializa en el prototipo'],
    ['Jerarquía', 'Horario y lugar antes de confirmar.', 'Lista de definición <dl> con «Horario», «Lugar» y «Cupos» antes del botón «Reservar un lugar».'],
    ['Visibilidad', 'La interfaz dice si hay una reserva.', '<p role="status"> anuncia «Reserva confirmada…» o «Cancelaste tu reserva…»; el resumen cambia de color según data-estado.'],
    ['Control', 'La persona puede deshacer su acción.', 'Botón «Cancelar mi reserva»: libera el cupo (11 → 12) y vuelve a habilitar la reserva.'],
]))

# 3. Componentes
R.append(d.sub('3. Del dibujo a los componentes'))
R.append(d.para('La pantalla se divide en dos componentes. La **tarjeta** (<article>) reúne el taller y su acción; el **resumen** (<section> «Mi reserva») reúne el estado y la cancelación. '
                'El orden de lectura es tarjeta → resumen porque primero se decide (datos + acción) y después se verifica el resultado (estado + deshacer). '
                'En móvil se leen uno debajo del otro; en escritorio uno al lado del otro, pero el orden del HTML no cambia.'))

# 4. Ficha
R.append(d.sub('4. Ficha de aplicación'))
R.append(d.para('Se aplicó la ruta «actor → tarea → dato decisivo → acción principal → estado final» al caso de clase y a una pantalla real del proyecto del equipo '
                '(**Usability Test Dashboard 2.0**, pantalla «Bitácora de observaciones»):', keep=True))
R.append(d.table([1700, 1500, 1600, 1500, 1844], [
    ['Actor', 'Tarea', 'Dato decisivo', 'Acción principal', 'Estado final'],
    ['Moderador/a de la prueba', 'Registrar cómo le fue a un participante en una tarea', 'Éxito, tiempo (s) y número de errores', 'Agregar al backlog', 'Hallazgo agregado al backlog y confirmado en role="status"'],
    ['Estudiante (caso de clase)', 'Reservar un taller', 'Horario y lugar', 'Reservar un lugar', 'Reserva confirmada y cupo descontado'],
]))
R.append(d.para('**Requisito (RF-OBS-01):** el moderador debe registrar por cada participante y tarea el éxito, el tiempo y los errores observados, y enviar el hallazgo '
                'al backlog sabiendo si el envío se completó o falló.'))
R.append(d.para('**Regla de negocio:** las métricas de una observación no pueden ser inválidas. Si se escribe un número de errores negativo, el sistema lo corrige a 0, '
                'y si se escribe un tiempo menor que 1 s, lo corrige a 1 (handleObsChange en ObservationRecordPage.tsx). «Errores» es obligatorio.'))
R.append(d.para('**Criterio de aceptación medible:** al escribir −3 en «Errores» el valor queda en 0, y al escribir 0 en «Tiempo (s)» queda en 1, en 5 de 5 intentos (100 %). '
                'El backlog contiene 0 observaciones con errores < 0 o tiempo < 1. En el caso de clase, con una reserva confirmada, pulsar Enter sobre «Reservar» '
                'genera 0 reservas duplicadas y el cupo baja exactamente en 1.'))

# 5. HTML
R.append(d.sub('5. Taller de HTML5: primero la estructura'))
R.append(d.table([2400, 5744], [
    ['Elemento', 'Función en la pantalla'],
    ['<header>', 'Identifica el sitio (Aula Abierta) fuera de la tarea principal.'],
    ['<main>', 'Contiene la tarea principal: elegir y reservar el taller.'],
    ['<article>', 'Tarjeta autónoma del taller: reúne el dato decisivo y la acción principal.'],
    ['<dl>', 'Pares término-valor: Horario, Lugar y Cupos, leídos antes del botón.'],
    ['<section>', 'Resumen «Mi reserva»: agrupa el estado y la cancelación.'],
    ['<button>', 'Ejecuta la reserva y la cancelación; es alcanzable con Tab y se activa con Enter o Espacio.'],
    ['<p role="status">', 'Comunica el cambio de estado a lectores de pantalla sin mover el foco.'],
]))
R.append(d.para('**Prueba sin estilos:** al desactivar estilos.css la página se lee como un documento lineal (título, taller, horario, lugar, botón, «Mi reserva», estado) '
                'y sigue siendo claro qué hacer.'))

# 6. CSS
R.append(d.sub('6. Taller de CSS: una columna antes que dos'))
R.append(d.para('La cuadrícula empieza con grid-template-columns: 1fr. Con @media (min-width: 48rem), es decir 768 px con la fuente predeterminada de 16 px, '
                'pasa a dos columnas (3fr 2fr). El ancho de la página es fluido (max-width: 60rem) y los botones miden al menos 44 px de alto.', keep=True))
R.append(d.table([1600, 2600, 3944], [
    ['Ancho', 'Columnas medidas', 'Observación'],
    ['360 px', '1 (328 px)', 'Sin scroll horizontal (scrollWidth = 360). Resumen visible debajo de la tarjeta.'],
    ['767 px', '1 (735 px)', 'Todavía una columna: el cambio no ocurre antes de 48rem.'],
    ['768 px', '2 (432 px | 288 px)', 'La tarjeta y el resumen se separan; el orden del HTML se conserva.'],
]))
R.append(d.figure(FIG_768, 4.2, 'Figura 2. Punto de corte a 768 px (48rem): la tarjeta y el resumen pasan a dos columnas.'))
R.append(d.figure(FIG_ESCRITORIO, 5.8, 'Figura 3. Vista de escritorio a 1366 px con dos columnas y la reserva confirmada.'))

# 7. Interacción
R.append(d.sub('7. Taller de interacción: una reserva tiene tres momentos'))
R.append(d.table([1500, 3000, 1800, 1844], [
    ['Estado', 'Mensaje en role="status"', 'Botones', 'Foco después de la acción'],
    ['Disponible', '«Aún no tienes una reserva.» · 12 cupos', 'Reservar habilitado · Cancelar oculto', '—'],
    ['Confirmada', '«Reserva confirmada: Interfaces web accesibles · jueves de 14:00 a 16:00 · Laboratorio 2.» · 11 cupos', 'Reservar deshabilitado («Ya tienes un lugar») · Cancelar visible', '«Cancelar mi reserva»'],
    ['Cancelada', '«Cancelaste tu reserva. El lugar vuelve a estar disponible.» · 12 cupos', 'Reservar habilitado · Cancelar oculto', '«Reservar un lugar»'],
]))
R.append(d.para('Al confirmar se bloquea una segunda reserva. Como el botón que tenía el foco queda deshabilitado u oculto, el foco se mueve de forma explícita a la siguiente acción lógica, '
                'de modo que quien usa Tab y Enter no pierde su posición en la página.'))
R.append(d.figure(FIG_ESTADOS, 6.0, 'Figura 4. Los tres momentos de la reserva a 360 px: disponible, confirmada y cancelada.'))

# 8. Revisión entre pares
R.append(d.sub('8. Revisión entre pares y entrega de la fase 1'))
R.append(d.para('La otra pareja intentó localizar el horario, reservar y cancelar en móvil y escritorio. Resultados registrados:', keep=True))
R.append(d.table([2000, 1300, 1300, 3544], [
    ['Tarea', 'Móvil 360 px', 'Escritorio 1366 px', 'Observación de la pareja revisora'],
    ['Localizar el horario', '[completar]', '[completar]', '[completar en clase]'],
    ['Reservar', '[completar]', '[completar]', '[completar en clase]'],
    ['Cancelar', '[completar]', '[completar]', '[completar en clase]'],
]))
R.append(d.table([2200, 5944], [
    ['Entregable', 'Contenido'],
    ['Una ruta', 'Estudiante → reservar → horario → confirmar → lugar reservado (y su equivalente en el proyecto: moderador → registrar observación → agregar al backlog).'],
    ['Una decisión HCI', 'En móvil la tarjeta y el resumen van en una sola columna, en el orden del HTML; así el estado de la reserva queda siempre debajo de la acción, sin scroll horizontal ni zoom.'],
    ['Dos capturas', 'Figura 1 (móvil, 360 px) y Figuras 2 y 3 (escritorio, 768 y 1366 px).'],
    ['Hipótesis para la fase 2', 'Al confirmar o cancelar con teclado, quien usa lector de pantalla (NVDA/TalkBack) escucha el mensaje de role="status" y entiende que el foco pasó al botón siguiente. Se valida si al menos 4 de 5 participantes repiten el estado de su reserva sin buscarlo visualmente.'],
]))

R.append(d.EMPTY)
out += R

out += E[110:113]
for k, v in {113: True, 114: True, 115: True, 116: False, 117: True, 118: True, 119: False, 120: False, 121: True}.items():
    out.append(d.check(E[k], v))
out += E[122:124]
for s in ['**Una interfaz adaptable empieza por el contenido, no por el ancho.** El boceto A fallaba en móvil por fijar 960 px; partir de una columna y ampliar desde 48rem permitió que la misma estructura sirva en el teléfono y en el escritorio sin reordenar el HTML.',
          '**La visibilidad del estado se diseña en la estructura.** Un <p role="status"> y un resumen que cambia de color hacen que la persona sepa si tiene un lugar sin buscarlo, y que un lector de pantalla también lo anuncie.',
          '**El control incluye deshacer y no perder el foco.** Cancelar la reserva devuelve el cupo, y mover el foco a la siguiente acción evita que quien navega con teclado quede en un botón deshabilitado u oculto.']:
    out.append(d.concl(s))
out += E[127:129]
for s in ['Revisar cada pantalla a 360 px con la fuente predeterminada antes de agregar estilos decorativos.',
          'Probar siempre con teclado (Tab, Enter, Espacio) después de cada cambio de estado y verificar dónde queda el foco.',
          'Validar el anuncio de role="status" con un lector de pantalla real en la fase 2 y registrar el resultado.']:
    out.append(d.concl(s, 426))
out.append(d.EMPTY)
out.append(E[128].replace('Recomendaciones', 'Bibliografía'))
for s in ['[1] J. J. Cañas Delgado, T. Granollers i Saltiveri, y J. Lorés Vidal, *Diseño de sistemas interactivos centrados en el usuario*. Barcelona, España: Editorial UOC, 2012.',
          '[2] J. E. Córcoles Tendero y F. Montero Simarro, *Diseño de interfaces web*. Madrid, España: RA-MA Editorial, 2015.',
          '[3] J. Ferrer Martínez, *Desarrollo de interfaces*. Madrid, España: RA-MA Editorial, 2015.',
          '[4] J. Nielsen, "10 Usability Heuristics for User Interface Design," *Nielsen Norman Group*, 2024. [En línea]. Disponible: https://www.nngroup.com/articles/ten-usability-heuristics/',
          '[5] J. Pintos Fernández, *Aplicación de técnicas de usabilidad y accesibilidad en el entorno cliente (UF1843)*. Madrid, España: Tutor Formación, 2024.',
          '[6] B. Shneiderman y C. Plaisant, *Diseño de interfaces de usuario: estrategias para una interacción persona-computadora efectiva*, 4.ª ed. Madrid, España: Pearson Educación, 2006.',
          '[7] World Wide Web Consortium (W3C), "Web Content Accessibility Guidelines (WCAG) 2.2," *W3C Recommendation*, Oct. 2023. [En línea]. Disponible: https://www.w3.org/TR/WCAG22/',
          '[8] World Wide Web Consortium (W3C), "Accessible Rich Internet Applications (WAI-ARIA) 1.2: status role," *W3C Recommendation*, Jun. 2023. [En línea]. Disponible: https://www.w3.org/TR/wai-aria-1.2/#status']:
    out.append(d.ref(s))
out.append(E[132])
dest = d.save(out, DOC + 'APE5_Fase1_AulaAbierta.docx')
print('ok', dest)
