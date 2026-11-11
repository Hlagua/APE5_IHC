# APE 5 · Planificación del Grupo 5 · CaféU

- **Proyecto:** CaféU (APE 4) · pantalla «Mi pedido → Confirmar y pagar»
- **Coordinador:** Henry Daniel Lagua Flores (@Hlagua) · rama `plan-clases` · Issue #9
- **Revisión cruzada:** Melany Saleth Cevallos Goyes (@SalyC15)
- **Sesión:** ___/___/2026 · 120 minutos · Grupo retador QA/UX: **G3**

## 1. Hipótesis que se defiende

> En un viewport móvil de 360 px, un estudiante que no conoce la pantalla confirma su pedido de CaféU y **dice su número de pedido y si ya pagó, sin desplazarse horizontalmente y sin pedir ayuda**.

**Qué la refutaría:**
- *Técnico:* `document.documentElement.scrollWidth > innerWidth` en cualquiera de los anchos 320, 360, 768 o 1366 px.
- *Con personas:* menos de 4 de 5 participantes dicen su número de pedido y si pagaron sin buscarlo, o alguno necesita ayuda para encontrar el total o el estado.

## 2. Agenda de la sesión (120 min)

| Tiempo | Actividad | Responsable | Producto |
| :--- | :--- | :--- | :--- |
| 0–10 min | Apertura: hipótesis y criterio de refutación | Henry | Diapositivas 1–2 |
| 10–30 min | Pruebas técnicas en DevTools (4 viewports) y capturas | Carlos | `resultados/pruebas.md`, `evidencias/` |
| 30–60 min | Observación con compañeros de otro grupo (consigna neutral) | Carlos (registro) · Melany (moderación) | `resultados/checklist.md` |
| 60–90 min | Defensa cruzada ante G3: 2 preguntas técnicas y 1 objeción | Alison (acta) · los cuatro responden | `docs/preguntas.md` |
| 90–105 min | Integración en GitHub: 4 Issues, 4 PRs y revisión cruzada | Los cuatro | Ramas fusionadas en `main` |
| 105–120 min | Conclusiones, informe final y entrega en Moodle | Carlos (informe) · Henry (entrega) | `docs/conclusiones.md`, informe PDF |

## 3. Reparto de trabajo sin conflictos

Cada rama toca archivos distintos, así que los 4 Pull Requests pueden fusionarse en cualquier orden sin conflictos.

| N.º | Integrante | Rama | Issue | Archivos | Revisa su PR |
| :---: | :--- | :--- | :---: | :--- | :--- |
| 1 | Henry Daniel Lagua Flores (@Hlagua) — coordinador | `plan-clases` | #9 | `README.md`, `.gitignore`, `docs/plan.md`, `docs/github.md`, `presentacion/` | Melany |
| 2 | Melany Saleth Cevallos Goyes (@SalyC15) | `prototipo-html` | #10 | `prototipos/prototipo-A.html`, `docs/proyecto.md` | Alison |
| 3 | Alison Marcela Cobos Taco (@Itsuna18) | `interfaz-responsive` | #11 | `src/index.html`, `src/estilos.css`, `src/api.js`, `src/interaccion.js`, `tests/test_runner.html`, `docs/preguntas.md` | Carlos |
| 4 | Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) | `pruebas-informe` | #12 | `evidencias/`, `resultados/`, `docs/conclusiones.md`, `docs/protocolo_pruebas.md`, `_scripts/`, `06_documento/` | Henry |

## 4. Oradores de la presentación (`presentacion/index.html`)

| Diapositiva | Tema | Orador |
| :---: | :--- | :--- |
| 1–2 | Hipótesis y criterio de refutación | Henry |
| 3 | Diagnóstico del boceto A de «Mi pedido» (desborde y escala 0,375) | Melany |
| 4–5 | HTML5 semántico, CSS Mobile-First y 48rem | Melany y Alison |
| 6 | Interacción: cobro único, foco y hallazgo H-01 | Alison |
| 7 | Pruebas técnicas en 4 viewports | Carlos |
| 8 | Observación con usuarios | Carlos |
| 9 | Defensa ante G3 y trazabilidad en GitHub | Los cuatro |
| 10 | Conclusiones | Henry |

## 5. Lista de control antes de entregar

- [ ] `resultados/checklist.md` con los datos reales de la observación (sin filas vacías).
- [ ] `docs/preguntas.md` con lo que realmente preguntó G3, quién respondió y la valoración.
- [ ] `docs/conclusiones.md` y el informe con el «dato observado con personas».
- [ ] 4 Issues cerrados y 4 PRs **aprobados por el revisor desde su propia cuenta** y fusionados en `main` (ver `docs/github.md`).
- [ ] Informe UTA en PDF firmado por los cuatro integrantes, subido en «Archivos enviados».
- [ ] Enlace del repositorio en «Texto en línea».
