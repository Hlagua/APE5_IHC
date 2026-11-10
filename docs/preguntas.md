# APE 5 · Fase 2 · Acta de defensa cruzada QA/UX

- **Grupo que defiende:** Grupo 5 — Alison Cobos (@Itsuna18) · Melany Cevallos (@SalyC15) · Carlos Ramos (@carlitosgiovanniramos) · Henry Lagua (@Hlagua)
- **Grupo retador (QA/UX):** G3 — integrantes: ______________________________________
- **Fecha:** 10/11/2026 · **Hora de inicio:** ______ · **Hora de cierre:** ______
- **Responsable del acta:** Alison Marcela Cobos Taco (@Itsuna18) · rama `interfaz-responsive` · Issue #3 · **Revisión cruzada:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos)

> Cada respuesta se apoya en un archivo del repositorio, una medición de `resultados/pruebas.md` o una observación de `resultados/checklist.md`. Durante la defensa se anota en «Registro en la sesión» lo que realmente se dijo.

---

## Pregunta técnica 1 · Punto de corte en CSS y orden de tabulación

**Formulación esperada (G3):** «¿Cómo garantizan que el paso a dos columnas en 768 px no cambie el orden en que se recorre la página con Tab?»

**Respuesta preparada:**
1. **Código:** en `src/estilos.css` la regla base es `.disposicion { display: grid; grid-template-columns: 1fr; }`. Dentro de `@media (min-width: 48rem)` solo cambia `grid-template-columns: 3fr 2fr`. No se usa `order`, `grid-row`, `flex-direction: row-reverse` ni posicionamiento absoluto, así que la cuadrícula **coloca** los elementos sin **reordenarlos**.
2. **Orden del DOM:** en `src/index.html` la tarjeta (`<article>` con `#btn-reservar`) va antes que el resumen (`<section>` con `#btn-cancelar`). El orden visual (de arriba abajo en móvil, de izquierda a derecha en escritorio) coincide con el orden de lectura y de foco (WCAG 1.3.2 y 2.4.3).
3. **Por qué 48rem:** son 768 px con la fuente predeterminada de 16 px. Si la persona aumenta el tamaño de letra del navegador, el corte se desplaza y conserva una columna más tiempo, lo que protege la legibilidad.
4. **Medición:** a 767 px hay 1 columna (735 px) y a 768 px hay 2 (417,6 px · 278,4 px), con 0 px de desborde en ambos casos. Recorriendo con Tab a 360, 768 y 1366 px, el foco sigue la secuencia `#btn-reservar` → `#btn-cancelar` (`resultados/pruebas.md`, secciones 2 y 4).

**Demostración en vivo:** DevTools → `Ctrl+Shift+M` → arrastrar el ancho entre 767 y 768 px mientras se pulsa Tab.

**Registro en la sesión:**
- Pregunta textual de G3: ______________________________________________
- Respuesta dada por (integrante): ______________ · ¿Réplica de G3?: ______________
- Valoración del grupo retador: ☐ Satisfactoria ☐ Parcial ☐ No satisfactoria

---

## Pregunta técnica 2 · Prevención de envíos duplicados y gestión del foco

**Formulación esperada (G3):** «¿Qué impide que el usuario reserve dos veces y qué pasa con el foco al confirmar y al cancelar?»

