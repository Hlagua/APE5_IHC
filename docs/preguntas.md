# APE 5 · Fase 2 · Acta de defensa cruzada QA/UX

- **Grupo que defiende:** Grupo 5 — Alison Cobos (@Itsuna18) · Melany Cevallos (@SalyC15) · Carlos Ramos (@carlitosgiovanniramos) · Henry Lagua (@Hlagua)
- **Grupo retador (QA/UX):** Grupo 3 (G3) — Equipo evaluador asignado en aula
- **Fecha:** 10/11/2026 · **Hora de inicio:** 11:00 · **Hora de cierre:** 11:30
- **Responsable del acta:** Alison Marcela Cobos Taco (@Itsuna18) · rama `interfaz-responsive` · Issue #3 · **Revisión cruzada:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos)

> Cada respuesta se apoya en un archivo del repositorio, una medición de `resultados/pruebas.md` y una observación empírica de `resultados/checklist.md`.

---

## Pregunta técnica 1 · Punto de corte en CSS y orden de tabulación

**Formulación esperada (G3):** «¿Cómo garantizan que el paso a dos columnas en 768 px no cambie el orden en que se recorre la página con Tab?»

**Respuesta técnica fundamentada:**
1. **Código CSS:** en `src/estilos.css` la regla base es `.disposicion { display: grid; grid-template-columns: 1fr; gap: 1rem; }`. Dentro de `@media (min-width: 48rem)` únicamente cambia `grid-template-columns: 3fr 2fr; align-items: start; gap: 1.5rem;`. No se usa `order`, `grid-row`, `flex-direction: row-reverse` ni posicionamiento absoluto, por lo que CSS Grid **distribuye espacialmente** los contenedores sin alterar su secuencia lógica.
2. **Orden del DOM:** en `src/index.html` la tarjeta (`<article>` con `#btn-reservar`) antecede al resumen (`<section>` con `#btn-cancelar`). El orden visual (de arriba abajo en móvil, de izquierda a derecha en escritorio) coincide exactamente con el orden del árbol DOM y la secuencia de foco por teclado (WCAG 1.3.2 Secuencia significativa y WCAG 2.4.3 Orden del foco).
3. **Justificación de `48rem`:** equivale a `768 px` con la fuente base de `16 px`. Si el usuario incrementa el tamaño de fuente del navegador (ej. a 20 px o 24 px por baja visión), el umbral en `rem` escala proporcionalmente y mantiene el diseño en una sola columna hasta que realmente exista espacio suficiente para dos columnas legibles.
4. **Medición verificable:** a `767 px` se mide 1 columna (`735 px`) y a `768 px` conmuta a 2 columnas (`417,6 px` y `278,4 px`), con `0 px` de desborde en ambos casos. Recorriendo con `Tab` a 320, 360, 768 y 1366 px, el foco sigue invariablemente la ruta `#btn-reservar` → `#btn-cancelar` (`resultados/pruebas.md`, secciones 2 y 4).

**Demostración en vivo:** DevTools → `Ctrl+Shift+M` → variar el ancho entre 767 y 768 px mientras se pulsa `Tab`.

**Registro en la sesión:**
- Pregunta textual de G3: ¿Qué cambia en CSS al cruzar el punto de corte de 48rem y cómo aseguran no alterar el recorrido con Tab? ·
- Respuesta dada por (integrante): Melany Cevallos (@SalyC15) y Alison Cobos (@Itsuna18) · ¿Réplica de G3?: Confirmaron en DevTools el paso de 767 a 768 px sin cambio de orden DOM.
- Valoración del grupo retador: ☒ Satisfactoria ☐ Parcial ☐ No satisfactoria

---

## Pregunta técnica 2 · Prevención de envíos duplicados y gestión del foco

**Formulación esperada (G3):** «¿Qué impide que el usuario reserve dos veces y qué pasa con el foco al confirmar y al cancelar?»

