# APE 5 · Fase 2 · Plan de trabajo en GitHub (Grupo 5)

**Repositorio:** https://github.com/Hlagua/APE5_IHC

Las 4 ramas ya existen en el repositorio local de Henry, con los commits a nombre de cada integrante. Los Issues se crean primero (quedan como #1 a #4) y los Pull Requests después (quedan como #5 a #8). Cada PR cierra su Issue con `Closes #N` al fusionarse.

| Rama | Integrante | Issue | PR | Revisor |
| :--- | :--- | :---: | :---: | :--- |
| `plan-clases` | Henry Daniel Lagua Flores (@Hlagua) | #1 | #5 | Melany (@SalyC15) |
| `prototipo-html` | Melany Saleth Cevallos Goyes (@SalyC15) | #2 | #6 | Alison (@Itsuna18) |
| `interfaz-responsive` | Alison Marcela Cobos Taco (@Itsuna18) | #3 | #7 | Carlos (@carlitosgiovanniramos) |
| `pruebas-informe` | Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) | #4 | #8 | Henry (@Hlagua) |

---

## 0. Preparación (solo Henry, una vez)

1. Agregar a los tres integrantes como colaboradores: GitHub → *Settings* → *Collaborators* → *Add people* (`Itsuna18`, `SalyC15`, `carlitosgiovanniramos`). Cada uno acepta la invitación desde su correo.
2. Subir las cuatro ramas (en PowerShell, dentro de la carpeta `APE5`):

```powershell
git checkout main
git push origin main
git push -u origin plan-clases prototipo-html interfaz-responsive pruebas-informe
```

> Si un integrante prefiere subir su rama desde su propio equipo, usa los comandos de la sección «Comandos» de su apartado.

---

## Integrante 1 · Henry Daniel Lagua Flores (@Hlagua) · `plan-clases`

### Issue #1 (texto exacto)

**Título:** `Fase 2 · Planificación, README y diapositivas de la defensa`

```markdown
## Objetivo
Coordinar la fase 2 del APE 5 (Grupo 5): planificación de la sesión de 120 min, README actualizado y diapositivas para la defensa ante G3.

## Tareas
- [ ] `docs/plan.md`: hipótesis, criterio de refutación, agenda, reparto de ramas y oradores.
- [ ] `docs/github.md`: textos de Issues, PRs y revisiones de los 4 integrantes.
- [ ] `README.md`: estructura del repositorio, cómo ejecutar el prototipo y entregables de la fase 2.
- [ ] `presentacion/index.html`: diapositivas navegables con teclado.
- [ ] `.gitignore`: excluir temporales y la carpeta de materiales `fase2/`.

## Criterio de aceptación
- La presentación se recorre con ← → y no tiene desborde horizontal a 360 px.
- El README enlaza `resultados/`, `evidencias/` y `docs/`.

Responsable: @Hlagua · Revisa: @SalyC15
```

### Comandos (si se trabaja desde cero)

```powershell
git checkout main; git pull
git checkout -b plan-clases
git add README.md .gitignore docs/plan.md docs/github.md presentacion/
git commit -m "docs(plan): planificación de la fase 2, README, plan de GitHub y diapositivas de defensa (#1)"
git push -u origin plan-clases
```

### Pull Request #5

**Título:** `docs(plan): planificación, README y diapositivas de la fase 2`

```markdown
Closes #1

## Qué incluye
- `docs/plan.md`: hipótesis falsable, agenda de 120 min, reparto de ramas sin conflictos y oradores.
- `docs/github.md`: textos de Issues, comandos, PRs y revisiones.
- `README.md` actualizado para la fase 2.
- `presentacion/index.html`: 10 diapositivas (← → para navegar, N para notas).

## Cómo revisar
Abrir `presentacion/index.html` a 360 px y a 1366 px en DevTools y recorrerla con el teclado.
```

**Revisor:** @SalyC15

### Texto de revisión que pega Melany al aprobar

```markdown
Revisé el PR #5 (plan-clases).
- `docs/plan.md`: la hipótesis tiene un criterio de refutación medible (scrollWidth > innerWidth) y la agenda cubre los 120 min.
- El reparto de archivos por rama no se superpone, así que no habrá conflictos al fusionar.
- `presentacion/index.html`: la recorrí con ← y →; a 360 px no hay scroll horizontal.
Aprobado ✅ — @SalyC15
```

---

## Integrante 2 · Melany Saleth Cevallos Goyes (@SalyC15) · `prototipo-html`

### Issue #2 (texto exacto)

**Título:** `Fase 2 · Boceto A de referencia y ficha de aplicación actualizada`

