# Protocolo de pruebas · APE 5 · CaféU «Mi pedido»

- **Grupo:** 5 · **Autor:** Carlos Giovanni Ramos Jácome ([@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos)), Tester
- **Pantalla:** `src/index.html` (versión B) · **Línea base:** `prototipos/prototipo-A.html`

## 1. Casos de prueba técnicos

Los resultados medidos están en `resultados/pruebas.md`. La columna «Automatizado» indica qué casos comprueba `tests/test_runner.html`.

| ID | Categoría | Procedimiento | Resultado esperado | Automatizado |
| :--- | :--- | :--- | :--- | :---: |
| TC-RESP-01 | Responsivo | 320 × 720 y 360 × 800 en DevTools; medir `scrollWidth` | `scrollWidth = innerWidth`; 1 columna | TC-04 (360 px) |
| TC-RESP-02 | Responsivo | 767 px | Sigue en 1 columna | — |
| TC-RESP-03 | Responsivo | 768 px (48rem) | 2 columnas `3fr 2fr`, mismo orden del DOM | — |
| TC-RESP-04 | Responsivo | 1366 × 768 | 2 columnas, contenedor centrado (`max-width: 60rem`) | — |
| TC-A11Y-01 | Teclado | Cargar la página y pulsar Tab | El foco va primero a «Confirmar y pagar», con contorno visible | — |
| TC-A11Y-02 | Foco | Enter sobre «Confirmar y pagar» | Pedido #A24 pagado; foco en «Cancelar pedido» | TC-05, TC-06 |
| TC-A11Y-03 | Foco | Enter sobre «Cancelar pedido» (pasado 1 s) | Pedido cancelado; foco en «Confirmar y pagar» | TC-09, TC-10 |
| TC-A11Y-04 | Estado | Revisar `#estado` | `role="status"` y `aria-live="polite"` | TC-02 |
| TC-FUNC-01 | Cobro único | Con el pedido pagado, activar 5 veces «Confirmar y pagar» | Saldo $5.75 sin cambios | TC-07 |
| TC-FUNC-02 | Doble pulsación | Tab → Enter Enter | Pedido sigue pagado (H-01) | TC-08 |
| TC-FUNC-03 | Devolución | Pagar y cancelar | Saldo $10.00 → $5.75 → $10.00 | TC-05, TC-09 |

## 2. Prueba con usuarios

El procedimiento, la consigna neutral y la tabla de registro están en `resultados/checklist.md`.

## 3. Cuestionario SUS (opcional, al final de cada participante)

Escala de 1 (totalmente en desacuerdo) a 5 (totalmente de acuerdo):

1. Creo que me gustaría usar esta pantalla de pedido con frecuencia.
2. Encontré la pantalla innecesariamente compleja.
3. Pensé que la pantalla era fácil de usar.
4. Creo que necesitaría ayuda de otra persona para usarla.
5. Las funciones de la pantalla estaban bien integradas.
6. Había demasiada inconsistencia en la pantalla.
7. La mayoría de la gente aprendería a usarla muy rápido.
8. La pantalla me resultó muy engorrosa.
9. Me sentí seguro de que mi pedido se pagó una sola vez.
10. Necesité aprender muchas cosas antes de poder usarla.

**Cálculo:** ítems impares, respuesta − 1; ítems pares, 5 − respuesta; suma × 2,5 (de 0 a 100).

| Participante | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | SUS |
| :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| P-01 | | | | | | | | | | | |
| P-02 | | | | | | | | | | | |
| P-03 | | | | | | | | | | | |
| P-04 | | | | | | | | | | | |
| P-05 | | | | | | | | | | | |

> Reportar un puntaje SUS solo si se aplicó el cuestionario y se registraron las respuestas de cada participante.
