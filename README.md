# PRÁCTICA EXPERIMENTAL DE APRENDIZAJE – APE 5 · Grupo 5
## Diseño de interfaces web adaptables · Interacción Humano-Computador (IHC) · Quinto "A"
### Universidad Técnica de Ambato (UTA) · FISEI · Carrera de Ingeniería de Software

**Docente:** Ing. Mg. José Caiza · **Repositorio:** [https://github.com/Hlagua/APE5_IHC](https://github.com/Hlagua/APE5_IHC)

---

## Integrantes del Grupo 5

| N.º | Integrante | Usuario GitHub | Rol en el proyecto | Rama fase 2 · Issue |
|:---:|---|---|---|---|
| 1 | **Henry Daniel Lagua Flores** (coordinador) | [@Hlagua](https://github.com/Hlagua) | QA / Arquitecto | `plan-clases` · #1 |
| 2 | **Melany Saleth Cevallos Goyes** | [@SalyC15](https://github.com/SalyC15) | Desarrollador Front-End | `prototipo-html` · #2 |
| 3 | **Alison Marcela Cobos Taco** | [@Itsuna18](https://github.com/Itsuna18) | Desarrollador Back-End | `interfaz-responsive` · #3 |
| 4 | **Carlos Giovanni Ramos Jácome** | [@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos) | Tester | `pruebas-informe` · #4 |

---

## Fases de la práctica

| Fase | Contenido | Estado |
|---|---|---|
| **Fase 1** · Del boceto a la interfaz web adaptable | Diagnóstico del boceto A a 360 px, ficha de aplicación, HTML5 semántico, CSS Mobile-First (48rem) e interacción accesible por teclado. Entrega: [`APE5_Fase1/`](APE5_Fase1/README.md) y [`06_documento/`](06_documento/) | Entregada |
| **Fase 2** · Validación técnica, pruebas con usuarios y defensa | Mediciones en 320/360/768/1366 px, observación en aula, defensa cruzada ante G3, 4 PRs revisados e informe final UTA | En curso |

---

## Estructura del repositorio

| Ruta | Contenido |
|---|---|
| [`src/index.html`](src/index.html) | Pantalla «Elige tu taller» (versión B): `<header>`, `<main>`, `<article>`, `<dl>`, `<section>`, `<button>` y `<p role="status">` |
| [`src/estilos.css`](src/estilos.css) | Mobile-First: 1 columna base y 2 columnas desde `@media (min-width: 48rem)`; botones de 44 px y `:focus-visible` |
| [`src/interaccion.js`](src/interaccion.js) | Disponible → Confirmada → Cancelada, `disabled` contra duplicados, traslado del foco y margen contra doble Enter |
| [`src/api.js`](src/api.js) | API simulada: validación de cupos y persistencia en `sessionStorage` |
| [`prototipos/prototipo-A.html`](prototipos/prototipo-A.html) | Boceto A original (960 px fijos), línea base de comparación |
| [`docs/proyecto.md`](docs/proyecto.md) | Diagnóstico y ficha de aplicación |
| [`docs/preguntas.md`](docs/preguntas.md) | Respuestas preparadas y acta de la defensa cruzada ante G3 |
| [`docs/conclusiones.md`](docs/conclusiones.md) | Requisito, decisión, dato observado, limitación y siguiente iteración |
| [`docs/plan.md`](docs/plan.md) · [`docs/github.md`](docs/github.md) | Planificación de la sesión y plan de Issues, PRs y revisiones |
| [`resultados/pruebas.md`](resultados/pruebas.md) | Mediciones de `scrollWidth` frente a `innerWidth`, teclado, foco y hallazgo H-01 |
| [`resultados/checklist.md`](resultados/checklist.md) | Protocolo y tabla de observación con compañeros |
| [`evidencias/`](evidencias/) | Capturas de cada viewport con la medición impresa |
| [`presentacion/index.html`](presentacion/index.html) | Diapositivas de la defensa (← → para navegar, N para notas) |
| [`06_documento/`](06_documento/) | Informes UTA (fase 1 y fase 2) |
| [`_scripts/`](_scripts/) | Generadores de capturas e informes |
| [`tests/test_runner.html`](tests/test_runner.html) | Pruebas automáticas en el navegador |

---

## Resultados técnicos de la fase 2

| Viewport | Versión B · scrollWidth / innerWidth | Boceto A · desborde |
|---|---|---|
| 320 × 720 | 320 / 320 → **0 px** | +640 px |
| 360 × 800 | 360 / 360 → **0 px** | +600 px |
| 768 × 1024 | 768 / 768 → **0 px** | +192 px |
| 1366 × 768 | 1366 / 1366 → **0 px** | 0 px |

Detalle y método en [`resultados/pruebas.md`](resultados/pruebas.md).

---

## Cómo ejecutar

```bash
python -m http.server 8766
```

Abrir `http://localhost:8766/src/index.html` (prototipo), `http://localhost:8766/prototipos/prototipo-A.html` (boceto A) o `http://localhost:8766/presentacion/` (diapositivas).

> Entre un participante y otro, abrir una pestaña nueva o ejecutar `ReservaAPI.reiniciar()` en la consola: la reserva se guarda en `sessionStorage`.

Para regenerar las capturas y el informe (con el servidor encendido):

```bash
python _scripts/ape5_fase2_evidencias.py
```

```bash
python _scripts/ape5_fase2_build.py
```
