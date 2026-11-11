# APE 5 · Diagnóstico y ficha de aplicación · CaféU

- **Institución:** Universidad Técnica de Ambato (UTA) · FISEI · Ingeniería de Software
- **Asignatura:** Interacción Humano-Computador · Quinto "A" · **Docente:** Ing. Mg. José Caiza
- **Grupo:** 5 · **Repositorio:** https://github.com/Hlagua/APE5_IHC
- **Proyecto del grupo:** **CaféU**, la aplicación de pedidos de la cafetería universitaria trabajada en el APE 4 ([Hlagua/APE4_IHC](https://github.com/Hlagua/APE4_IHC)).
- **Pantalla transformada:** «Mi pedido → Confirmar y pagar» (W4 Resumen del APE 4) → `src/`
- **Responsable de la ficha:** Melany Saleth Cevallos Goyes (@SalyC15) · rama `prototipo-html` · Issue #2 · **Revisión cruzada:** Alison Marcela Cobos Taco (@Itsuna18)

---

## 1. De dónde viene la pantalla

En el APE 4, CaféU se diseñó y probó como prototipo **móvil** (v1 → v3.1): wireframes, Figma y un prototipo HTML con un marco de teléfono fijo. El APE 5 pide llevar una pantalla a una **interfaz web real y adaptable**, que funcione igual en un teléfono y en un computador. Elegimos «Mi pedido» porque es el punto donde el estudiante decide pagar, y donde el APE 4 detectó el mayor riesgo para el usuario: **el temor a pagar dos veces** (problema D1, H9).

| Dato | Valor (del prototipo CaféU v3.1) |
| :--- | :--- |
| Productos | 1 × Café Americano 12 oz ($1.50) · 1 × Sánduche de jamón y queso ($2.75) |
| Total | $4.25 |
| Retiro | Edificio central · listo en unos 10 minutos |
| Pago | Tarjeta universitaria |
| Número de pedido | #A24 |

## 2. Diagnóstico del boceto A (versión de escritorio de 960 px)

`prototipos/prototipo-A.html` es la misma pantalla como boceto de escritorio: `body { width: 960px }` y una cuadrícula fija de `580px 360px`. A la izquierda está el pedido y el botón «Confirmar y pagar»; a la derecha, el panel «Estado del pedido».

1. **Desborde horizontal:** a 360 px, `document.documentElement.scrollWidth = 960` frente a `innerWidth = 360`, es decir, **+600 px**. A 320 px son +640 px y a 768 px, +192 px (`resultados/pruebas.md`).
2. **Se pierde la información crítica:** el panel «Estado del pedido» empieza en x = 600 px, fuera de la pantalla del teléfono. El estudiante paga y **no ve si el pago se hizo**, justo el temor de doble cobro que encontramos en el APE 4.
3. **En un teléfono el fallo cambia de forma, pero persiste:** con emulación de dispositivo móvil, Chromium no muestra la barra horizontal. Lo que hace es alejar toda la página (`visualViewport.scale = 0,375`), y el texto de 18 px se ve de **6,75 px**. El estado «cabe», pero no se puede leer.
4. **Sin control ni anuncio:** el botón del boceto está deshabilitado, no existe `role="status"` y no hay forma de cancelar.

Principios afectados: **H1** Visibilidad del estado del sistema, **H9** Recuperarse de errores, **WCAG 1.4.10** Reajuste, **WCAG 4.1.3** Mensajes de estado.

## 3. Ficha de aplicación

| Campo | CaféU · «Mi pedido» |
| :--- | :--- |
| **Actor** | Estudiante universitario con poco tiempo entre clases que pide desde el celular |
| **Tarea principal** | Confirmar y pagar su pedido para retirarlo sin hacer fila |
| **Dato clave que decide la acción** | Productos, **total ($4.25)**, lugar y tiempo de retiro (Edificio central, 10 min) y medio de pago con su saldo (`<dl>`) |
| **Acción principal** | Botón «Confirmar y pagar · $4.25» |
| **Resultado visible** | En `<p role="status">`: «Pedido **#A24** confirmado y pagado ($4.25). Estará listo en unos 10 minutos en el Edificio central.» El panel se pone verde, el saldo baja de $10.00 a $5.75 y el botón cambia a «Pedido #A24 pagado» (deshabilitado) |
| **Mecanismo para corregir o cancelar** | Antes de pagar: «Editar» el pedido (pantalla W5 del APE 4). Después de pagar: botón **«Cancelar pedido»**, que devuelve los $4.25 a la tarjeta y deja confirmar de nuevo |

**Requisito (RF-PED-01):** el estudiante debe poder confirmar y pagar su pedido una sola vez, ver de inmediato el número de pedido y cuándo retirarlo, y cancelarlo con devolución si se equivocó.

## 4. Regla de interacción y criterio de aceptación

- **Regla:** **un pedido se cobra una sola vez.** Al confirmar, «Confirmar y pagar» queda `disabled`, el controlador ignora nuevas confirmaciones y `PedidoAPI.confirmarPedido()` rechaza el segundo cobro (`src/interaccion.js`, `src/api.js`).
- **Criterios de aceptación medibles:**
  - Con el pedido pagado (saldo $5.75), **5 intentos** de activar «Confirmar y pagar» dejan el saldo en **$5.75**: 0 cobros duplicados en 5 de 5.
  - Un **doble Enter** (dos pulsaciones en menos de 600 ms) deja el pedido **confirmado**: 0 cancelaciones accidentales.
  - Tras confirmar, el foco queda en «Cancelar pedido»; tras cancelar, en «Confirmar y pagar».
  - Cancelar devuelve exactamente $4.25 (saldo de $5.75 a $10.00).

## 5. Decisiones HCI

| Decisión | Principio | Justificación |
| :--- | :--- | :--- |
| Una columna en móvil y dos desde 48rem, sin reordenar el DOM | H1 · WCAG 1.4.10 · 1.3.2 | En el boceto A el estado quedaba a 600 px a la derecha; ahora aparece justo debajo del botón de pagar. |
| Total, retiro y pago en un `<dl>` antes del botón | Jerarquía · H6 | El estudiante ve cuánto paga y con qué antes de comprometer su dinero. |
| `disabled` + texto «Pedido #A24 pagado» | H5 Prevención de errores | Responde al temor de doble cobro del APE 4 (D1). |
| «Cancelar pedido» con devolución visible | H3 Control · H9 | Deshacer sin salir de la pantalla y ver el saldo restituido. |
| `role="status"` con número, total y tiempo | H1 · WCAG 4.1.3 | El lector de pantalla anuncia el resultado sin mover el foco. |
| `.focus()` al siguiente control y margen de 600 ms | WCAG 2.4.3 · H5 | El foco nunca queda en un botón deshabilitado u oculto, y un doble Enter no cancela el pago (H-01). |

## 6. Hipótesis para la validación

> En un viewport de 360 px, un estudiante que no conoce la pantalla confirma su pedido y **dice su número de pedido y si ya pagó sin buscarlo y sin pedir ayuda**.

Se considera validada si al menos **4 de 5** participantes lo logran. La prueba con lector de pantalla (NVDA o TalkBack) queda para la siguiente iteración.
