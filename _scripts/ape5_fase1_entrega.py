"""Documento corto de la fase 1 del APE 5 · CaféU «Mi pedido» (ficha, dos capturas e hipótesis).

Uso: python _scripts/ape5_fase1_entrega.py [URL_REPO]
(requiere las capturas de evidencias/, generadas con _scripts/ape5_fase2_evidencias.py)
Genera 06_documento/APE5_Fase1_Entrega_CafeU.docx (y .pdf con Word).
"""
import os, sys, subprocess
sys.path.insert(0, 'C:/Users/henry/Documents/UTA/IHC/APE4/_scripts')
from docx_lib import Doc, TNR, run

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
EV = REPO + 'evidencias/'
DOC = REPO + '06_documento/'
W = os.environ.get('TEMP', '/tmp').replace('\\', '/') + '/ape5/fase1_cafeu/'
os.makedirs(W, exist_ok=True)
REPO_URL = sys.argv[1] if len(sys.argv) > 1 else 'https://github.com/Hlagua/APE5_IHC'

d = Doc(W)
E = d.E
out = E[0:3]
out.append(d.replace_t(E[3], 'Refactorización con SOLID, Clean Architecture y Patrones Creacionales – Tipo B: Venta de motocicletas',
                       'APE 5. Fase 1 · Del boceto a la interfaz web adaptable (HTML5, CSS Mobile-First e interacción) · caso CaféU – Entrega · Grupo 5'))
out.append(E[4])
out.append(d.replace_t(E[5], 'Sexto - A', 'Quinto - A'))
out.append(E[6])
for n in ['Cevallos Goyes Melany Saleth', 'Cobos Taco Alison Marcela', 'Ramos Jacome Carlos Giovanni']:
    out.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="3540"/><w:rPr>%s</w:rPr></w:pPr>%s</w:p>' % (TNR, run(n)))
out.append(d.replace_t(E[7], 'Patrones de Software', 'Interacción Humano Computador'))
out.append(d.replace_t(E[8], 'Ing. Alex Maigua, Mg.', 'Ing. Mg. José Caiza'))
out.append(d.EMPTY)

R = []
R.append(d.link_para('Repositorio de GitHub (código HTML/CSS/JS y docs/proyecto.md): ', REPO_URL))
R.append(d.para('**Proyecto del grupo:** CaféU, la aplicación de pedidos de la cafetería universitaria del APE 4. **Pantalla transformada:** «Mi pedido → Confirmar y pagar», '
                'de un boceto de escritorio con 960 px fijos (prototipos/prototipo-A.html) a una interfaz adaptable (src/index.html, src/estilos.css, src/interaccion.js).'))

R.append(d.sub('1. Ficha de aplicación del proyecto'))
R.append(d.table([2400, 5744], [
    ['Campo', 'CaféU · «Mi pedido»'],
    ['Actor', 'Estudiante universitario con poco tiempo entre clases que pide desde el celular'],
    ['Tarea principal', 'Confirmar y pagar su pedido para retirarlo sin hacer fila'],
    ['Dato clave', 'Productos, total $4.25, retiro en el Edificio central (10 min) y tarjeta universitaria con su saldo'],
    ['Acción principal', '«Confirmar y pagar · $4.25»'],
    ['Resultado visible', '«Pedido #A24 confirmado y pagado ($4.25). Estará listo en unos 10 minutos en el Edificio central.» en role="status"'],
    ['Mecanismo para corregir o cancelar', '«Editar» antes de pagar; «Cancelar pedido» después, con devolución de los $4.25'],
]))
R.append(d.para('**Requisito (RF-PED-01):** el estudiante debe poder confirmar y pagar su pedido una sola vez, ver de inmediato el número de pedido y cuándo retirarlo, '
                'y cancelarlo con devolución si se equivocó.'))
R.append(d.para('**Regla y criterio de aceptación medible:** un pedido se cobra una sola vez. Con el pedido pagado, 5 intentos de activar «Confirmar y pagar» dejan el '
                'saldo en $5.75 (0 cobros duplicados en 5 de 5); un doble Enter no cancela el pedido recién pagado.'))
R.append(d.para('**Decisión HCI justificada:** en el boceto A, el panel «Estado del pedido» empieza en x = 600 px; a 360 px queda fuera de la pantalla y el estudiante paga sin '
                'ver si se cobró, el mismo temor de doble cobro que encontramos en el APE 4 (D1, H9). En la versión B, el pedido y el estado van en una sola columna, en el orden '
                'del HTML, y desde 48rem (768 px) pasan a dos columnas sin reordenar el código (H1 Visibilidad, WCAG 1.4.10). Al pagar, el botón queda disabled y el foco pasa '
                'a «Cancelar pedido» (H5, WCAG 2.4.3).'))

R.append(d.sub('2. Capturas del cambio de distribución'))
R.append(d.figure(EV + 'B-360-confirmada.png', 2.4, 'Figura 1. Móvil a 360 px: una columna; el estado del pedido #A24 queda debajo del botón (desborde 0 px).'))
R.append(d.figure(EV + 'B-1366-confirmada.png', 5.8, 'Figura 2. Escritorio a 1366 px: dos columnas desde 48rem, con el mismo orden del HTML (desborde 0 px).'))

R.append(d.sub('3. Hipótesis para validar en la fase 2'))
R.append(d.para('**Hipótesis:** en un viewport de 360 px, un estudiante que no conoce la pantalla confirma su pedido y dice su número de pedido y si ya pagó, sin buscarlo '
                'y sin pedir ayuda. **Medición:** se valida si al menos 4 de 5 participantes de otros grupos lo logran; se registra en resultados/checklist.md.'))
out += R
out.append(E[132])
dest = d.save(out, DOC + 'APE5_Fase1_Entrega_CafeU.docx')
print('ok', dest)

ps = ("$w=New-Object -ComObject Word.Application;$w.Visible=$false;try{$d=$w.Documents.Open('%s',$false,$true);"
      "$d.SaveAs([ref]'%s',[ref]17);$d.Close($false)}finally{$w.Quit()}") % (dest.replace('/', '\\'), dest.replace('/', '\\')[:-5] + '.pdf')
r = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True)
print('pdf', 'ok' if r.returncode == 0 else 'no generado: ' + r.stderr[:200])
