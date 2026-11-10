# APE 5 · Fase 2 · Pruebas técnicas en navegador

- **Grupo:** 5 · **Responsable:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos), Tester · rama `pruebas-informe` · Issue #4
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)
- **Fecha de medición:** 10/11/2026
- **Versión evaluada:** `src/index.html` + `src/estilos.css` + `src/interaccion.js` + `src/api.js` (versión B, integrada en `main`)
- **Línea base:** `prototipos/prototipo-A.html` (boceto A, ancho fijo de 960 px)

## 1. Método

1. Abrir el prototipo servido en local (`python -m http.server 8766`) en Chromium.
2. DevTools → barra de dispositivos (`Ctrl + Shift + M`) → modo **Responsive**, **zoom 100 %**, fuente predeterminada (16 px).
3. Fijar cada viewport y ejecutar en la consola:
   ```js
   ({ innerWidth, scrollWidth: document.documentElement.scrollWidth,
      columnas: getComputedStyle(document.querySelector('.disposicion')).gridTemplateColumns })
   ```
4. Criterio de aprobación (R2): `scrollWidth <= innerWidth` → **0 px de desborde horizontal**.
5. Las capturas de `evidencias/` se generan con `_scripts/ape5_fase2_evidencias.py`. El script carga la página en un iframe del tamaño exacto del viewport, vuelve a medir y escribe el resultado en una franja sobre cada imagen (oscura si pasa, roja si hay desborde).

## 2. Resultados de la versión B (Mobile-First)

| Viewport | innerWidth | scrollWidth | Desborde | Columnas de `.disposicion` | Resultado | Evidencia |
| :--- | ---: | ---: | ---: | :--- | :---: | :--- |
| 320 × 720 | 320 | 320 | **0 px** | 1 (288 px) | ✅ Aprobado | `evidencias/B-320.png` |
| 360 × 800 | 360 | 360 | **0 px** | 1 (328 px) | ✅ Aprobado | `evidencias/B-360.png`, `B-360-confirmada.png` |
| 768 × 1024 | 768 | 768 | **0 px** | 2 (417,6 px · 278,4 px) | ✅ Aprobado | `evidencias/B-768.png` |
| 1366 × 768 | 1366 | 1366 | **0 px** | 2 (532,8 px · 355,2 px) | ✅ Aprobado | `evidencias/B-1366.png`, `B-1366-confirmada.png` |

**Prueba del punto de corte:** a **767 px** la cuadrícula se mantiene en una columna (735 px, sin desborde) y a **768 px** (48rem) cambia a dos columnas. El cambio ocurre exactamente en `@media (min-width: 48rem)`.

**Caso extremo:** con un título de 81 caracteres a 320 px («Taller intensivo de diseño de interfaces web accesibles para dispositivos móviles»), `scrollWidth = 320` y la tarjeta termina en x = 304 px. El texto se ajusta en varias líneas sin desbordar.

**Escala visual en emulación móvil:** `visualViewport.scale = 1` a 360 px. La página no se aleja y el texto conserva su tamaño real de 16 px.

## 3. Línea base: boceto A (ancho fijo de 960 px)

| Viewport | innerWidth | scrollWidth | Desborde | Panel «Mi reserva» | Evidencia |
| :--- | ---: | ---: | ---: | :--- | :--- |
| 320 × 720 | 320 | 960 | **+640 px** | Empieza en x = 600 px: fuera de la pantalla | `evidencias/A-320.png` |
| 360 × 800 | 360 | 960 | **+600 px** | Empieza en x = 600 px: fuera de la pantalla | `evidencias/A-360.png` |
| 768 × 1024 | 768 | 960 | **+192 px** | Empieza en x = 600 px: cortado a la derecha | `evidencias/A-768.png` |
| 1366 × 768 | 1366 | 1366 | 0 px | Visible (x = 803 px) | `evidencias/A-1366.png` |

**Hallazgo adicional con emulación de dispositivo móvil (320 y 360 px):** Chromium no muestra el desborde. Amplía el viewport de diseño a 960 px y **aleja toda la página** (`visualViewport.scale = 0,375`). El texto de 18 px se ve con un tamaño efectivo de **6,8 px**. Es decir, el boceto A falla de dos maneras: desborde horizontal (+600 px) o texto ilegible. Ninguna de las dos permite leer el estado de la reserva a simple vista.

