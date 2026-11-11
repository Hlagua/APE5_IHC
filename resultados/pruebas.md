# APE 5 · Pruebas técnicas en navegador · CaféU «Mi pedido»

- **Grupo:** 5 · **Responsable:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos), Tester · rama `pruebas-informe` · Issue #4
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)
- **Fecha de medición:** 11/11/2026
- **Versión evaluada (B):** `src/index.html` + `src/estilos.css` + `src/interaccion.js` + `src/api.js`
- **Línea base (A):** `prototipos/prototipo-A.html` (boceto de escritorio de «Mi pedido», 960 px fijos)

## 1. Método

1. Servir el repositorio en local (`python -m http.server 8768`) y abrirlo en Chromium.
2. DevTools → barra de dispositivos (`Ctrl + Shift + M`) → **Responsive**, **zoom 100 %**, fuente predeterminada (16 px).
3. En cada viewport, ejecutar en la consola:
   ```js
   ({ innerWidth, scrollWidth: document.documentElement.scrollWidth,
      columnas: getComputedStyle(document.querySelector('.disposicion')).gridTemplateColumns })
   ```
4. Criterio de aprobación: `scrollWidth <= innerWidth`, es decir, **0 px de desborde horizontal**.
5. Las capturas de `evidencias/` se generan con `_scripts/ape5_fase2_evidencias.py`. El script carga la página en un iframe del tamaño exacto del viewport, vuelve a medir y escribe el resultado en una franja sobre cada imagen (oscura si pasa, roja si hay desborde).

> **Atención en la demostración en vivo:** con el tipo de dispositivo «Mobile» en DevTools, el boceto A **no** muestra barra horizontal: Chromium aleja la página (sección 3). Para ver los +600 px, hay que cambiar el tipo de dispositivo a «Desktop» o medir con la consola.

## 2. Resultados de la versión B (Mobile-First)

| Viewport | innerWidth | scrollWidth | Desborde | Columnas de `.disposicion` | Resultado | Evidencia |
| :--- | ---: | ---: | ---: | :--- | :---: | :--- |
| 320 × 720 | 320 | 320 | **0 px** | 1 (288 px) | ✅ Aprobado | `evidencias/B-320.png` |
| 360 × 800 | 360 | 360 | **0 px** | 1 (328 px) | ✅ Aprobado | `evidencias/B-360.png`, `B-360-confirmada.png` |
| 768 × 1024 | 768 | 768 | **0 px** | 2 (417,6 px · 278,4 px) | ✅ Aprobado | `evidencias/B-768.png` |
| 1366 × 768 | 1366 | 1366 | **0 px** | 2 (532,8 px · 355,2 px) | ✅ Aprobado | `evidencias/B-1366.png`, `B-1366-confirmada.png` |

- **Punto de corte:** a **767 px** la cuadrícula sigue en una columna (735,3 px, sin desborde) y a **768 px** (48rem) pasa a dos.
- **Caso extremo:** con un producto de 88 caracteres («Sánduche integral de pollo desmechado con aguacate, tomate y queso fresco de la casa») a 320 px, `scrollWidth = 320`. El nombre se ajusta en varias líneas.
- **Escala en emulación móvil:** `visualViewport.scale = 1` a 320 y 360 px. El texto conserva su tamaño real.

## 3. Línea base: boceto A de CaféU (960 px fijos)

| Viewport | innerWidth | scrollWidth | Desborde | Panel «Estado del pedido» | Evidencia |
| :--- | ---: | ---: | ---: | :--- | :--- |
| 320 × 720 | 320 | 960 | **+640 px** | Empieza en x = 600 px: fuera de la pantalla | `evidencias/A-320.png` |
| 360 × 800 | 360 | 960 | **+600 px** | Empieza en x = 600 px: fuera de la pantalla | `evidencias/A-360.png` |
| 768 × 1024 | 768 | 960 | **+192 px** | Cortado a la derecha | `evidencias/A-768.png` |
| 1366 × 768 | 1366 | 1366 | 0 px | Visible | `evidencias/A-1366.png` |

**Con emulación de dispositivo móvil (360 px):** Chromium amplía el viewport de diseño a 960 px y aleja la página: `innerWidth = scrollWidth = 960` y `visualViewport.scale = 0,375`. El texto de 18 px se ve de **6,75 px**. El boceto A «cabe», pero no se puede leer.

