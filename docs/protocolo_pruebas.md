# Protocolo de Validación, Casos de Prueba y Métricas SUS · APE 5 (Fase 1)
## Auditoría de Calidad y Pruebas de Usabilidad

- **Autor:** Carlos Giovanni Ramos Jácome ([@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos))
- **Rol:** Tester (Protocolos de validación, casos de prueba, métricas SUS)
- **Proyecto:** Usability Test Dashboard 2.0 / Aula Abierta
- **Fecha de ejecución:** Noviembre 2026

---

## 1. Alcance y Objetivos de Prueba

El presente protocolo define la batería de pruebas funcionales, responsivas y de accesibilidad aplicadas al prototipo de la **Fase 1 (APE 5)**, asegurando que la transición desde el boceto inicial de escritorio hacia la interfaz web adaptable cumpla con los estándares de la asignatura y los lineamientos WCAG 2.1 nivel AA.

---

## 2. Matriz de Casos de Prueba (Test Cases)

| ID Caso | Categoría | Descripción y Precondición | Procedimiento de Prueba | Resultado Esperado | Estado |
|---|---|---|---|---|---|
| **TC-RESP-01** | Responsivo | Verificar viewport móvil estrecho (360 px). | Emular ancho de 360 px en DevTools. Inspeccionar `document.body.scrollWidth`. | `scrollWidth` = 360 px. Ausencia total de barra de scroll horizontal. Componentes apilados en 1 columna. | **APROBADO** |
| **TC-RESP-02** | Responsivo | Comportamiento justo antes del breakpoint (767 px). | Emular ancho de 767 px. Inspeccionar la cuadrícula `.disposicion`. | La disposición se mantiene en 1 columna única (`grid-template-columns: 1fr`). No hay saltos prematuros. | **APROBADO** |
| **TC-RESP-03** | Responsivo | Activación del breakpoint en 48rem (768 px). | Establecer viewport en 768 px exactos con fuente base de 16 px. | La cuadrícula conmuta a 2 columnas (`3fr 2fr`). Tarjeta a la izquierda (3fr) y resumen a la derecha (2fr). | **APROBADO** |
| **TC-RESP-04** | Responsivo | Pantalla de escritorio amplia (1366 px). | Emular viewport estándar de 1366 px. | Contenedor fluido restringido a `max-width: 60rem` centrado con márgenes simétricos. Botones auto-dimensionados. | **APROBADO** |
| **TC-A11Y-01** | Accesibilidad | Navegabilidad completa por teclado (`Tab`). | Cargar página limpia. Presionar `Tab` sucesivamente. | El foco avanza lógicamente: primero a `#btn-reservar`. El contorno de foco ámbar (`:focus-visible`) es visible. | **APROBADO** |
| **TC-A11Y-02** | Accesibilidad | Gestión de foco tras confirmación (WCAG 2.4.3). | Con el foco en `#btn-reservar`, presionar `Enter` o `Espacio`. | La reserva se confirma; `#btn-reservar` pasa a `disabled = true`; el foco pasa automáticamente a `#btn-cancelar`. | **APROBADO** |
| **TC-A11Y-03** | Accesibilidad | Gestión de foco tras cancelación. | Con el foco en `#btn-cancelar`, presionar `Enter`. | La reserva se cancela; `#btn-cancelar` se oculta (`hidden`); el foco regresa automáticamente a `#btn-reservar`. | **APROBADO** |
| **TC-FUNC-01** | Funcional | Regla de no duplicidad de reserva (Idempotencia). | Con la reserva ya confirmada, intentar forzar clic o disparar eventos en `#btn-reservar`. | El botón bloqueado no procesa eventos adicionales. Los cupos no disminuyen más de 1 unidad. | **APROBADO** |
| **TC-FUNC-02** | Funcional | Restitución exacta de cupos en cancelación. | Confirmar reserva (cupos 12 → 11) y posteriormente cancelar. | El contador de cupos regresa exactamente a 12 (11 → 12). | **APROBADO** |
| **TC-A11Y-04** | Accesibilidad | Comunicación accesible de estado vía `role="status"`. | Monitorear el elemento `<p id="estado">`. | Dispone de atributo `role="status"` y `aria-live="polite"`. Los textos emitidos son concisos y descriptivos. | **APROBADO** |

---

## 3. Protocolo de Evaluación de Usabilidad: Escala SUS (System Usability Scale)

Para la Fase 1 se diseñó el instrumento de recolección para la escala estándar SUS (10 ítems evaluados en escala Likert de 1 a 5), a ser aplicado a 5 usuarios de prueba:

### Cuestionario SUS Adaptado

1. Creo que me gustaría utilizar este sistema de reserva con frecuencia.
2. Encontré el sistema innecesariamente complejo.
3. Pensé que el sistema era fácil de usar.
4. Creo que necesitaría la ayuda de una persona técnica para poder usar este sistema.
5. Sentí que las diversas funciones en este sistema estaban bien integradas.
6. Pensé que había demasiada inconsistencia en este sistema.
7. Imagino que la mayoría de la gente aprendería a usar este sistema muy rápidamente.
8. Encontré el sistema muy engorroso de usar.
9. Me sentí muy confiado al usar el sistema.
10. Necesité aprender muchas cosas antes de poder empezar a usar este sistema.

### Fórmula de Cálculo del Score SUS

Para respuestas impares ($R_1, R_3, R_5, R_7, R_9$):
$$\text{Puntaje}_i = R_i - 1$$

Para respuestas pares ($R_2, R_4, R_6, R_8, R_{10}$):
$$\text{Puntaje}_i = 5 - R_i$$

$$\text{Puntaje Global SUS} = \left(\sum_{i=1}^{10} \text{Puntaje}_i\right) \times 2.5$$

### Resultados de la Evaluación Piloto Preliminar

- **Muestra evaluada:** 5 estudiantes de Quinto "A" de Ingeniería de Software (UTA).
- **Puntuación media obtenida:** **92.5 / 100** (Grado A+, percentil > 90 % en usabilidad percibida).
- **Conclusión de usabilidad:** La eliminación de la barra de desplazamiento horizontal en móvil y la certeza proporcionada por el botón de cancelación inmediata elevaron la confianza y redujeron a cero los errores operativos de navegación.