**Respuesta técnica fundamentada:**
1. **Bloqueo en la interfaz (UI):** en `src/interaccion.js`, la función `pintar("confirmada")` asigna `btnReservar.disabled = true` y actualiza la etiqueta a «Ya tienes un lugar». Un control nativo `<button disabled>` queda excluido del orden de tabulación y no dispara eventos `click` ni `keydown`.
2. **Doble verificación en controlador y API:** el manejador de evento aborta inmediatamente si el estado ya es confirmado (`if (resumen.dataset.estado === "confirmada") return;`), y `ReservaAPI.confirmarReserva()` en `src/api.js` valida que `estado !== "confirmada"` y `cuposDisponibles > 0` antes de descontar en `sessionStorage`.
3. **Traslado del foco al confirmar:** dado que el botón recién pulsado pasa a `disabled`, invocamos explícitamente `btnCancelar.focus()` para situar el foco en la siguiente acción válida («Cancelar mi reserva»). Sin esta transferencia explícita, el navegador perdería el foco enviándolo a `<body>`, desorientando a usuarios de teclado o lectores de pantalla (WCAG 2.4.3).
4. **Retorno del foco al cancelar:** cuando el usuario cancela su reserva, `#btn-cancelar` pasa a `hidden = true`, por lo que `btnReservar.focus()` restituye el foco al botón principal «Reservar un lugar».
5. **Medición verificable:** en la prueba de teclado real, `Tab → Enter` posiciona `document.activeElement` en `#btn-cancelar` y reduce los cupos de 12 a 11. Cinco llamadas forzadas a `btnReservar.click()` mantienen los cupos en **11** (0 duplicados en 5/5 intentos). Pulsar `Espacio` o `Enter` sobre Cancelar devuelve el foco a `#btn-reservar` y restituye los cupos a 12 (`resultados/pruebas.md`, sección 4).
6. **Hallazgo propio y corrección (H-01):** detectamos que un doble `Enter` muy rápido (< 600 ms) reservaba en la primera pulsación y cancelaba en la segunda porque el foco ya había saltado a «Cancelar». Implementamos una guarda temporal de `600 ms` (`MARGEN_DOBLE_PULSACION_MS` en `src/interaccion.js`) que ignora activaciones involuntarias inmediatas sobre «Cancelar», cumpliendo la Heurística H5 de Nielsen (Prevención de errores).
7. **Anuncio accesible:** `<p id="estado" role="status" aria-live="polite">` notifica el cambio de estado a tecnologías de asistencia sin interrumpir el flujo (WCAG 4.1.3).

**Demostración en vivo:** `Tab → Enter` → verificar anillo de foco ámbar sobre «Cancelar mi reserva» → `Enter` → el foco regresa a «Reservar un lugar».

**Registro en la sesión:**
- Pregunta textual de G3: ¿Cómo evitan reservas repetidas incluso con doble Enter y adónde se mueve el foco tras confirmar y cancelar? ·
- Respuesta dada por (integrante): Alison Cobos (@Itsuna18) y Carlos Ramos (@carlitosgiovanniramos) · ¿Réplica de G3?: Verificaron el bloqueo con doble Enter y la suite `tests/test_runner.html` (9/9 aprobadas).
- Valoración del grupo retador: ☒ Satisfactoria ☐ Parcial ☐ No satisfactoria

---

## Objeción de diseño · Ajuste geométrico frente a comprensión real

**Formulación esperada (G3):** «Que la página quepa en 360 px no prueba que el usuario la entienda mejor.»

**Respuesta técnica y de principios HCI:**
1. **Acuerdo conceptual:** Coincidimos en que lograr `0 px` de desborde horizontal (`scrollWidth <= innerWidth`) es una **condición necesaria pero no suficiente**: garantiza el ajuste geométrico en el viewport (WCAG 1.4.10), pero por sí sola no garantiza comprensión cognitiva.
2. **Demostración con nuestra propia medición:** En emulación móvil de Chromium, el Boceto A también «cabe» sin barra horizontal porque el navegador escala el viewport de 960 px a `visualViewport.scale = 0,375`, reduciendo la fuente de 18 px a **6,8 px efectivos**. Cumple el encaje geométrico en pantalla, pero es completamente ilegible e incomprensible.
3. **Separación rigurosa de dos niveles de evidencia:**
   - *Evidencia técnica (`resultados/pruebas.md`):* mide geometría (`scrollWidth = innerWidth` a 320, 360, 768 y 1366 px), escala `1:1` con texto real de 16 px, punto de corte en `48rem` y ciclo de foco.
   - *Evidencia empírica con usuarios (`resultados/checklist.md`):* evalúa comprensión mediante una consigna neutral sin nombrar botones, midiendo tiempo de tarea, errores de navegación y solicitudes de ayuda.
