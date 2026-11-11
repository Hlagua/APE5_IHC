# APE 5 · Observación con usuarios en aula · CaféU «Mi pedido»

- **Grupo:** 5 · **Responsable del registro:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · rama `pruebas-informe` · Issue #4
- **Moderación y cronómetro:** Carlos Giovanni Ramos Jácome · **Registro:** Melany Saleth Cevallos Goyes
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)
- **Fecha:** 11/11/2026 · **Lugar:** Laboratorio de Cómputo FISEI - UTA

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
| P-01 | G2 | B | 360 × 800 | 16 | 0 | 0 | Sí | S | Leyó el total ($4.25) en orden y confirmó al instante («Ya salió que el pedido #A24 está pagado»). |
| P-02 | G3 | B | 360 × 800 | 14 | 0 | 0 | Sí | S | Verificó el tiempo de retiro (10 min) y notó el saldo restante de $5.75. |
| P-03 | G1 | B | 1366 × 768 | 12 | 0 | 0 | Sí | S | En escritorio identificó de inmediato las dos columnas y usó «Cancelar pedido» sin dificultad. |
| P-04 | G4 | B | 360 × 800 | 15 | 0 | 0 | Sí | S | Navegó exclusivamente por teclado (Tab/Enter); el foco pasó directamente a Cancelar. |
| P-05 | G2 | B | 360 × 800 | 15 | 0 | 0 | Sí | S | Presionó Enter repetidamente y verificó que no se produjo doble cobro. |
| P-06 | G3 | A | 360 × 800 | 36 | 2 | 1 | No | N | Tuvo que hacer scroll horizontal buscando el estado; el botón estaba deshabilitado de fábrica. |

> P-06 es opcional: hace la tarea con el **boceto A** (`prototipos/prototipo-A.html`) para comparar. El boceto A no permite pagar (botón deshabilitado), así que solo se registra si encuentra el total y el estado del pedido.

## 5. Lista de verificación durante la observación

| Comportamiento observado | P-01 | P-02 | P-03 | P-04 | P-05 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Lee el total antes de pagar | Sí | Sí | Sí | Sí | Sí |
| Encuentra el estado del pedido sin desplazarse horizontalmente | Sí | Sí | Sí | Sí | Sí |
| Dice el número de pedido sin buscarlo | Sí | Sí | Sí | Sí | Sí |
| Nota que el botón quedó bloqueado («Pedido #A24 pagado») | Sí | Sí | Sí | Sí | Sí |
| Encuentra «Cancelar pedido» sin buscarlo | Sí | Sí | Sí | Sí | Sí |
| Pregunta si «se cobró» o si «se cobró dos veces» | No | No | No | No | No |

## 6. Resumen (completar al final)

- Tiempo medio de la versión B: 14,4 s · Errores en la versión B: 0 · Ayudas en la versión B: 0
- Participantes que dijeron n.º y estado de pago sin buscarlo: 5 de 5
- Dificultad más repetida: Ninguna en versión B; en boceto A (P-06) el participante requirió scroll horizontal continuo y preguntó dónde estaba el estado del pedido.
- ¿Se valida la hipótesis de `docs/proyecto.md` (al menos 4 de 5 dicen n.º y pago sin buscarlo)? **Sí**, porque el 100 % (5 de 5) identificó el número de pedido #A24 y el estado confirmado inmediatamente tras pulsar confirmar, con 0 errores y 0 solicitudes de ayuda.
