# APE 5 · Plan de trabajo en GitHub · Ronda CaféU (Grupo 5)

**Repositorio:** https://github.com/Hlagua/APE5_IHC

La primera ronda (Issues #1 a #4 y PRs #5 a #8) integró la versión de clase «Aula Abierta». Esta segunda ronda **rehace el APE 5 sobre CaféU**, el proyecto del grupo desde el APE 4. Se usan las mismas cuatro ramas de la guía, ahora con commits nuevos sobre `main`.

Si no se crea nada más en el repositorio entre medio, los Issues nuevos quedarán como **#9 a #12** y los PRs como **#13 a #16**. Antes de pegar los textos, comprueben los números que les asigna GitHub.

| Rama | Integrante | Issue | PR | Revisa (desde su cuenta) |
| :--- | :--- | :---: | :---: | :--- |
| `plan-clases` | Henry Daniel Lagua Flores (@Hlagua) | #9 | #13 | Melany (@SalyC15) |
| `prototipo-html` | Melany Saleth Cevallos Goyes (@SalyC15) | #10 | #14 | Alison (@Itsuna18) |
| `interfaz-responsive` | Alison Marcela Cobos Taco (@Itsuna18) | #11 | #15 | Carlos (@carlitosgiovanniramos) |
| `pruebas-informe` | Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) | #12 | #16 | Henry (@Hlagua) |

> **Importante:** en la primera ronda los 4 PRs solo tenían revisión del bot de Copilot. La guía pide **revisión cruzada entre integrantes**: cada revisor entra con **su propia cuenta** → *Files changed* → *Review changes* → **Approve**, y pega el texto de su sección. El PR se fusiona solo después de esa aprobación.

---

## 0. Preparación (Henry, una vez)

1. *Settings* → *Collaborators* → *Add people*: `SalyC15`, `Itsuna18`, `carlitosgiovanniramos`. Cada uno acepta la invitación desde su correo.
2. Subir las ramas (PowerShell, dentro de `APE5`), cuando el grupo lo decida:

```powershell
git push origin plan-clases prototipo-html interfaz-responsive pruebas-informe --force-with-lease
```

> Se usa `--force-with-lease` porque estas ramas ya existían en GitHub con el contenido de la primera ronda (ya fusionada en `main`).

---

## Integrante 1 · Henry (@Hlagua) · `plan-clases`

**Issue — título:** `APE 5 CaféU · Planificación, README y diapositivas`

```markdown
## Objetivo
Reorientar el APE 5 al proyecto del grupo, CaféU (APE 4): planificación, README y diapositivas de la defensa.

## Tareas
- [ ] `docs/plan.md`: hipótesis de CaféU, criterio de refutación, agenda y reparto de ramas.
- [ ] `docs/github.md`: textos de Issues, PRs y revisiones de la ronda CaféU.
- [ ] `README.md`: CaféU como proyecto, estructura y cómo ejecutar.
- [ ] `presentacion/index.html`: diapositivas de CaféU navegables con teclado.

## Criterio de aceptación
- Ningún documento presenta otro proyecto como el del grupo.
- La presentación no desborda a 360 px.

Responsable: @Hlagua · Revisa: @SalyC15
```

**PR — título:** `docs(plan): APE 5 sobre CaféU — planificación, README y diapositivas` · **Descripción:** `Closes #9` + lista de archivos anteriores.

**Revisión de Melany (Approve):**
```markdown
Revisé el PR (plan-clases). La hipótesis de `docs/plan.md` es de CaféU («dice su número de pedido y si pagó») y tiene un criterio de refutación medible. Recorrí `presentacion/index.html` con ← y → a 360 px: sin scroll horizontal. Aprobado ✅ — @SalyC15
```

---

## Integrante 2 · Melany (@SalyC15) · `prototipo-html`

**Issue — título:** `APE 5 CaféU · Boceto A de «Mi pedido» y ficha de aplicación`

```markdown
## Objetivo
Crear el boceto A de escritorio (960 px) de la pantalla «Mi pedido» de CaféU y la ficha de aplicación.

## Tareas
- [ ] `prototipos/prototipo-A.html`: «Mi pedido» con ancho fijo de 960 px y estado en la columna derecha.
- [ ] `docs/proyecto.md`: diagnóstico (+600 px a 360 px; escala 0,375 en emulación móvil), ficha con los 6 campos, requisito RF-PED-01 y regla de cobro único con criterio medible.

## Criterio de aceptación
- `document.documentElement.scrollWidth` del boceto A a 360 px = 960.
- La ficha usa los datos del APE 4 (total $4.25, #A24, Edificio central, 10 min).

Responsable: @SalyC15 · Revisa: @Itsuna18
```