## 4. Interacción por teclado y prevención de duplicados (360 × 800)

Prueba hecha con pulsaciones reales de teclado (no con clics simulados), partiendo de una sesión limpia.

| Paso | Tecla | Foco resultante | Estado | Cupos | `#btn-reservar.disabled` | `#btn-cancelar.hidden` | Mensaje en `role="status"` |
| :--- | :--- | :--- | :--- | ---: | :---: | :---: | :--- |
| 0 | — (carga) | `body` | disponible | 12 | false | true | «Aún no tienes una reserva.» |
| 1 | `Tab` | `#btn-reservar` | disponible | 12 | false | true | — |
| 2 | `Enter` | **`#btn-cancelar`** | confirmada | 11 | **true** | false | «Reserva confirmada: Interfaces web accesibles · Jueves, 14:00 a 16:00 · Laboratorio 2.» |
| 3 | `click()` forzado sobre Reservar | `#btn-cancelar` | confirmada | **11** (no cambia) | true | false | — |
| 4 | `Shift + Tab` | `#btn-cancelar` (Reservar deshabilitado se omite) | confirmada | 11 | true | false | — |
| 5 | `Espacio` | **`#btn-reservar`** | cancelada | 12 | false | true | «Cancelaste tu reserva. El lugar vuelve a estar disponible.» |

- **Orden de tabulación:** igual al orden del DOM (tarjeta → resumen) en 320, 360, 768 y 1366 px. El CSS no usa `order` ni posicionamiento que altere la lectura.
- **Prevención de duplicados:** con la reserva confirmada, ni `Enter` ni un `click()` forzado sobre el botón deshabilitado cambian los cupos (11 → 11).
- **Foco visible:** contorno ámbar de 3 px con `:focus-visible` en ambos botones.

## 5. Hallazgo H-01 y corrección: doble Enter cancelaba la reserva

| | Antes (fase 1) | Después (fase 2) |
| :--- | :--- | :--- |
| Prueba | `Tab` → `Enter` `Enter` (dos pulsaciones seguidas) | La misma |
| Estado final | **cancelada**, cupos 12 | **confirmada**, cupos 11 |
| Foco final | `#btn-reservar` | `#btn-cancelar` |
| Explicación | El primer Enter reserva y mueve el foco a «Cancelar»; el segundo Enter cae sobre «Cancelar» y deshace la reserva sin que la persona lo quiera. | Durante 600 ms después de confirmar, «Cancelar» ignora activaciones (`MARGEN_DOBLE_PULSACION_MS` en `src/interaccion.js`). |
| Comprobación de que cancelar sigue funcionando | — | Enter sobre «Cancelar» 1 s después → **cancelada**, cupos 12, foco en `#btn-reservar` |

- **Principio:** prevención de errores (Nielsen H5). Se conserva el traslado del foco que pide la guía (WCAG 2.4.3).
- **Origen:** prueba exploratoria con teclado del equipo, no observación de participantes.

**Suite automática:** `tests/test_runner.html` da **9 de 9 aprobadas** con la corrección (TC-07 espera 700 ms antes de cancelar y la nueva TC-09 comprueba que la activación inmediata de «Cancelar» se ignora). Sin la espera, TC-07 y TC-08 fallaban porque simulaban una cancelación instantánea, justo el caso que H-01 bloquea.

## 6. Observaciones para la prueba con usuarios

- `src/api.js` guarda la reserva en `sessionStorage`. Al recargar en la misma pestaña, la reserva sigue confirmada (cupos 11). **Entre un participante y otro** hay que abrir una pestaña nueva o ejecutar `ReservaAPI.reiniciar()` en la consola, para que todos empiecen con «Aún no tienes una reserva.».

## 7. Conclusión técnica

La versión B cumple el criterio R2: **0 px de desborde horizontal en 320, 360, 768 y 1366 px** al 100 % de zoom. El boceto A desborda 640, 600 y 192 px en los tres primeros anchos. La tarea completa (reservar y cancelar) puede hacerse solo con teclado, y el foco nunca queda sobre un control deshabilitado u oculto.
