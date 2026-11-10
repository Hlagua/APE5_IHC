# APE 5 · Conclusiones finales

- **Grupo:** 5 · **Responsable:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · rama `pruebas-informe` · Issue #4
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)

## 1. Requisito

Una estudiante debe poder, **desde su teléfono**, consultar el horario y el lugar de un taller, reservar un lugar, comprobar que la reserva quedó hecha y deshacerla, sin desplazarse horizontalmente y usando solo el teclado si lo necesita. En el proyecto del grupo (Usability Test Dashboard 2.0), el equivalente es el requisito RF-OBS-01: registrar una observación y saber si el envío al backlog se completó.

## 2. Decisión

Cambiamos la cuadrícula fija de 960 px del boceto A por un diseño **Mobile-First**:
- HTML5 semántico en el orden de la tarea: `<article>` con el dato decisivo en un `<dl>` y la acción, seguido de `<section>` con el estado (`role="status"`) y la acción de deshacer.
- Una columna por defecto y dos columnas solo desde `@media (min-width: 48rem)`, sin reordenar el DOM.
- Tres estados explícitos (disponible → confirmada → cancelada). Al confirmar, `disabled` bloquea la segunda reserva, y el foco pasa siempre al control que sigue disponible.

## 3. Dato observado

- **En el laboratorio (medido):** 0 px de desborde horizontal en 320, 360, 768 y 1366 px, frente a +640, +600 y +192 px del boceto A en los tres primeros anchos. El cambio de columnas ocurre exactamente entre 767 y 768 px. Con teclado, Tab → Enter reserva y deja el foco en «Cancelar»; un clic forzado sobre el botón deshabilitado no descuenta otro cupo (`resultados/pruebas.md`).
- **Hallazgo propio corregido (H-01):** un doble Enter reservaba y cancelaba al instante. Con un margen de 600 ms en «Cancelar», el doble Enter ahora deja la reserva confirmada (antes: cancelada con 12 cupos; después: confirmada con 11).
- **Con personas (aula):** _(completar con `resultados/checklist.md`)_ con ____ participantes de otros grupos, el tiempo medio fue ____ s, con ____ errores de navegación y ____ solicitudes de ayuda. La dificultad más repetida fue «______».

## 4. Limitación

- La evidencia con personas es **preliminar**: pocos participantes, todos estudiantes de la carrera y en un solo contexto (aula, DevTools en un computador, no en un teléfono real).
- **No se probó con lectores de pantalla reales** (NVDA, TalkBack), así que el anuncio de `role="status"` solo está verificado en el código, no con usuarios.
- El estado se guarda en `sessionStorage` del navegador: no hay un servidor que controle los cupos entre varias personas, así que dos estudiantes podrían «tener» el mismo último cupo.
- El ajuste geométrico (0 px de desborde) no demuestra por sí solo que se entienda mejor. Nuestra propia medición lo muestra: con emulación móvil, el boceto A «cabe», pero con texto de 6,8 px.

## 5. Siguiente iteración

1. Repetir la observación con **al menos 5 participantes en teléfonos reales** y con NVDA y TalkBack. La hipótesis se valida si al menos 4 de 5 dicen el estado de su reserva sin buscarlo.
2. Llevar la validación de cupos a un servidor (API real con control de concurrencia), manteniendo el bloqueo `disabled` como prevención en la interfaz.
3. Aplicar el mismo patrón (dato decisivo → acción → estado con `role="status"` → deshacer) a la pantalla «Bitácora de observaciones» del Usability Test Dashboard, y medirla con las mismas cuatro resoluciones.