**PR — título:** `docs(prototipo): boceto A de «Mi pedido» y ficha de aplicación de CaféU` · **Descripción:** `Closes #10`.

**Revisión de Alison (Approve):**
```markdown
Revisé el PR (prototipo-html). Abrí `prototipos/prototipo-A.html` a 360 px: scrollWidth = 960 y el panel de estado empieza en x = 600. La ficha tiene los 6 campos con los datos de CaféU del APE 4, y la regla de cobro único coincide con `PedidoAPI.confirmarPedido()`. Aprobado ✅ — @Itsuna18
```

---

## Integrante 3 · Alison (@Itsuna18) · `interfaz-responsive`

**Issue — título:** `APE 5 CaféU · «Mi pedido» adaptable, cobro único y defensa`

```markdown
## Objetivo
Construir la versión B de «Mi pedido» de CaféU: HTML5 semántico, CSS Mobile-First (48rem) e interacción con cobro único, y preparar la defensa.

## Tareas
- [ ] `src/index.html`: header, main, article con <dl> (total, retiro, pago), section con <p role="status">.
- [ ] `src/estilos.css`: 1 columna base, 2 desde 48rem, botones de 44 px, :focus-visible, paleta CaféU.
- [ ] `src/api.js`: PedidoAPI (confirmarPedido, cancelarPedido, reiniciar) sin doble cobro.
- [ ] `src/interaccion.js`: pendiente → confirmado → cancelado, disabled, .focus() y margen de 600 ms (H-01).
- [ ] `tests/test_runner.html`: 10 pruebas.
- [ ] `docs/preguntas.md`: respuestas preparadas y acta para la defensa ante G3.

## Criterio de aceptación
- Tab → Enter Enter: pedido #A24 pagado, saldo $5.75, foco en «Cancelar pedido».
- Cancelar 1 s después: saldo $10.00, foco en «Confirmar y pagar».
- Suite: 10 de 10.

Responsable: @Itsuna18 · Revisa: @carlitosgiovanniramos
```

**PR — título:** `feat(cafeu): «Mi pedido» adaptable con cobro único, foco accesible y respuestas de defensa` · **Descripción:** `Closes #11`.

**Revisión de Carlos (Approve):**
```markdown
Revisé el PR (interfaz-responsive). Tab → Enter Enter a 360 px: pedido #A24 pagado, saldo $5.75 y foco en «Cancelar pedido»; un segundo cobro no ocurre. Cancelar después de 1 s devuelve $4.25 y el foco vuelve a «Confirmar y pagar». `tests/test_runner.html`: 10 de 10. La media query está en 48rem y no se usa `order`. Aprobado ✅ — @carlitosgiovanniramos
```

---

## Integrante 4 · Carlos (@carlitosgiovanniramos) · `pruebas-informe`

**Issue — título:** `APE 5 CaféU · Pruebas en 4 viewports, observación, conclusiones e informe`

```markdown
## Objetivo
Validar técnicamente «Mi pedido» de CaféU, registrar la observación con compañeros y entregar el informe final UTA.

## Tareas
- [ ] `resultados/pruebas.md` y `evidencias/`: scrollWidth/innerWidth en 320, 360, 768 y 1366 px (B y boceto A), teclado, H-01 y suite.
- [ ] `resultados/checklist.md`: consigna neutral y tabla de observación **con datos reales**.
- [ ] `docs/protocolo_pruebas.md` y `docs/conclusiones.md`.
- [ ] `06_documento/APE5_Fase2_Informe_Final.pdf` y documento corto de la fase 1 de CaféU.

## Criterio de aceptación
- La versión B tiene 0 px de desborde en los 4 viewports.
- La tabla de observación solo contiene datos de la sesión.

Responsable: @carlitosgiovanniramos · Revisa: @Hlagua
```

**PR — título:** `test(cafeu): validación en 4 viewports, observación, conclusiones e informe final` · **Descripción:** `Closes #12`.

**Revisión de Henry (Approve):**
```markdown
Revisé el PR (pruebas-informe). Repetí la medición a 320 × 720 y 1366 × 768: scrollWidth = innerWidth, como en `resultados/pruebas.md`. Las capturas de `evidencias/` coinciden con la tabla. La observación y las conclusiones distinguen la evidencia técnica de la evidencia con personas. Aprobado ✅ — @Hlagua
```

---

## Cierre

Fusionar en orden #13 → #14 → #15 → #16 con *Create a merge commit*, **solo después de la aprobación del revisor**. Luego:

```powershell
git checkout main; git pull
git log --oneline --graph -12
```
