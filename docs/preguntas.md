# APE 5 · Acta de defensa cruzada QA/UX · CaféU «Mi pedido»

- **Grupo que defiende:** Grupo 5 — Henry Lagua (@Hlagua) · Melany Cevallos (@SalyC15) · Alison Cobos (@Itsuna18) · Carlos Ramos (@carlitosgiovanniramos)
- **Grupo retador (QA/UX):** G3 — integrantes: David Morales, Pamela Quinatoa, Kevin Salazar
- **Fecha:** 11/11/2026 · **Hora de inicio:** 09:30 · **Hora de cierre:** 10:15
- **Responsable del acta:** Alison Marcela Cobos Taco (@Itsuna18) · rama `interfaz-responsive` · Issue #3 · **Revisión cruzada:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos)

> Cada respuesta se apoya en un archivo del repositorio, una medición de `resultados/pruebas.md` o una observación de `resultados/checklist.md`. En «Registro en la sesión» se anota **lo que realmente se dijo**.

---

## Pregunta técnica 1 · Punto de corte en CSS y orden de tabulación

**Formulación esperada (G3):** «¿Qué cambia en CSS al cruzar 48rem y cómo aseguran que no se altere el recorrido con Tab?»

**Respuesta preparada:**
1. **Código:** en `src/estilos.css` la base es `.disposicion { display: grid; grid-template-columns: 1fr; }`. Dentro de `@media (min-width: 48rem)` solo cambian `grid-template-columns: 3fr 2fr`, `align-items` y `gap`. No usamos `order`, `grid-row` ni posicionamiento: la cuadrícula **coloca** los bloques, no los **reordena**.
2. **Orden del DOM:** en `src/index.html` primero va el pedido (`<article>` con el total y «Confirmar y pagar») y después el estado (`<section>` con `role="status"` y «Cancelar pedido»). El orden visual (de arriba abajo en el teléfono, de izquierda a derecha en el computador) coincide con el de lectura y el de Tab (WCAG 1.3.2 y 2.4.3).
3. **Por qué 48rem:** son 768 px con la fuente de 16 px. Si el estudiante agranda la letra del navegador, el corte se desplaza y la pantalla mantiene una columna por más tiempo.
4. **Medición:** a 767 px hay 1 columna (735,3 px) y a 768 px hay 2 (417,6 · 278,4 px), con 0 px de desborde en ambos. El foco recorre `#btn-confirmar` → `#btn-cancelar` en 320, 360, 768 y 1366 px (`resultados/pruebas.md`, secciones 2 y 4).

**Demostración en vivo:** DevTools → `Ctrl+Shift+M` → mover el ancho entre 767 y 768 px y pulsar Tab.

**Registro en la sesión:**
- Pregunta textual de G3: ¿Qué cambia en CSS al cruzar el punto de corte de 48rem y cómo garantizan que no se altere el orden con Tab? ·
- Respuesta dada por (integrante): Melany Cevallos (@SalyC15) y Alison Cobos (@Itsuna18) · ¿Réplica de G3?: Verificaron el paso de 767 a 768 px en DevTools comprobando que el orden del DOM no se altera.
- Valoración del grupo retador: ☒ Satisfactoria ☐ Parcial ☐ No satisfactoria

---

## Pregunta técnica 2 · Pago duplicado y gestión del foco

**Formulación esperada (G3):** «¿Qué impide que el estudiante pague dos veces y dónde queda el foco al confirmar y al cancelar?»

**Respuesta preparada:**
1. **Bloqueo en la interfaz:** `pintar()` en `src/interaccion.js` pone `btnConfirmar.disabled = true` y cambia el texto a «Pedido #A24 pagado». Un `<button disabled>` no recibe foco ni dispara `click`.
2. **Doble verificación:** el controlador sale si el estado ya es «confirmado», y `PedidoAPI.confirmarPedido()` en `src/api.js` rechaza un segundo cobro (`motivo: 'ya_confirmado'`). Es la respuesta directa al temor de doble cobro del APE 4 (D1).
3. **Foco al confirmar:** como el botón pulsado queda deshabilitado, `btnCancelar.focus()` lleva el foco a la siguiente acción posible. Sin esto, el foco caería en `<body>` y quien usa teclado o lector de pantalla perdería su lugar.
4. **Foco al cancelar:** «Cancelar pedido» se oculta (`hidden`) y `btnConfirmar.focus()` devuelve el foco a «Confirmar y pagar».
5. **Hallazgo propio H-01:** ese mismo traslado del foco hacía que un doble Enter pagara y cancelara al instante. Sin el margen, el resultado era «cancelado» con saldo $10.00; con el margen de 600 ms es «confirmado» con $5.75 (`resultados/pruebas.md`, sección 5).
6. **Medición:** con teclas reales, el saldo baja de $10.00 a $5.75 una sola vez; 5 intentos más no cobran (TC-07). Cancelar devuelve exactamente $4.25. La suite da 10 de 10.

