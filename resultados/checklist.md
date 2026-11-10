# APE 5 · Fase 2 · Observación con usuarios en aula

- **Grupo:** 5 · **Responsable del registro:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · rama `pruebas-informe` · Issue #4
- **Moderación y cronómetro:** Melany Saleth Cevallos Goyes (@SalyC15) · **Registro:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos)
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)
- **Fecha:** 10/11/2026 · **Lugar:** Laboratorio / Aula de clase FISEI

## 1. Preparación (antes de cada participante)

- [x] Abrir `src/index.html` en una **pestaña nueva** o ejecutar `ReservaAPI.reiniciar()` en la consola. La pantalla muestra «Aún no tienes una reserva.» y 12 cupos.
- [x] Fijar el viewport en DevTools (360 × 800 para móvil o 1366 × 768 para escritorio) con zoom al 100 %.
- [x] El participante es de **otro grupo** y no ha visto el prototipo previamente.
- [x] Tener el cronómetro en cero y no señalar la pantalla.

## 2. Consigna neutral (leída textualmente)

> «Necesitas asistir al taller del jueves. Averigua a qué hora y dónde se dicta, aparta un lugar y luego deshaz esa acción. Avísame cuando creas que terminaste.»

- No se mencionaron los nombres de los botones («Reservar», «Cancelar») ni su ubicación.
- Cuando un participante dudó en el Boceto A, se respondió primero: «¿Qué harías si estuvieras solo?», registrando la asistencia cuando fue necesaria.
- El tiempo inició al finalizar la lectura de la consigna y se detuvo cuando el participante indicó que había terminado.

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
| P-01 | G2 | B | 360 × 800 | 16 | 0 | 0 | S | Ninguna; leyó horario y lugar en orden y confirmó al instante («Ya salió en verde que tengo lugar»). |
| P-02 | G3 | B | 1366 × 768 | 13 | 0 | 0 | S | Ninguna; identificó las dos columnas y usó «Cancelar mi reserva» de inmediato. |
| P-03 | G1 | A | 360 × 800 | 35 | 2 | 1 | N | Desplazó horizontalmente buscando el estado («No aparece dónde está mi reserva y el botón no deja hacer clic»). |
| P-04 | G4 | B | 360 × 800 | 15 | 0 | 0 | S | Recorrió con Tab y Enter sin usar ratón; notó que el foco pasó directo a «Cancelar mi reserva». |

> Nota comparativa: P-03 realizó la consigna sobre el **boceto A** (`prototipos/prototipo-A.html`) como control experimental en móvil (360 × 800 px), evidenciando el impacto del desborde de +600 px y del botón deshabilitado.

## 5. Lista de verificación durante la observación

| Comportamiento observado | P-01 (B · 360) | P-02 (B · 1366) | P-03 (A · 360) | P-04 (B · 360) |
| :--- | :---: | :---: | :---: | :---: |
| Encuentra el horario y el lugar sin desplazarse horizontalmente | Sí | Sí | No | Sí |
| Lee el mensaje de estado después de reservar sin que se lo indiquen | Sí | Sí | No | Sí |
| Nota que el botón de reservar quedó bloqueado («Ya tienes un lugar») | Sí | Sí | No aplica | Sí |
| Encuentra «Cancelar mi reserva» sin buscarlo | Sí | Sí | No existe | Sí |
| Usa el teclado (Tab / Enter) en algún momento | No | Sí | No | Sí |
| Pregunta si la reserva «se guardó» o si «funcionó» | No | No | Sí | No |

## 6. Resumen

- Tiempo medio de la versión B: **14,7 s** (frente a **35,0 s** en el Boceto A, reducción del **58 %**) · Errores en versión B: **0** · Ayudas en versión B: **0**.
- Dificultad más repetida: En la versión B no se presentaron bloqueos; en el Boceto A (P-03) el desborde horizontal de +600 px ocultó el panel «Mi reserva» e impidió completar la tarea.
- ¿Se confirma la hipótesis de la fase 1? (al confirmar o cancelar, el participante sabe el estado de su reserva sin buscarlo): **Sí** — porque **3 de 3 participantes en la Versión B (100 %) verbalizaron el estado confirmado y cancelado inmediatamente gracias al cambio visual del resumen y al traslado automático del foco**.
