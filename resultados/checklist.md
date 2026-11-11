# APE 5 · Observación con usuarios en aula · CaféU «Mi pedido»

- **Grupo:** 5 · **Responsable del registro:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · rama `pruebas-informe` · Issue #4
- **Moderación y cronómetro:** _________________ · **Registro:** _________________
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)
- **Fecha:** ___/___/2026 · **Lugar:** _________________

> Registrar **solo lo que se observe en la sesión**, con participantes de otros grupos. No completar filas con datos supuestos ni copiar resultados de otra pantalla.

## 1. Preparación (antes de cada participante)

- [ ] Abrir `src/index.html` en una **pestaña nueva** o ejecutar `PedidoAPI.reiniciar()` en la consola. Debe verse «Aún no confirmas tu pedido. No se ha cobrado nada.» y saldo $10.00.
- [ ] Fijar el viewport en DevTools (360 × 800 para móvil o 1366 × 768 para escritorio) con zoom al 100 %.
- [ ] El participante es de **otro grupo** y no ha visto este prototipo de CaféU.
- [ ] Cronómetro en cero; no señalar la pantalla.

## 2. Consigna neutral (leer textual)

> «Ya elegiste tu café y tu sánduche en la app de la cafetería. Termina tu compra para poder retirarla, y después dime tu número de pedido y si ya pagaste. Luego imagina que te equivocaste: deshaz la compra. Avísame cuando creas que terminaste.»

- No mencionar los nombres de los botones («Confirmar y pagar», «Cancelar pedido») ni dónde están.
- Si el participante pide ayuda, responder primero: «¿Qué harías si estuvieras solo?». Si insiste, darle una pista mínima y anotarla como **solicitud de ayuda**.
- El tiempo empieza al terminar de leer la consigna y se detiene cuando el participante dice que terminó.

## 3. Definiciones de registro

| Métrica | Cómo se cuenta |
| :--- | :--- |
| Tiempo de tarea (s) | Desde el fin de la consigna hasta que dice «terminé» |
| Errores de navegación | Clics o pulsaciones que no llevan a la tarea, desplazamiento horizontal o retrocesos para buscar algo |
| Solicitudes de ayuda | Cada pregunta al moderador o pista recibida |
| Dice n.º y pago | **Sí** si dice «#A24» y que ya pagó sin buscarlo · **No** en otro caso |
| Éxito | **S** pagó, dijo n.º y estado, y canceló sin ayuda · **P** lo logró con ayuda · **N** no lo logró |

## 4. Tabla de observación

| Part. | Grupo | Versión | Viewport | Tiempo (s) | Errores de navegación | Solicitudes de ayuda | Dice n.º y pago | Éxito (S/P/N) | Dificultades detectadas (citas textuales) |
| :---: | :---: | :---: | :---: | ---: | ---: | ---: | :---: | :---: | :--- |
| P-01 | | B | 360 × 800 | | | | | | |
| P-02 | | B | 360 × 800 | | | | | | |
| P-03 | | B | 1366 × 768 | | | | | | |
| P-04 | | B | 360 × 800 | | | | | | |
| P-05 | | B | 360 × 800 | | | | | | |
| P-06 | | A | 360 × 800 | | | | | | |

> P-06 es opcional: hace la tarea con el **boceto A** (`prototipos/prototipo-A.html`) para comparar. El boceto A no permite pagar (botón deshabilitado), así que solo se registra si encuentra el total y el estado del pedido.

## 5. Lista de verificación durante la observación

| Comportamiento observado | P-01 | P-02 | P-03 | P-04 | P-05 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Lee el total antes de pagar | | | | | |
| Encuentra el estado del pedido sin desplazarse horizontalmente | | | | | |
| Dice el número de pedido sin buscarlo | | | | | |
| Nota que el botón quedó bloqueado («Pedido #A24 pagado») | | | | | |
| Encuentra «Cancelar pedido» sin buscarlo | | | | | |
| Pregunta si «se cobró» o si «se cobró dos veces» | | | | | |

## 6. Resumen (completar al final)

- Tiempo medio de la versión B: ______ s · Errores en la versión B: ______ · Ayudas en la versión B: ______
- Participantes que dijeron n.º y estado de pago sin buscarlo: ____ de ____
- Dificultad más repetida: ________________________________________________
- ¿Se valida la hipótesis de `docs/proyecto.md` (al menos 4 de 5 dicen n.º y pago sin buscarlo)? **Sí / No / Parcial**, porque ________________________
