# PRÁCTICA EXPERIMENTAL DE APRENDIZAJE – APE 5 · Grupo 5
## Diseño de interfaces web adaptables · Caso **CaféU** · Interacción Humano-Computador (IHC) · Quinto "A"
### Universidad Técnica de Ambato (UTA) · FISEI · Carrera de Ingeniería de Software

**Docente:** Ing. Mg. José Caiza · **Repositorio:** [https://github.com/Hlagua/APE5_IHC](https://github.com/Hlagua/APE5_IHC)

**Proyecto del grupo:** **CaféU**, la aplicación de pedidos de la cafetería universitaria que diseñamos y probamos en el APE 4 ([Hlagua/APE4_IHC](https://github.com/Hlagua/APE4_IHC)). En el APE 5 llevamos la pantalla **«Mi pedido → Confirmar y pagar»** del prototipo móvil a una **interfaz web real y adaptable** (HTML5 semántico, CSS Mobile-First con corte en 48rem e interacción accesible por teclado).

---

## Integrantes del Grupo 5

| N.º | Integrante | Usuario GitHub | Rol | Rama · Issue (ronda CaféU) |
|:---:|---|---|---|---|
| 1 | **Henry Daniel Lagua Flores** (coordinador) | [@Hlagua](https://github.com/Hlagua) | QA / Arquitecto | `plan-clases` · #9 |
| 2 | **Melany Saleth Cevallos Goyes** | [@SalyC15](https://github.com/SalyC15) | Desarrollador Front-End | `prototipo-html` · #10 |
| 3 | **Alison Marcela Cobos Taco** | [@Itsuna18](https://github.com/Itsuna18) | Desarrollador Back-End | `interfaz-responsive` · #11 |
| 4 | **Carlos Giovanni Ramos Jácome** | [@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos) | Tester | `pruebas-informe` · #12 |

> Los números de Issue son los esperados si se crean en este orden; ver [`docs/github.md`](docs/github.md).

---

## Del APE 4 al APE 5

| | APE 4 (Prototipado – Wireframes) | APE 5 (Diseño de interfaces web) |
|---|---|---|
| Qué se hizo con CaféU | Requisitos, sitemap, wireframes, prototipo navegable v1 → v3.1, prueba con usuarios | La pantalla «Mi pedido» como página web adaptable de 320 a 1366 px |
| Riesgo atendido | D1: temor a un doble cobro en el pago | Regla de **cobro único**: `disabled`, API idempotente y margen contra el doble Enter |
| Datos | Café Americano $1.50 + Sánduche $2.75 = **$4.25**, pedido **#A24**, retiro en el Edificio central en 10 min | Los mismos |

---

## Estructura del repositorio

| Ruta | Contenido |
|---|---|
| [`src/index.html`](src/index.html) | «Mi pedido» (versión B): `<header>`, `<main>`, `<article>` con `<dl>` (total, retiro, pago), `<section>` con `<p role="status">` y `<button>` nativos |
| [`src/estilos.css`](src/estilos.css) | Mobile-First: 1 columna base y 2 desde `@media (min-width: 48rem)`; paleta CaféU, botones de 44 px y `:focus-visible` |
| [`src/interaccion.js`](src/interaccion.js) | Pendiente → Confirmado → Cancelado, `disabled` contra el doble cobro, traslado del foco y margen de 600 ms (H-01) |
| [`src/api.js`](src/api.js) | `PedidoAPI` simulada: cobro único, devolución al cancelar y `sessionStorage` |
| [`prototipos/prototipo-A.html`](prototipos/prototipo-A.html) | Boceto A de «Mi pedido» (960 px fijos), línea base |
| [`docs/proyecto.md`](docs/proyecto.md) | Diagnóstico y ficha de aplicación |
| [`docs/preguntas.md`](docs/preguntas.md) | Respuestas preparadas y acta de la defensa ante G3 |
| [`docs/conclusiones.md`](docs/conclusiones.md) | Requisito, decisión, dato observado, limitación y siguiente iteración |
| [`docs/protocolo_pruebas.md`](docs/protocolo_pruebas.md) | Casos de prueba y cuestionario SUS |
| [`docs/plan.md`](docs/plan.md) · [`docs/github.md`](docs/github.md) | Planificación y plan de Issues, PRs y revisiones |
| [`resultados/pruebas.md`](resultados/pruebas.md) | Mediciones de `scrollWidth` frente a `innerWidth`, teclado, foco, H-01 y suite |
| [`resultados/checklist.md`](resultados/checklist.md) | Protocolo y tabla de observación con compañeros |
| [`evidencias/`](evidencias/) | Capturas de cada viewport con la medición impresa |
| [`presentacion/index.html`](presentacion/index.html) | Diapositivas de la defensa (← → para navegar, N para notas) |
| [`tests/test_runner.html`](tests/test_runner.html) | Suite automática (10 pruebas) |
| [`06_documento/`](06_documento/) | Documento corto de la fase 1 e informe final UTA |
| [`_scripts/`](_scripts/) | Generadores de capturas e informes |

---

## Resultados técnicos

| Viewport | Versión B · scrollWidth / innerWidth | Boceto A · desborde |
|---|---|---|
| 320 × 720 | 320 / 320 → **0 px** | +640 px |
| 360 × 800 | 360 / 360 → **0 px** | +600 px |
| 768 × 1024 | 768 / 768 → **0 px** | +192 px |
| 1366 × 768 | 1366 / 1366 → **0 px** | 0 px |

Suite automática: **10 de 10**. Detalle y método en [`resultados/pruebas.md`](resultados/pruebas.md).

---

## Cómo ejecutar

```bash
python -m http.server 8768
```

Abrir `http://localhost:8768/src/index.html` (pantalla), `http://localhost:8768/prototipos/prototipo-A.html` (boceto A), `http://localhost:8768/tests/test_runner.html` (pruebas) o `http://localhost:8768/presentacion/` (diapositivas).

> Entre un participante y otro, abrir una pestaña nueva o ejecutar `PedidoAPI.reiniciar()` en la consola: el pedido se guarda en `sessionStorage`.

Con el servidor encendido, regenerar capturas y documentos:

```bash
python _scripts/ape5_fase2_evidencias.py
```

```bash
python _scripts/ape5_fase1_entrega.py
```

```bash
python _scripts/ape5_fase2_build.py
```

> Los generadores de documentos usan la plantilla UTA y `docx_lib.py` del APE 4, en el equipo de Henry.
