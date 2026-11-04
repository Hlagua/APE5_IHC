"""Documento corto de entrega APE 5 · Fase 1 (Moodle «Archivos enviados»). Uso: python ape5_fase1_entrega.py [URL_REPO]"""
import sys, os
sys.path.insert(0, 'C:/Users/henry/Documents/UTA/IHC/APE4/_scripts')
from docx_lib import Doc, TNR, run

W = 'C:/Users/henry/AppData/Local/Temp/ape5/entrega/'
os.makedirs(W, exist_ok=True)
B = 'C:/Users/henry/Documents/UTA/IHC/APE5/APE5_Fase1/'
CAP = B + '04_capturas/'
DOC = B + '06_documento/'
REPO = sys.argv[1] if len(sys.argv) > 1 else 'https://github.com/Hlagua/APE5_IHC'

d = Doc(W)
E = d.E
out = E[0:3]
out.append(d.replace_t(E[3], 'Refactorización con SOLID, Clean Architecture y Patrones Creacionales – Tipo B: Venta de motocicletas',
                       'APE 5. Fase 1 · Del boceto a la interfaz web adaptable (HTML5, CSS Mobile-First e interacción) – Entrega'))
out.append(E[4])
out.append(d.replace_t(E[5], 'Sexto - A', 'Quinto - A'))
out.append(E[6])
for n in ['Cobos Taco Alison Marcela', 'Cevallos Goyes Melany Saleth', 'Ramos Jacome Carlos Giovanni']:
    out.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="3540"/><w:rPr>%s</w:rPr></w:pPr>%s</w:p>' % (TNR, run(n)))
out.append(d.replace_t(E[7], 'Patrones de Software', 'Interacción Humano Computador'))
out.append(d.replace_t(E[8], 'Ing. Alex Maigua, Mg.', 'Ing. Mg. José Caiza'))
out.append(d.EMPTY)

R = []
R.append(d.link_para('Repositorio de GitHub (código HTML/CSS/JS y docs/proyecto.md): ', REPO))
R.append(d.para('**Proyecto del grupo:** Usability Test Dashboard 2.0 · pantalla «Bitácora de observaciones» (/dashboard/test-plan/record). '
                '**Pantalla transformada en clase:** boceto A «Elige tu taller» (caso Aula Abierta), publicada en src/index.html, src/estilos.css y src/reserva.js.'))

R.append(d.sub('1. Ficha de aplicación del proyecto'))
R.append(d.table([1700, 1500, 1600, 1500, 1844], [
    ['Actor', 'Tarea', 'Dato decisivo', 'Acción principal', 'Estado final'],
    ['Moderador/a de la prueba', 'Registrar cómo le fue a un participante en una tarea', 'Éxito, tiempo (s) y número de errores', 'Agregar al backlog', 'Hallazgo agregado al backlog y confirmado en role="status"'],
    ['Estudiante (caso de clase)', 'Reservar un taller', 'Horario y lugar', 'Reservar un lugar', 'Reserva confirmada y cupo descontado'],
]))
R.append(d.para('**Requisito (RF-OBS-01):** el moderador debe registrar por cada participante y tarea el éxito, el tiempo y los errores observados, y enviar el hallazgo '
                'al backlog sabiendo si el envío se completó o falló.'))
R.append(d.para('**Regla de negocio:** las métricas de una observación no pueden ser inválidas: un número de errores negativo se corrige a 0 y un tiempo menor que 1 s se corrige a 1 '
                '(handleObsChange en ObservationRecordPage.tsx). «Errores» es obligatorio.'))
R.append(d.para('**Criterio de aceptación medible:** al escribir −3 en «Errores» el valor queda en 0, y al escribir 0 en «Tiempo (s)» queda en 1, en 5 de 5 intentos (100 %); '
                'el backlog contiene 0 observaciones con errores < 0 o tiempo < 1.'))
R.append(d.para('**Decisión HCI justificada:** en móvil la tarjeta (dato decisivo + acción) y el resumen (estado + cancelar) van en una sola columna, en el mismo orden que el HTML, '
                'y desde 48rem (768 px) pasan a dos columnas sin reordenar el código. En el boceto A, con 960 px fijos, a 360 px el resumen «Mi reserva» quedaba fuera de la pantalla; '
                'ahora el estado aparece debajo de la acción sin scroll horizontal ni zoom (H1 Visibilidad del estado, WCAG 1.4.10 Reajuste). Al confirmar, «Reservar» queda '
                'disabled y el foco pasa a «Cancelar mi reserva»; al cancelar, vuelve a «Reservar» (H3 Control y libertad, WCAG 2.4.3 Orden del foco).'))

R.append(d.sub('2. Capturas preliminares del cambio de distribución'))
R.append(d.figure(CAP + 'movil-360-confirmada.png', 2.3, 'Figura 1. Móvil a 360 px: una columna; «Mi reserva» queda debajo de la tarjeta.'))
R.append(d.figure(CAP + 'escritorio-1366-confirmada.png', 5.8, 'Figura 2. Escritorio a 1366 px: dos columnas desde 48rem, con el mismo orden del HTML.'))

R.append(d.sub('3. Revisión entre pares e hipótesis para la fase 2'))
R.append(d.table([2000, 1300, 1500, 3344], [
    ['Tarea de la pareja revisora', 'Móvil 360 px', 'Escritorio 1366 px', 'Observación'],
    ['Localizar el horario', '[completar]', '[completar]', '[completar en clase]'],
    ['Reservar', '[completar]', '[completar]', '[completar en clase]'],
    ['Cancelar', '[completar]', '[completar]', '[completar en clase]'],
]))
R.append(d.para('**Hipótesis:** al confirmar o cancelar con teclado, quien usa lector de pantalla (NVDA o TalkBack) escucha el mensaje de role="status" y entiende que el foco '
                'pasó al botón siguiente. **Medición en la fase 2:** se valida si al menos 4 de 5 participantes repiten en voz alta el estado de su reserva sin buscarlo '
                'visualmente y sin preguntar dónde quedó el foco.'))
out += R
out.append(E[132])
print('ok', d.save(out, DOC + 'APE5_Fase1_Entrega.docx'))
