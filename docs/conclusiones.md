# APE 5 · Conclusiones finales · CaféU

- **Grupo:** 5 · **Responsable:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · rama `pruebas-informe` · Issue #4
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)

## 1. Requisito

**RF-PED-01:** en CaféU, el estudiante debe poder, **desde su teléfono**, confirmar y pagar su pedido una sola vez, ver de inmediato su número de pedido y cuándo retirarlo, y cancelarlo con devolución si se equivocó, sin desplazarse horizontalmente y con teclado si lo necesita.

## 2. Decisión

Llevamos la pantalla «Mi pedido» del prototipo móvil del APE 4 a una interfaz web **Mobile-First**:
- HTML5 semántico en el orden de la tarea: `<article>` con los productos y el dato clave en un `<dl>` (total, retiro y pago) antes de «Confirmar y pagar», seguido de `<section>` con el estado (`role="status"`) y «Cancelar pedido».
- Una columna por defecto y dos solo desde `@media (min-width: 48rem)`, sin reordenar el DOM.
- Tres momentos (pendiente → confirmado → cancelado). Al pagar, `disabled` impide el doble cobro, el foco pasa a «Cancelar pedido» y un margen de 600 ms evita la cancelación accidental (H-01).

## 3. Dato observado

- **En el laboratorio (medido):** 0 px de desborde en 320, 360, 768 y 1366 px, frente a +640, +600 y +192 px del boceto A. El cambio de columnas ocurre exactamente entre 767 y 768 px. Con teclado, el saldo baja de $10.00 a $5.75 una sola vez, cancelar devuelve exactamente $4.25 y la suite automática da 10 de 10 (`resultados/pruebas.md`).
- **Hallazgo propio corregido (H-01):** sin el margen, un doble Enter pagaba y cancelaba el pedido al instante; con el margen, el pedido queda pagado.
- **Con personas (aula):** _(completar con `resultados/checklist.md`)_ ____ de ____ participantes de otros grupos dijeron su número de pedido y si ya habían pagado sin buscarlo; tiempo medio en la versión B: ____ s, con ____ errores de navegación y ____ solicitudes de ayuda. Dificultad más repetida: «______».

## 4. Limitación

- La evidencia con personas es **preliminar**: pocos participantes, estudiantes de la misma carrera y un solo contexto (DevTools en un computador, no un teléfono real).
- **No se probó con lectores de pantalla reales** (NVDA, TalkBack): el anuncio de `role="status"` solo está verificado en el código.
- El pago es **simulado**: `src/api.js` guarda el pedido en `sessionStorage` y el saldo de $10.00 es ficticio. No hay pasarela ni servidor que garantice el cobro único entre dispositivos.
- El 0 px de desborde no demuestra por sí solo que se entienda mejor: con emulación móvil, el boceto A también «cabe», pero con texto de 6,75 px.

## 5. Siguiente iteración

1. Repetir la observación con **al menos 5 participantes en teléfonos reales** y con NVDA y TalkBack, midiendo si dicen su número de pedido y si pagaron sin buscarlo.
2. Llevar el cobro único al servidor (clave de idempotencia por pedido), manteniendo `disabled` y el margen de 600 ms como primera barrera en la interfaz.
3. Integrar el estado de pago en «Mis pedidos» (W7 del APE 4) y recuperar del APE 4 el caso de **pago rechazado** («No se realizó ningún cobro»), aplicando el mismo patrón adaptable.
