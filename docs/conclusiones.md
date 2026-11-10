# APE 5 · Conclusiones finales

- **Grupo:** 5 · **Responsable:** Carlos Giovanni Ramos Jácome (@carlitosgiovanniramos) · rama `pruebas-informe` · Issue #4
- **Revisión cruzada:** Henry Daniel Lagua Flores (@Hlagua)

## 1. Requisito

Una estudiante debe poder, **desde su teléfono**, consultar el horario y el lugar de un taller, reservar un lugar, comprobar que la reserva quedó hecha y deshacerla, sin desplazarse horizontalmente y usando solo el teclado si lo necesita. En el proyecto del grupo (**Usability Test Dashboard 2.0**), el equivalente es el requisito **RF-OBS-01**: registrar el desempeño de un participante en una tarea y recibir confirmación accesible inmediata de si el envío al backlog se completó.

## 2. Decisión

Cambiamos la cuadrícula fija de 960 px del boceto A por un diseño **Mobile-First**:
- HTML5 semántico en el orden lógico de la tarea: `<article>` con el dato decisivo en un `<dl>` y la acción principal, seguido de `<section>` con el estado (`role="status"`) y la acción de deshacer.
- Una columna por defecto (`grid-template-columns: 1fr`) y dos columnas (`3fr 2fr`) solo desde `@media (min-width: 48rem)`, sin reordenar el DOM con `order`.
- Tres estados explícitos (`disponible → confirmada → cancelada`). Al confirmar, `disabled` bloquea la segunda reserva, el foco pasa siempre al control que sigue disponible (`btnCancelar.focus()` / `btnReservar.focus()`) y un margen de `600 ms` protege contra el doble `Enter` accidental.

## 3. Dato observado

- **En el laboratorio (medido):** `0 px` de desborde horizontal (`scrollWidth == innerWidth`) en `320`, `360`, `768` y `1366 px`, frente a `+640`, `+600` y `+192 px` del boceto A en los tres primeros anchos. El cambio de columnas ocurre exactamente entre `767` y `768 px`. Con teclado, `Tab → Enter` reserva y deja el foco en «Cancelar»; cinco intentos forzados sobre el botón deshabilitado no descuentan otro cupo (`resultados/pruebas.md`).
- **Hallazgo propio corregido (H-01):** un doble `Enter` rápido reservaba y cancelaba al instante. Con un margen de `600 ms` en «Cancelar» (`MARGEN_DOBLE_PULSACION_MS`), el doble `Enter` ahora mantiene la reserva confirmada con 11 cupos y las 9 pruebas automatizadas (`tests/test_runner.html`) pasan al 100 % (9/9).
- **Con personas en aula (`resultados/checklist.md`):** con 4 participantes evaluados mediante consigna neutral, en la **Versión B** (P-01, P-02, P-04) el tiempo medio fue de **14,7 s**, con **0 errores de navegación**, **0 solicitudes de ayuda** y **100 % de éxito** (reducción del **58 %** en tiempo respecto a los **35,0 s**, **2 errores** y **1 ayuda** registrados en el Boceto A con P-03).

## 4. Limitación

- La muestra observada en aula (4 participantes) es representativa para validación formativa pero **preliminar** a nivel estadístico, y se ejecutó en el entorno controlado de laboratorio.
- Aunque el atributo `role="status"` y `aria-live="polite"` está verificado en el DOM y en la suite automática, falta completar sesiones con usuarios ciegos o de baja visión utilizando lectores de pantalla reales (**NVDA** en escritorio y **TalkBack / VoiceOver** en teléfonos físicos).
- El estado se persiste actualmente en `sessionStorage` del navegador local: no existe aún un backend centralizado con bloqueo transaccional en base de datos para concurrencia multiusuario en tiempo real.
- El ajuste geométrico (`0 px` de desborde) es condición necesaria pero no suficiente por sí solo: como demostró nuestra medición del Boceto A en emulación móvil (`scale = 0,375`, texto de `6,8 px`), encajar en pantalla sin jerarquía ni legibilidad no produce comprensión.

## 5. Siguiente iteración

1. Ampliar las pruebas con **al menos 5 participantes en teléfonos físicos reales** activando **TalkBack (Android)** y **NVDA (Windows)**, validando que al menos 4 de 5 verbalicen el estado anunciado por `role="status"` sin asistencia visual.
2. Conectar `src/api.js` a un endpoint REST real en servidor con control de concurrencia atómico de cupos, manteniendo `disabled` y la guarda de `600 ms` como primera línea de prevención en el cliente.
3. Transferir íntegramente este patrón validado (*Dato clave en `<dl>` → Acción con bloqueo y guarda → Estado en `role="status"` → Acción de reversión con traslado de foco*) a la pantalla «Bitácora de observaciones» (`/dashboard/test-plan/record`) de **Usability Test Dashboard 2.0**.
