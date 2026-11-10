# APE 5 · Fase 2 · Observación con usuarios en aula

- **Grupo:** 5 · **Responsable del registro:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · rama `pruebas-informe` · Issue #4
- **Moderación y cronómetro:** _________________ · **Registro:** _________________
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)
- **Fecha:** 10/11/2026 · **Lugar:** aula de clase

> Registrar **solo lo que se observe en la sesión**. No completar filas con datos supuestos.

## 1. Preparación (antes de cada participante)

- [ ] Abrir `src/index.html` en una **pestaña nueva** o ejecutar `ReservaAPI.reiniciar()` en la consola. La pantalla debe mostrar «Aún no tienes una reserva.» y 12 cupos.
- [ ] Fijar el viewport en DevTools (360 × 800 para móvil o 1366 × 768 para escritorio) con zoom al 100 %.
- [ ] El participante es de **otro grupo** y no ha visto el prototipo.
- [ ] Tener el cronómetro en cero y no señalar la pantalla.

## 2. Consigna neutral (leer textual)

> «Necesitas asistir al taller del jueves. Averigua a qué hora y dónde se dicta, aparta un lugar y luego deshaz esa acción. Avísame cuando creas que terminaste.»

- No mencionar los nombres de los botones («Reservar», «Cancelar») ni dónde están.
- Si el participante pide ayuda, responder primero: «¿Qué harías si estuvieras solo?». Si insiste, darle una pista mínima y anotarla como **solicitud de ayuda**.
- El tiempo empieza al terminar de leer la consigna y se detiene cuando el participante dice que terminó.

## 3. Definiciones de registro

| Métrica | Cómo se cuenta |
| :--- | :--- |
| Tiempo de tarea (s) | Desde el fin de la consigna hasta que dice «terminé» |
| Errores de navegación | Clics o pulsaciones sobre elementos que no llevan a la tarea, desplazamientos horizontales o retrocesos para buscar algo |
| Solicitudes de ayuda | Cada vez que pregunta al moderador o recibe una pista |
| Éxito | **S** si dijo bien la hora y el lugar, reservó y canceló sin ayuda · **P** si lo logró con ayuda · **N** si no lo logró |

## 4. Tabla de observación

| Part. | Grupo | Versión | Viewport | Tiempo (s) | Errores de navegación | Solicitudes de ayuda | Éxito (S/P/N) | Dificultades detectadas (citas textuales) |
| :---: | :---: | :---: | :---: | ---: | ---: | ---: | :---: | :--- |
| P-01 | | B | 360 × 800 | | | | | |
| P-02 | | B | 1366 × 768 | | | | | |
| P-03 | | A | 360 × 800 | | | | | |

> Opcional: P-03 hace la misma tarea con el **boceto A** (`prototipos/prototipo-A.html`) para comparar. El boceto A no permite reservar (el botón está deshabilitado), así que solo se mide si encuentra el horario y el estado de la reserva.

## 5. Lista de verificación durante la observación

| Comportamiento observado | P-01 | P-02 | P-03 |
| :--- | :---: | :---: | :---: |
| Encuentra el horario y el lugar sin desplazarse horizontalmente | | | |
| Lee el mensaje de estado después de reservar sin que se lo indiquen | | | |
| Nota que el botón de reservar quedó bloqueado («Ya tienes un lugar») | | | |
| Encuentra «Cancelar mi reserva» sin buscarlo | | | |
| Usa el teclado (Tab / Enter) en algún momento | | | |
| Pregunta si la reserva «se guardó» o si «funcionó» | | | |

## 6. Resumen (completar al final)

- Tiempo medio de la versión B: ______ s · Errores totales: ______ · Ayudas totales: ______
- Dificultad más repetida: ________________________________________________
- ¿Se confirma la hipótesis de la fase 1? (al confirmar o cancelar, el participante sabe el estado de su reserva sin buscarlo): **Sí / No / Parcial** — porque ________________________