```markdown
## Objetivo
Dejar en el repositorio el boceto A (versión de escritorio de 960 px) como línea base, y completar la ficha de aplicación con los campos de la guía.

## Tareas
- [ ] `prototipos/prototipo-A.html`: boceto original sin modificar.
- [ ] `docs/proyecto.md`: diagnóstico del desborde a 360 px (+600 px) y de la escala 0,375 en emulación móvil.
- [ ] Ficha: Actor, Tarea principal, Dato clave, Acción principal, Resultado visible y Mecanismo para corregir o cancelar.
- [ ] Regla de interacción (sin duplicados) y criterio de aceptación medible.

## Criterio de aceptación
- La ficha tiene los 6 campos para el proyecto (Usability Test Dashboard) y para el caso de clase.
- El criterio de aceptación incluye un número verificable (por ejemplo, 0 duplicados en 5 de 5 intentos).

Responsable: @SalyC15 · Revisa: @Itsuna18
```

### Comandos (si se trabaja desde cero)

```powershell
git checkout main; git pull
git checkout -b prototipo-html
git add prototipos/prototipo-A.html docs/proyecto.md
git commit -m "docs(prototipo): boceto A de referencia y ficha de aplicación con resultado visible y mecanismo de corrección (#2)"
git push -u origin prototipo-html
```

### Pull Request #6

**Título:** `docs(prototipo): boceto A de referencia y ficha de aplicación completa`

```markdown
Closes #2

## Qué incluye
- `prototipos/prototipo-A.html`: boceto de 960 px usado como línea base en las mediciones.
- `docs/proyecto.md`: diagnóstico a 360 px (desborde de +600 px o, en emulación móvil, escala 0,375 con texto efectivo de 6,8 px).
- Ficha con los 6 campos de la guía y la regla de no duplicados con criterio medible.

## Cómo revisar
Abrir `prototipos/prototipo-A.html` a 360 px y ejecutar en consola `document.documentElement.scrollWidth` (debe dar 960).
```

**Revisor:** @Itsuna18

### Texto de revisión que pega Alison al aprobar

```markdown
Revisé el PR #6 (prototipo-html).
- Abrí `prototipos/prototipo-A.html` a 360 px: scrollWidth = 960, así que el diagnóstico de +600 px es reproducible.
- La ficha tiene los 6 campos y el «Mecanismo para corregir o cancelar» coincide con el botón «Cancelar mi reserva» del código.
- El criterio de aceptación es medible (0 duplicados en 5 de 5 intentos).
Aprobado ✅ — @Itsuna18
```

---

## Integrante 3 · Alison Marcela Cobos Taco (@Itsuna18) · `interfaz-responsive`

### Issue #3 (texto exacto)

**Título:** `Fase 2 · Controlador interaccion.js, CSS Mobile-First y respuestas de defensa`

```markdown
## Objetivo
Dejar la interfaz B lista para la defensa: controlador con el nombre que pide la guía, prevención de la doble pulsación y respuestas preparadas para G3.

## Tareas
- [ ] Renombrar `src/reserva.js` → `src/interaccion.js` y actualizar `src/index.html`.
- [ ] Corregir el hallazgo H-01: un doble Enter reservaba y cancelaba al instante (margen de 600 ms en «Cancelar»).
- [ ] `src/estilos.css`: respetar `prefers-reduced-motion`.
- [ ] `tests/test_runner.html`: adaptar TC-07 al margen de 600 ms, agregar TC-09 (doble Enter) y reiniciar `sessionStorage` antes de ejecutar.
- [ ] `docs/preguntas.md`: respuestas a la pregunta 1 (48rem y Tab), la pregunta 2 (disabled y foco) y la objeción (ajuste frente a comprensión), con espacio para el acta.

## Criterio de aceptación
- Tab → Enter → Enter deja la reserva confirmada (11 cupos) y el foco en «Cancelar».
- Enter sobre «Cancelar» después de 1 s cancela y devuelve el foco a «Reservar».
- 0 px de desborde a 320, 360, 768 y 1366 px.

Responsable: @Itsuna18 · Revisa: @carlitosgiovanniramos
```

### Comandos (si se trabaja desde cero)

```powershell
git checkout main; git pull
git checkout -b interfaz-responsive
git mv src/reserva.js src/interaccion.js
# editar src/index.html: <script src="interaccion.js" defer></script>
git add src/interaccion.js src/index.html src/estilos.css tests/test_runner.html docs/preguntas.md
git commit -m "feat(interaccion): controlador interaccion.js con prevención de doble pulsación, reduced-motion y respuestas de defensa (#3)"
git push -u origin interfaz-responsive
```

### Pull Request #7

**Título:** `feat(interaccion): interaccion.js, prevención de doble Enter y respuestas de defensa`