**Demostración en vivo:** Tab → Enter Enter → el pedido sigue pagado y el foco está en «Cancelar pedido». Esperar 1 s → Espacio → se devuelven $4.25 y el foco vuelve a «Confirmar y pagar».

**Registro en la sesión:**
- Pregunta textual de G3: ¿Qué impide que el estudiante pague dos veces incluso con doble Enter y adónde va el foco al confirmar y cancelar? ·
- Respuesta dada por (integrante): Alison Cobos (@Itsuna18) y Carlos Ramos (@carlitosgiovanniramos) · ¿Réplica de G3?: Se comprobó en vivo la desactivación disabled, la guarda de 600 ms y la suite de 10 pruebas.
- Valoración del grupo retador: ☒ Satisfactoria ☐ Parcial ☐ No satisfactoria

---

## Objeción de diseño · Ajuste geométrico frente a comprensión real

**Formulación esperada (G3):** «Que la pantalla no desborde no significa que el estudiante entienda si ya pagó.»

**Respuesta preparada:**
1. **Estamos de acuerdo.** El 0 px de desborde es **necesario pero no suficiente**: asegura que nada quede fuera de la pantalla, no que el estudiante comprenda su estado.
2. **Nuestra medición lo demuestra.** Con emulación móvil, el boceto A también «cabe» (`scrollWidth = innerWidth = 960`), pero porque Chromium aleja la página al 37,5 % y el texto se ve de 6,75 px. Cumple la geometría y es ilegible.
3. **Por eso separamos dos evidencias:**
   - *Técnica* (`resultados/pruebas.md`): desborde, punto de corte, foco, cobro único. Es medible y reproducible.
   - *Con personas* (`resultados/checklist.md`): ¿el participante dice su número de pedido y si ya pagó sin buscarlo?, con tiempo, errores y ayudas.
4. **Qué aporta el diseño a la comprensión:** el total se lee antes de pagar; el estado aparece justo debajo del botón en el teléfono, con número de pedido, monto y tiempo de retiro; el panel cambia de color; el saldo visible baja una sola vez; y el botón dice «Pedido #A24 pagado».
5. **Límite honesto:** con 5 participantes, la evidencia es preliminar (véase `docs/conclusiones.md`).

**Dato de la observación para citar:** 5 de 5 participantes dijeron su número de pedido (#A24) y si habían pagado sin buscarlo; tiempo medio de 14,4 s (0 errores, 0 ayudas).

**Registro en la sesión:**
- Objeción textual de G3: Que la pantalla no desborde en 360 px no significa necesariamente que el estudiante entienda si ya pagó. ·
- Respuesta dada por (integrante): Henry Lagua (@Hlagua) y Carlos Ramos (@carlitosgiovanniramos) · ¿Réplica de G3?: Aceptaron la distinción técnica de pruebas.md frente a la evidencia con usuarios en checklist.md.
- Valoración del grupo retador: ☒ Aceptada ☐ Aceptada con reservas ☐ No aceptada

---

## Preguntas adicionales del docente o de G3

| N.º | Pregunta | Respondió | Respuesta resumida | Evidencia citada |
| :---: | :--- | :--- | :--- | :--- |
| 1 | ¿Qué ocurre si el usuario recarga la página tras pagar? | Alison Cobos | Se mantiene el estado confirmado en `sessionStorage` con saldo $5.75; para reiniciar se usa `PedidoAPI.reiniciar()`. | `src/api.js`, `pruebas.md` §6 |
| 2 | ¿Cómo responde el layout a 320 px si el nombre del producto es largo? | Melany Cevallos | Se aplicó `min-width: 0` y `overflow-wrap: anywhere` en los datos; `scrollWidth` permanece en 320 px sin desborde. | `estilos.css`, `pruebas.md` §2 |

## Acuerdos y compromisos derivados de la defensa

- Mantener la separación explícita entre validación geométrica (0 px desborde) y validación de comprensión con usuarios en futuras iteraciones.
- Incorporar en el sprint siguiente pruebas con lectores de pantalla reales (NVDA y TalkBack) en dispositivos móviles físicos.

**Firmas:** Grupo 5 (defiende): Henry Lagua, Melany Cevallos, Alison Cobos, Carlos Ramos · Grupo retador G3: David Morales, Pamela Quinatoa
