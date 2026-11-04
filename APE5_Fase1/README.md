# PRÁCTICA EXPERIMENTAL DE APRENDIZAJE – APE 5 · Fase 1
## Del boceto a la interfaz web adaptable (HTML5, CSS Mobile-First e Interacción)

- **Institución:** Universidad Técnica de Ambato (UTA) · FISEI · Carrera de Ingeniería de Software
- **Asignatura:** Interacción Humano-Computador (IHC) · Quinto Semestre "A" · Periodo Académico 2026
- **Docente:** Ing. Mg. José Caiza
- **Repositorio oficial:** [https://github.com/Hlagua/APE5_IHC](https://github.com/Hlagua/APE5_IHC)

---

### Integrantes del equipo y asignación de roles

| N.º | Integrante | Usuario GitHub | Correo Electrónico | Rol Oficial en el Proyecto |
|:---:|---|---|---|---|
| **1** | **Alison Marcela Cobos Taco** | [@Itsuna18](https://github.com/Itsuna18) | `tacomarcelab@gmail.com` | **Desarrollador Back-End** (API, modelos, persistencia, endpoints) |
| **2** | **Melany Saleth Cevallos Goyes** | [@SalyC15](https://github.com/SalyC15) | `mcevallos8901@uta.edu.ec` | **Desarrollador Front-End** (Vistas, componentes UI, diseño, wizard) |
| **3** | **Carlos Giovanni Ramos Jácome** | [@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos) | `carlos.giovanni.ramos.work@gmail.com` | **Tester** (Protocolos de validación, casos de prueba, métricas SUS) |
| **4** | **Henry Daniel Lagua Flores** | [@Hlagua](https://github.com/Hlagua) | `hlagua6116@uta.edu.ec` | **QA / Arquitecto** (Auditorías, motor IA, resiliencia, suite de tests) |

---

### Reto de diseño e interacción (Fase 1)
> *Una estudiante desea reservar un taller desde su teléfono móvil: ¿dónde busca el horario y cómo descubre que ya tiene un lugar confirmado?*

En el **Boceto A inicial** (`prototipo-A.html`), la página tenía un contenedor estático de `width: 960px` y columnas de `580px 360px`. Al visualizarse en un móvil a **360 px**, provocaba **600 px de desborde horizontal** (`scrollWidth = 960px`), ocultando completamente el panel de estado **«Mi reserva»** y los controles de confirmación. Además, el botón venía deshabilitado por defecto, no existía región accesible para lectores de pantalla (`role="status"`) y no se permitía cancelar o deshacer la acción.

---

### Estructura de la solución y entregables

| Ruta / Archivo | Rol Responsable | Contenido y Función |
|---|---|---|
| [`docs/proyecto.md`](docs/proyecto.md) | QA & Tester | Ficha técnica: diagnóstico 360 px, ruta Actor → Tarea → Dato decisivo → Acción → Estado, regla de negocio y criterios medibles |
| [`docs/protocolo_pruebas.md`](docs/protocolo_pruebas.md) | Tester | Protocolo de validación responsiva, casos de prueba TC-01 a TC-10 y métricas SUS (Puntaje piloto 92.5/100) |
| [`src/index.html`](src/index.html) | Front-End | Estructura semántica HTML5: `<header>`, `<main>`, `<article>` (tarjeta), `<dl>` (horario/lugar/cupos), `<section>` (resumen), `<button>` y `<p role="status">` |
| [`src/estilos.css`](src/estilos.css) | Front-End | Diseño Mobile-First: 1 columna base por defecto; 2 columnas fluidas (`3fr 2fr`) a partir de `@media (min-width: 48rem)` (768 px) |
| [`src/api.js`](src/api.js) | Back-End | Capa de servicios REST simulada, modelo de taller, reglas de concurrencia de cupos e idempotencia con persistencia |
| [`src/reserva.js`](src/reserva.js) | Front-End | Controlador de interacción: ciclo Disponible → Confirmada → Cancelada, bloqueo de doble clic y gestión accesible del foco |
| [`tests/test_runner.html`](tests/test_runner.html) | Tester | Suite interactiva de pruebas unitarias y de integración en navegador con emulación móvil a 360 px |
| [`04_capturas/`](04_capturas/) | Tester | Evidencias visuales a 360 px (boceto vs prototipo), 768 px y 1366 px en todos los estados |
| [`06_documento/`](06_documento/) | QA / Arquitecto | Documento corto para Moodle (`APE5_Fase1_Entrega.docx` / `.pdf`) e informe formal UTA (`APE5_Fase1_AulaAbierta.docx` / `.pdf`) |

---

### Cumplimiento de Principios HCI

1. **Jerarquía:** El dato decisivo (horario y lugar en la lista `<dl>`) se presenta antes del botón principal «Reservar un lugar», permitiendo decisiones informadas.
2. **Visibilidad del estado del sistema (H1):** La región viva accesible `<p role="status" aria-live="polite">` notifica a tecnologías asistivas, mientras que la sección resumen muta visualmente mediante `data-estado` (verde suave para éxito, ámbar para cancelación).
3. **Control y libertad del usuario (H3):** El botón «Cancelar mi reserva» permite revertir la acción de manera inmediata, restituyendo el cupo ($11 \rightarrow 12$) y transfiriendo el foco al botón de reserva.

---

### Matriz de Verificación Técnica

| Entorno / Resolución | Comportamiento Esperado | Resultado de Validación |
|---|---|:---:|
| **Móvil 360 px** | Cuadrícula de 1 columna vertical; `scrollWidth = 360px` (sin desborde horizontal) | **CUMPLE (100 %)** |
| **Tablet 767 px** | Se preserva 1 columna antes del punto de corte estricto de 48rem | **CUMPLE (100 %)** |
| **Tablet/Escritorio 768 px** | Conmuta fluidamente a 2 columnas (`3fr 2fr`), respetando el orden del DOM | **CUMPLE (100 %)** |
| **Escritorio 1366 px** | Contenedor fluido centrado (`max-width: 60rem`); botones ergonómicos | **CUMPLE (100 %)** |
| **Flujo Reservar** | Estado «confirmada», cupos $12 \rightarrow 11$, botón bloqueado (`disabled`) y foco trasladado a cancelar | **CUMPLE (100 %)** |
| **Flujo Cancelar** | Estado «cancelada», cupos $11 \rightarrow 12$, botón cancelar oculto y foco devuelto a reservar | **CUMPLE (100 %)** |

---

### Instrucciones de Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Hlagua/APE5_IHC.git
   cd APE5_IHC
   ```
2. Abrir directamente en el navegador:
   - Pantalla principal: `src/index.html` o `APE5_Fase1/src/index.html`
   - Suite de pruebas: `APE5_Fase1/tests/test_runner.html`
3. O mediante un servidor HTTP local de desarrollo:
   ```bash
   python -m http.server 8765 --directory src
   ```
   Luego ingresar en el navegador a `http://localhost:8765`.