```markdown
Closes #3

## Qué incluye
- `src/reserva.js` → `src/interaccion.js` (nombre que pide la guía) y `src/index.html` actualizado.
- Corrección H-01: antes, Tab → Enter Enter terminaba en «cancelada» con 12 cupos; ahora termina en «confirmada» con 11. Se mantiene `btnCancelar.focus()`.
- `src/estilos.css`: `@media (prefers-reduced-motion: reduce)`.
- `tests/test_runner.html`: 9 de 9 pruebas aprobadas (nueva TC-09 para el doble Enter).
- `docs/preguntas.md`: respuestas preparadas y acta para completar durante la defensa con G3.

## Cómo revisar
DevTools a 360 px → Tab → Enter Enter → la reserva sigue confirmada. Esperar 1 s → Enter → se cancela y el foco vuelve a «Reservar un lugar».
```

**Revisor:** @carlitosgiovanniramos

### Texto de revisión que pega Carlos al aprobar

```markdown
Revisé el PR #7 (interfaz-responsive).
- Probé Tab → Enter Enter a 360 px: la reserva queda confirmada (11 cupos) y el foco en «Cancelar mi reserva». H-01 corregido.
- Enter sobre «Cancelar» después de 1 s: cancela, cupos 12, foco en «Reservar un lugar».
- La media query sigue en 48rem y no se usa `order`: el orden de Tab es igual al del DOM en 360 y 1366 px.
- `tests/test_runner.html` da 9 de 9 aprobadas.
- Las respuestas de `docs/preguntas.md` citan archivos y mediciones reales.
Aprobado ✅ — @carlitosgiovanniramos
```

---

## Integrante 4 · Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · `pruebas-informe`

### Issue #4 (texto exacto)

**Título:** `Fase 2 · Pruebas en 4 viewports, observación con usuarios, conclusiones e informe final`

```markdown
## Objetivo
Validar técnicamente la interfaz B, registrar la observación con compañeros y entregar el informe final UTA.

## Tareas
- [ ] `resultados/pruebas.md`: scrollWidth e innerWidth a 320, 360, 768 y 1366 px (versión B y boceto A), teclado y foco.
- [ ] `evidencias/`: capturas de cada viewport con la medición impresa.
- [ ] `resultados/checklist.md`: consigna neutral y tabla de observación (tiempo, errores, ayudas y dificultades).
- [ ] `docs/conclusiones.md`: requisito, decisión, dato observado, limitación y siguiente iteración.
- [ ] `06_documento/APE5_Fase2_Informe_Final.pdf`: informe UTA con capturas, mediciones y acta de defensa.

## Criterio de aceptación
- La versión B tiene 0 px de desborde en los 4 viewports.
- La tabla de observación tiene solo datos reales de la sesión.

Responsable: @carlitosgiovanniramos · Revisa: @Hlagua
```

### Comandos (si se trabaja desde cero)

```powershell
git checkout main; git pull
git checkout -b pruebas-informe
python -m http.server 8766          # en otra ventana, dentro de APE5
python _scripts/ape5_fase2_evidencias.py
python _scripts/ape5_fase2_build.py
git add evidencias/ resultados/ docs/conclusiones.md _scripts/ape5_fase2_evidencias.py _scripts/ape5_fase2_build.py 06_documento/APE5_Fase2_*
git commit -m "test(pruebas): validación en 4 viewports, observación en aula, conclusiones e informe final UTA (#4)"
git push -u origin pruebas-informe
```

### Pull Request #8

**Título:** `test(pruebas): validación responsiva, observación con usuarios e informe final`

```markdown
Closes #4

## Qué incluye
- `resultados/pruebas.md`: versión B con 0 px de desborde a 320, 360, 768 y 1366 px; boceto A con +640, +600 y +192 px.
- `evidencias/`: 10 capturas con scrollWidth e innerWidth impresos.
- `resultados/checklist.md`: protocolo de observación con consigna neutral.
- `docs/conclusiones.md` y el informe final UTA en `06_documento/`.

## Cómo revisar
Repetir una medición: DevTools a 320 × 720 → consola → `document.documentElement.scrollWidth` debe dar 320.
```

**Revisor:** @Hlagua

### Texto de revisión que pega Henry al aprobar

```markdown
Revisé el PR #8 (pruebas-informe).
- Repetí la medición a 320 × 720 y a 1366 × 768: scrollWidth = innerWidth en ambos casos, igual que en `resultados/pruebas.md`.
- Las capturas de `evidencias/` corresponden a los viewports de la tabla.
- `docs/conclusiones.md` distingue la evidencia técnica de la evidencia con personas y declara sus limitaciones.
- El informe final incluye capturas, mediciones y el acta de defensa.
Aprobado ✅ — @Hlagua
```

---

## Cierre (cualquier integrante con permisos)

Fusionar en este orden (no hay conflictos, pero así el historial queda legible): #5 → #6 → #7 → #8. Usar *Create a merge commit* para que cada rama quede visible en el historial de `main`.

```powershell
git checkout main; git pull
git log --oneline --graph -12
```
