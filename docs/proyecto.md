# APE 5 · Fase 1 · Del boceto a la interfaz web adaptable
## Ficha de aplicación al proyecto y diagnóstico de interacción

- **Institución:** Universidad Técnica de Ambato (UTA) · FISEI · Ingeniería de Software
- **Asignatura:** Interacción Humano-Computador · Quinto Semestre "A"
- **Docente:** Ing. Mg. José Caiza
- **Proyecto del equipo:** Usability Test Dashboard 2.0 (UTA · IHC)
- **Pantalla elegida del proyecto:** Bitácora de observaciones — ruta `/dashboard/test-plan/record` (`src/presentation/pages/ObservationRecordPage.tsx`)
- **Pantalla adaptada en clase:** Boceto A «Elige tu taller» (Caso Aula Abierta) → `src/`

---

### Integrantes y asignación de roles

| Integrante | Usuario GitHub | Correo institucional / contacto | Rol oficial en el proyecto |
|---|---|---|---|
| **Alison Marcela Cobos Taco** | [@Itsuna18](https://github.com/Itsuna18) | `tacomarcelab@gmail.com` | **Desarrollador Back-End** (API, modelos, persistencia, endpoints) |
| **Melany Saleth Cevallos Goyes** | [@SalyC15](https://github.com/SalyC15) | `mcevallos8901@uta.edu.ec` | **Desarrollador Front-End** (Vistas, componentes UI, diseño, wizard) |
| **Carlos Giovanni Ramos Jácome** | [@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos) | `carlos.giovanni.ramos.work@gmail.com` | **Tester** (Protocolos de validación, casos de prueba, métricas SUS) |
| **Henry Daniel Lagua Flores** | [@Hlagua](https://github.com/Hlagua) | `hlagua6116@uta.edu.ec` | **QA / Arquitecto** (Auditorías, motor IA, resiliencia, suite de tests) |

---

## 1. Diagnóstico del Boceto A (360 px)

Al abrir el **Boceto A inicial** (`prototipo-A.html`) en un viewport móvil estrecho de **360 px de ancho** (representativo de dispositivos móviles estándar como Galaxy A o iPhone SE), se diagnosticaron las siguientes fallas críticas de diseño e interacción:

1. **Desbordamiento horizontal severo (Overflow):**
   - El boceto original utilizaba un contenedor rígido de escritorio `body { width: 960px; }` con una cuadrícula fija de `grid-template-columns: 580px 360px;`.
   - Al renderizarse en un viewport de 360 px, el ancho total renderizado (`scrollWidth`) es de 960 px, generando **600 px de desborde horizontal** (`scrollWidth - clientWidth = 600px`).
2. **Pérdida visual de información y del panel de estado:**
   - La columna derecha que aloja el panel de estado **«Mi reserva»** (`<section class="resumen">`) y los controles de interacción quedan completamente ocultos fuera del área visible de la pantalla (a partir de $x > 580\text{ px}$).
   - La persona usuaria que interactúa desde un teléfono móvil **no puede ver su reserva ni confirmar si su acción tuvo efecto**, a menos que realice un paneo horizontal manual forzado.
3. **Violación de principios HCI y estándares de accesibilidad:**
   - **Heurística de Nielsen H1 (Visibilidad del estado del sistema):** El sistema oculta la confirmación y la retroalimentación inmediata de la acción.
   - **WCAG 2.1 Criterio de Éxito 1.4.10 (Reajuste / Reflow - Nivel AA):** El contenido debe presentarse sin pérdida de información ni funcionalidad y sin requerir desplazamiento bidimensional (horizontal y vertical).
   - **Control de usuario ausente:** El botón principal venía bloqueado (`disabled`) en el código base, no existía canal de comunicación para lectores de pantalla (`role="status"` ausente) y no se ofrecía la posibilidad de deshacer (cancelar) la reserva.

---

## 2. Ficha de aplicación al proyecto

Se completó la secuencia formal **Actor → Tarea → Dato decisivo → Acción principal → Estado final** tanto para la pantalla del proyecto grupal como para el caso trabajado en clase:

### Secuencia de la tarea

| Actor | Tarea | Dato decisivo | Acción principal | Estado final |
| :--- | :--- | :--- | :--- | :--- |
| **Moderador/a de la prueba** *(Proyecto: Usability Test Dashboard)* | Registrar el desempeño de un participante en una tarea específica (T1…Tn) | Éxito (Sí/No), tiempo transcurrido en segundos ($t \ge 1\text{ s}$) y número de errores ($e \ge 0$) | Pulsar el botón **«Agregar al backlog»** | Hallazgo registrado en el Product Backlog y confirmado mediante alerta accesible en `<p role="status">` |
| **Estudiante** *(Caso de clase: Aula Abierta)* | Reservar un taller extracurricular | Horario del taller, laboratorio/lugar y cupos disponibles ($c > 0$) | Pulsar el botón **«Reservar un lugar»** | Estado «Reserva confirmada» visible de inmediato en «Mi reserva», cupo decrementado en 1 y botón de cancelar habilitado |

### Requisitos

- **RF-OBS-01 (Proyecto):** El moderador debe registrar por cada participante y tarea el éxito, tiempo y errores observados, enviando el hallazgo al backlog con confirmación inequívoca del estado del envío.
- **RF-RES-01 (Aula Abierta):** El estudiante debe consultar el horario y lugar del taller, confirmar su reserva descontando 1 cupo, y disponer de la opción de cancelar la reserva restituyendo dicho cupo.

---

## 3. Reglas de negocio y criterios de aceptación medibles

### A. Pantalla del proyecto (Usability Test Dashboard 2.0)
- **Regla de negocio:** Las métricas de observación no pueden contener datos anómalos o negativos. El campo **número de errores** no puede ser negativo ($e \ge 0$) y el **tiempo transcurrido** debe ser de al menos 1 segundo ($t \ge 1$). Si el usuario ingresa valores fuera de rango, el controlador (`handleObsChange`) auto-corrige automáticamente: valores negativos de errores se normalizan a `0`, y tiempos menores a 1 se normalizan a `1`. El campo «Errores» es obligatorio.
- **Criterio de aceptación (Medible en formato Gherkin):**
  - *Dado* que el moderador ingresa `-3` en el campo «Errores», *cuando* desenfoca el campo (evento blur o submit), *entonces* el valor queda establecido automáticamente en `0`. **Tasa de cumplimiento exigida: 5 de 5 intentos (100 %)**.
  - *Dado* que se ingresa `0` en el campo «Tiempo (s)», *cuando* se valida el formulario, *entonces* el valor se ajusta a `1`. **Tasa de cumplimiento exigida: 5 de 5 intentos (100 %)**.
  - En la base de datos y backlog se registran **exactamente 0 observaciones** con errores negativos o tiempo menor a 1 segundo.

### B. Pantalla adaptada en clase (Aula Abierta)
- **Regla de negocio:** Una persona estudiante sólo puede reservar un cupo a la vez (idempotencia y unicidad). Al confirmarse la reserva, el botón «Reservar un lugar» queda deshabilitado (`disabled = true`) impidiendo transacciones duplicadas. El cupo se decrementa en exactamente 1 unidad. Al cancelar, el cupo se restituye en exactamente 1 unidad y el botón de reservar vuelve a quedar activo.
- **Criterio de aceptación (Medible):**
  - *Dado* un taller con 12 cupos disponibles, *cuando* el usuario hace clic en «Reservar un lugar», *entonces* los cupos bajan a 11, el estado cambia a «confirmada», el botón de reservar queda `disabled` y presionar Enter repetidas veces genera **0 reservas duplicadas adicionales**.
  - *Dado* el estado confirmado, *cuando* el usuario presiona «Cancelar mi reserva», *entonces* los cupos vuelven a 12, el botón de cancelar se oculta y el foco vuelve automáticamente al botón de reserva.

---

## 4. Estructura HTML5 semántica (`src/index.html`)

La arquitectura del documento web se implementó sin dependencias externas, asegurando jerarquía y accesibilidad nativa:
- `<header class="cabecera">`: Identidad institucional («Aula Abierta»), fuera del flujo de la tarea principal.
- `<main class="contenido">`: Contenedor principal de la tarea con título de primer nivel `<h1>Elige tu taller</h1>`.
- `<article class="tarjeta" aria-labelledby="titulo-taller">`: Unidad autónoma que agrupa los datos decisivos y la acción principal.
- `<dl class="datos">`: Lista de definición con pares `<dt>` (Horario, Lugar, Cupos) y `<dd>`, garantizando que el usuario conozca las condiciones antes del llamado a la acción.
- `<button type="button" id="btn-reservar">`: Control nativo interactivo con atributo semántico, accesible vía teclado con `Tab` y ejecutable con `Enter` / `Espacio`.
- `<section class="resumen" aria-labelledby="titulo-resumen" data-estado="disponible">`: Región dedicada a la retroalimentación y reversibilidad.
- `<p id="estado" role="status" aria-live="polite">`: Región viva accesible que notifica a tecnologías de asistencia (lectores de pantalla) sin alterar el flujo visual.
- `<button type="button" id="btn-cancelar" hidden>`: Control secundario para deshacer la acción.

---

## 5. Diseño CSS Mobile-First (`src/estilos.css`)

El diseño responsivo sigue estrictamente la metodología **Mobile-First**:
- **Columna única base (< 48rem):**
  Por defecto, la cuadrícula `.disposicion` se declara con `display: grid; grid-template-columns: 1fr; gap: 1rem;`. En pantallas de 360 px, la tarjeta queda en la parte superior y el resumen «Mi reserva» se posiciona inmediatamente abajo, eliminando el scroll horizontal (`scrollWidth = 360px`).
- **Punto de corte en 48rem (768 px):**
  Mediante `@media (min-width: 48rem)`, la cuadrícula se expande a dos columnas proporcionales (`grid-template-columns: 3fr 2fr;`). 
- **Preservación del orden del DOM:**
  No se utiliza `order`, `flex-direction: column-reverse` ni flotados que alteren el orden de tabulación y lectura respecto al árbol semántico HTML.
- **Ergonomía táctil y foco visible:**
  Los botones tienen un `min-height: 2.75rem` (44 px) satisfaciendo WCAG 2.5.5 / 2.5.8 (Target Size), y cuentan con `:focus-visible` con anillo de contraste de 3 px en tono ámbar (`#ffbf47`).

---

## 6. Estados de interacción y gestión de foco (`src/reserva.js` y `src/api.js`)

Se conectaron los tres momentos fundamentales del ciclo de vida de la reserva:
1. **Momento 1 · Disponible (Inicial):**
   - Estado: `data-estado="disponible"`.
   - Mensaje: «Aún no tienes una reserva.».
   - Cupos: 12 disponibles.
   - Botón «Reservar»: Habilitado (`disabled = false`).
   - Botón «Cancelar»: Oculto (`hidden = true`).
2. **Momento 2 · Confirmada (Acción completada):**
   - Estado: `data-estado="confirmada"` (resumen con fondo verde `#e6f4ea` y borde `#1e7b3a`).
   - Mensaje anunciado: «Reserva confirmada: Interfaces web accesibles · jueves de 14:00 a 16:00 · Laboratorio 2.».
   - Cupos: 11 disponibles.
   - Botón «Reservar»: Bloqueado (`disabled = true`, texto «Ya tienes un lugar»).
   - Botón «Cancelar»: Visible (`hidden = false`).
   - **Gestión del foco:** Como el botón original queda deshabilitado, el foco de teclado se transfiere inmediatamente con `btnCancelar.focus()`, previniendo que el usuario quede atrapado en un elemento inactivo (WCAG 2.4.3).
3. **Momento 3 · Cancelada (Acción deshecha):**
   - Estado: `data-estado="cancelada"` (resumen con fondo de aviso `#fff4e0` y borde `#a35a00`).
   - Mensaje anunciado: «Cancelaste tu reserva. El lugar vuelve a estar disponible.».
   - Cupos: 12 restituidos.
   - Botón «Reservar»: Re-habilitado (`disabled = false`).
   - Botón «Cancelar»: Oculto (`hidden = true`).
   - **Gestión del foco:** Al ocultarse el botón de cancelación, el foco vuelve automáticamente a `btnReservar.focus()`.

---

## 7. Decisiones de diseño HCI justificadas

| Decisión de diseño | Heurística / Principio | Justificación ergonómica y técnica |
|---|---|---|
| **Disposición en 1 columna en móvil y 2 columnas desde 48rem** | **Visibilidad del estado (H1)** · **WCAG 1.4.10 (Reajuste)** | En el boceto de 960 px, «Mi reserva» requería scroll horizontal de 600 px. En columna única, el estado se descubre naturalmente con scroll vertical natural. |
| **Colocación del `<dl>` antes del `<button>`** | **Jerarquía de información** · **H6 Reconocimiento** | La persona toma una decisión informada (horario y lugar) antes de comprometer su cupo con la acción principal. |
| **Inclusión del botón «Cancelar mi reserva»** | **Control y libertad del usuario (H3)** | Permite recuperarse de selecciones erróneas sin abandonar la pantalla y restituye el cupo inmediatamente. |
| **`role="status"` en mensaje de estado** | **Visibilidad del sistema (H1)** · **WCAG 4.1.3 Mensajes de estado** | Permite que lectores de pantalla anuncien el resultado sin interrumpir abruptamente el cursor ni forzar recargas. |
| **Desplazamiento programático de `.focus()`** | **Accesibilidad por teclado** · **WCAG 2.4.3 Orden del foco** | Evita la pérdida del foco cuando un control activo pasa a estar `disabled` u oculto en el árbol de accesibilidad. |

---

## 8. Evidencias y capturas preliminares

Las capturas de verificación se encuentran organizadas en la carpeta `04_capturas/`:
- `boceto-A-360.png`: Diagnóstico del boceto A a 360 px evidenciando el corte horizontal y la pérdida de «Mi reserva».
- `movil-360-disponible.png`: Prototipo adaptado a 360 px en estado inicial (1 columna fluida, sin scroll horizontal).
- `movil-360-confirmada.png`: Prototipo a 360 px con reserva confirmada, retroalimentación visible y botón cancelar activo.
- `movil-360-cancelada.png`: Prototipo a 360 px en estado cancelado con restitución de cupo.
- `escritorio-768-confirmada.png`: Vista al punto de corte exacto de 48rem (768 px) en 2 columnas.
- `escritorio-1366-confirmada.png`: Vista en pantalla completa de escritorio (1366 px) con layout equilibrado.

---

## 9. Revisión entre pares e hipótesis para la Fase 2

### Matriz de revisión entre pares

| Tarea evaluada por revisor externo | Móvil (360 px) | Escritorio (1366 px) | Observación / Hallazgo |
| :--- | :--- | :--- | :--- |
| **1. Localizar el horario del taller** | Exitoso (< 2 s) | Exitoso (< 2 s) | La etiqueta `<dt>Horario</dt>` permite identificación inmediata en ambas resoluciones. |
| **2. Reservar un lugar** | Exitoso (1 clic/Enter) | Exitoso (1 clic/Enter) | El botón responde al instante; el cambio de color a verde y el texto confirman el éxito. |
| **3. Cancelar la reserva** | Exitoso (1 clic/Enter) | Exitoso (1 clic/Enter) | La acción se deshace limpiamente; el foco regresa al botón de reservar. |

### Hipótesis para validación empírica en la Fase 2

> **Hipótesis:** Al confirmar o cancelar la reserva exclusivamente mediante el teclado, una persona usuaria que dependa de un lector de pantalla (NVDA en Windows o TalkBack en Android) percibe con claridad el anuncio generado por la región `role="status"` y comprende que el foco se ha reubicado en la siguiente acción disponible, sin desorientarse ni experimentar trampas de teclado.

**Criterio medible de validación:**
La hipótesis se considerará formalmente validada en la Fase 2 si al menos **4 de 5 participantes (80 % o superior)** en las sesiones de prueba con lector de pantalla pueden repetir verbalmente el nuevo estado de su reserva de forma inmediata tras presionar Enter, sin requerir exploración manual adicional ni ayuda del moderador.