4. **Decisiones HCI que producen la comprensión real:**
   - **Jerarquía semántica (H6 Reconocimiento antes que recuerdo):** la lista de definición `<dl>` presenta Horario, Lugar y Cupos **antes** del botón de acción, para que el usuario decida con información completa.
   - **Visibilidad del estado (H1):** el panel «Mi reserva» se ubica inmediatamente debajo del botón en móvil, cambia de color según `data-estado` (verde en confirmada, ámbar en cancelada), actualiza el texto del botón a «Ya tienes un lugar» y anuncia el resultado en `<p role="status">`.
   - **Control y libertad (H3):** el botón «Cancelar mi reserva» aparece en el mismo bloque visual y recibe el foco automáticamente.
5. **Dato observado en aula que respalda la comprensión:** En `resultados/checklist.md`, mientras en el Boceto A (P-03) el participante tardó **35 s**, cometió **2 errores** de paneo y pidió **1 ayuda** sin poder confirmar, en la Versión B (P-01, P-02, P-04) el tiempo medio bajó a **14,7 s** (reducción del **58 %**) con **0 errores** y **0 solicitudes de ayuda**, y el 100 % identificó verbalmente el estado de su reserva sin buscarlo.

**Registro en la sesión:**
- Objeción textual de G3: Que la pantalla no desborde en 360 px no significa necesariamente que el usuario entienda la interfaz o el estado de su reserva. ·
- Respuesta dada por (integrante): Henry Lagua (@Hlagua) y Carlos Ramos (@carlitosgiovanniramos) · ¿Réplica de G3?: Aceptaron la distinción entre ajuste geométrico (pruebas.md) y evidencia empírica con usuarios (checklist.md).
- Valoración del grupo retador: ☒ Aceptada ☐ Aceptada con reservas ☐ No aceptada

---

## Preguntas adicionales del docente o de G3

| N.º | Pregunta | Respondió | Respuesta resumida | Evidencia citada |
| :---: | :--- | :--- | :--- | :--- |
| 1 | ¿Qué sucede si se recarga la página tras confirmar? | Alison Cobos | `src/api.js` persiste el estado y los 11 cupos en `sessionStorage`; al recargar, `interaccion.js` sincroniza el estado confirmado. Para iniciar limpio con otro participante se ejecuta `ReservaAPI.reiniciar()`. | `src/api.js`, `resultados/pruebas.md` §6 |
| 2 | ¿Cómo se comporta en pantallas aún más estrechas (320 px) con textos largos? | Carlos Ramos | Se probó a 320 × 720 px con un título de 81 caracteres; el contenedor ajusta las líneas manteniendo `scrollWidth = 320 px` (0 px de desborde). | `evidencias/B-320.png`, `resultados/pruebas.md` §2 |

## Acuerdos y compromisos derivados de la defensa

- Incorporar el patrón validado (`<dl>` decisivo → `<button>` con bloqueo + guarda de 600 ms → `<p role="status">` → acción de reversión con traslado de foco) en el componente `ObservationRecordPage.tsx` de nuestro proyecto grupal **Usability Test Dashboard 2.0**.
- En la siguiente iteración, reemplazar `sessionStorage` por un endpoint de backend real con control de concurrencia multiusuario y ejecutar pruebas con lectores de pantalla NVDA y TalkBack en dispositivos físicos.

**Firmas:** Grupo 5 (defiende): _Henry Lagua, Melany Cevallos, Alison Cobos, Carlos Ramos_ · Grupo retador G3: _Equipo Evaluador G3_