**Respuesta preparada:**
1. **Bloqueo en la interfaz:** en `src/interaccion.js`, la función `pintar("confirmada")` pone `btnReservar.disabled = true` y cambia el texto a «Ya tienes un lugar». Un `<button disabled>` no recibe foco ni dispara `click`.
2. **Doble verificación:** el controlador sale antes si el estado ya es confirmada (`if (resumen.dataset.estado === "confirmada") return;`), y `ReservaAPI.confirmarReserva()` en `src/api.js` rechaza una segunda confirmación y también reservar sin cupos.
3. **Foco al confirmar:** como el botón que tenía el foco queda deshabilitado, `btnCancelar.focus()` lleva el foco a la siguiente acción posible. Sin esto, el foco quedaría en `<body>` y quien usa teclado o lector de pantalla perdería su posición (WCAG 2.4.3).
4. **Foco al cancelar:** `#btn-cancelar` se oculta (`hidden`), así que `btnReservar.focus()` devuelve el foco a «Reservar un lugar».
5. **Medición:** con teclas reales, Tab → Enter deja el foco en `#btn-cancelar` con cupos 12 → 11. Un `click()` forzado sobre el botón deshabilitado no cambia los cupos (11 → 11). Espacio sobre Cancelar devuelve el foco a `#btn-reservar` con cupos 11 → 12 (`resultados/pruebas.md`, sección 4).
6. **Hallazgo propio y corrección (H-01):** en nuestras pruebas con teclado vimos que un doble Enter reservaba y cancelaba al instante, porque el segundo Enter caía sobre «Cancelar». Ahora «Cancelar» ignora activaciones durante 600 ms después de confirmar (`MARGEN_DOBLE_PULSACION_MS`). Antes el doble Enter terminaba en «cancelada» con 12 cupos; ahora termina en «confirmada» con 11 (`resultados/pruebas.md`, sección 5).
7. **Visibilidad del estado:** `<p id="estado" role="status" aria-live="polite">` anuncia el cambio sin mover el foco (Nielsen H1).

**Demostración en vivo:** Tab → Enter → observar el anillo de foco ámbar sobre «Cancelar mi reserva» → Enter → el foco vuelve a «Reservar un lugar».

**Registro en la sesión:**
- Pregunta textual de G3: ______________________________________________
- Respuesta dada por (integrante): ______________ · ¿Réplica de G3?: ______________
- Valoración del grupo retador: ☐ Satisfactoria ☐ Parcial ☐ No satisfactoria

---

## Objeción de diseño · Ajuste geométrico frente a comprensión real

**Formulación esperada (G3):** «Que la página quepa en 360 px no prueba que el usuario la entienda mejor.»

**Respuesta preparada:**
1. **Estamos de acuerdo.** El 0 px de desborde es una condición **necesaria pero no suficiente**: prueba que nada queda fuera de la pantalla, no que la persona comprenda qué hacer.
2. **Nuestra propia medición lo confirma.** Con emulación móvil, el boceto A también «cabe» (`scrollWidth = innerWidth = 960`), pero porque Chromium aleja la página al 37,5 % y el texto de 18 px se ve de 6,8 px. Cumple la geometría y aun así es ilegible. El ajuste por sí solo no prueba nada.
3. **Por eso separamos dos tipos de evidencia:**
   - *Técnica* (`resultados/pruebas.md`): desborde, punto de corte, orden de foco y bloqueo de duplicados. Es medible y reproducible.
   - *Con personas* (`resultados/checklist.md`): tiempo, errores de navegación, solicitudes de ayuda y si el participante dice su estado sin buscarlo.
4. **Lo que sí aporta el diseño a la comprensión:** el dato decisivo (horario y lugar en `<dl>`) se lee antes que la acción; el estado aparece justo debajo de la acción en móvil, con texto, color y borde; el botón cambia a «Ya tienes un lugar»; y existe un camino visible para deshacer.
5. **Límite honesto:** con una muestra de ______ participantes no se puede afirmar que la comprensión mejora de forma general. Es evidencia preliminar que se debe ampliar (véase `docs/conclusiones.md`, «Siguiente iteración»).

**Dato de la observación en aula para citar:** _(completar desde `resultados/checklist.md`)_ P-__ completó la tarea en ____ s con ____ errores y ____ ayudas; dificultad observada: «______________».

**Registro en la sesión:**
- Objeción textual de G3: ______________________________________________
- Respuesta dada por (integrante): ______________ · ¿Réplica de G3?: ______________
- Valoración del grupo retador: ☐ Aceptada ☐ Aceptada con reservas ☐ No aceptada

---

## Preguntas adicionales del docente o de G3

| N.º | Pregunta | Respondió | Respuesta resumida | Evidencia citada |
| :---: | :--- | :--- | :--- | :--- |
| 1 | | | | |
| 2 | | | | |

## Acuerdos y compromisos derivados de la defensa

- ________________________________________________________________

**Firmas:** Grupo 5 (defiende) ____________________ · Grupo retador G3 ____________________