## 4. Teclado, cobro único y foco (360 × 800, pulsaciones reales)

Prueba con teclas reales, partiendo de una sesión limpia (saldo $10.00).

| Paso | Tecla | Foco resultante | Estado | Saldo | `#btn-confirmar` | Mensaje en `role="status"` |
| :---: | :--- | :--- | :--- | ---: | :--- | :--- |
| 0 | — (carga) | `body` | pendiente | $10.00 | «Confirmar y pagar · $4.25» | «Aún no confirmas tu pedido. No se ha cobrado nada.» |
| 1 | `Tab` | `#btn-confirmar` | pendiente | $10.00 | habilitado | — |
| 2 | `Enter` `Enter` (doble) | **`#btn-cancelar`** | **confirmado** | **$5.75** | **disabled** · «Pedido #A24 pagado» | «Pedido #A24 confirmado y pagado ($4.25). Estará listo en unos 10 minutos en el Edificio central.» |
| 3 | `Shift + Tab` | `#btn-cancelar` (el botón deshabilitado se omite) | confirmado | $5.75 | disabled | — |
| 4 | `Espacio` (1 s después) | **`#btn-confirmar`** | cancelado | **$10.00** | habilitado | «Cancelaste el pedido #A24. Se devolvieron $4.25 a tu tarjeta universitaria.» |
| 5 | `Enter` | `#btn-cancelar` | confirmado | $5.75 | disabled · «Pedido #A25 pagado» | «Pedido #A25 confirmado y pagado…» |

- **Orden de tabulación:** igual al orden del DOM (pedido → estado) en todos los anchos. El CSS no usa `order` ni posicionamiento.
- **Cobro único:** con el pedido pagado, 5 activaciones más de «Confirmar y pagar» dejan el saldo en $5.75 (suite, TC-07).
- **Foco visible:** contorno de 3 px (#1F1A17) con `:focus-visible`.

## 5. Hallazgo H-01: el doble Enter cancelaba el pedido recién pagado

| | Sin el margen | Con el margen de 600 ms (versión entregada) |
| :--- | :--- | :--- |
| Prueba | `Tab` → `Enter` → `Enter` inmediato | La misma |
| Estado final | **cancelado**, saldo $10.00 («Cancelaste el pedido #A24…») | **confirmado**, saldo $5.75 |
| Explicación | El primer Enter paga y mueve el foco a «Cancelar pedido»; el segundo cae sobre ese botón y deshace el pago sin que el estudiante lo quiera. | «Cancelar pedido» ignora activaciones durante 600 ms después de confirmar (`MARGEN_DOBLE_PULSACION_MS`). Cancelar 1 s después funciona normalmente. |

- **Cómo se reprodujo el «sin margen»:** en la consola se adelantó `performance.now()` antes del segundo Enter, sin modificar el código.
- **Principio:** H5, prevención de errores. Se conserva el traslado del foco que pide la guía (WCAG 2.4.3).
- **Origen:** prueba exploratoria del equipo con teclado, no observación de participantes. El mismo defecto se había encontrado antes en el ejercicio de clase «Aula Abierta».

## 6. Suite automática

`tests/test_runner.html` da **10 de 10 aprobadas**: estructura semántica, `role="status"`, botones nativos, 0 desborde a 360 px, confirmación con #A24 y cobro de $4.25, foco a «Cancelar», 0 cobros duplicados en 5 intentos, doble Enter sin cancelación, cancelación con devolución a $10.00 y foco de vuelta a «Confirmar y pagar».

## 7. Para la prueba con usuarios

`src/api.js` guarda el pedido en `sessionStorage`. Si se recarga en la misma pestaña, el pedido sigue pagado. **Entre un participante y otro** hay que abrir una pestaña nueva o ejecutar `PedidoAPI.reiniciar()` en la consola.

## 8. Conclusión técnica

La versión B de «Mi pedido» cumple el criterio: **0 px de desborde horizontal en 320, 360, 768 y 1366 px** al 100 % de zoom, frente a +640, +600 y +192 px del boceto A. La tarea completa (pagar, comprobar y cancelar) se hace solo con teclado, nunca se cobra dos veces y el foco nunca queda sobre un control deshabilitado u oculto.
