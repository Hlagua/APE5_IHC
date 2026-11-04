# PRÁCTICA EXPERIMENTAL DE APRENDIZAJE – APE 5
## Interacción Humano-Computador (IHC) · Quinto Semestre "A"
### Universidad Técnica de Ambato (UTA) · FISEI · Carrera de Ingeniería de Software

**Docente:** Ing. Mg. José Caiza  
**Repositorio GitHub:** [https://github.com/Hlagua/APE5_IHC](https://github.com/Hlagua/APE5_IHC)

---

## Integrantes del equipo y roles oficiales

| N.º | Integrante | Usuario GitHub | Correo Electrónico | Rol Oficial en el Proyecto |
|:---:|---|---|---|---|
| **1** | **Alison Marcela Cobos Taco** | [@Itsuna18](https://github.com/Itsuna18) | `tacomarcelab@gmail.com` | **Desarrollador Back-End** (API, modelos, persistencia, endpoints) |
| **2** | **Melany Saleth Cevallos Goyes** | [@SalyC15](https://github.com/SalyC15) | `mcevallos8901@uta.edu.ec` | **Desarrollador Front-End** (Vistas, componentes UI, diseño, wizard) |
| **3** | **Carlos Giovanni Ramos Jácome** | [@carlitosgiovanniramos](https://github.com/carlitosgiovanniramos) | `carlos.giovanni.ramos.work@gmail.com` | **Tester** (Protocolos de validación, casos de prueba, métricas SUS) |
| **4** | **Henry Daniel Lagua Flores** | [@Hlagua](https://github.com/Hlagua) | `hlagua6116@uta.edu.ec` | **QA / Arquitecto** (Auditorías, motor IA, resiliencia, suite de tests) |

---

## Fases de la Práctica APE 5

| Fase | Directorio | Descripción y Estado |
|---|---|---|
| **Fase 1** | [`APE5_Fase1/`](APE5_Fase1/README.md) · [`src/`](src/) | **Del boceto a la interfaz web adaptable:** Diagnóstico de desborde a 360 px, estructura semántica HTML5, diseño CSS Mobile-First (48rem / 768 px) e interacción de reserva accesible por teclado. |
| **Fase 2** | `APE5_Fase2/` *(Próxima)* | Validación empírica con lectores de pantalla (NVDA / TalkBack) y pruebas de usabilidad en profundidad. |

---

## Entregables de la Fase 1

### 1. Código Fuente y Prototipo Funcional
- **Página principal interactiva:** [`src/index.html`](src/index.html) (también accesible en [`APE5_Fase1/src/index.html`](APE5_Fase1/src/index.html))
- **Estilos Mobile-First:** [`src/estilos.css`](src/estilos.css) (Breakpoint en `48rem` / `768px`)
- **Controlador de interacción UI:** [`src/reserva.js`](src/reserva.js) (Disponible → Confirmada → Cancelada con gestión de foco)
- **Capa de persistencia y API simulada:** [`src/api.js`](src/api.js) (Validación de cupos e idempotencia)
- **Suite de pruebas de usabilidad:** [`tests/test_runner.html`](tests/test_runner.html) (Ejecutable directamente en navegador)

### 2. Documentación y Ficha Técnica
- **Ficha de aplicación al proyecto:** [`docs/proyecto.md`](docs/proyecto.md)
  - Diagnóstico técnico del Boceto A a 360 px (pérdida de «Mi reserva» y 600 px de desborde).
  - Secuencia de la tarea: Actor → Tarea → Dato decisivo → Acción principal → Estado final (para el proyecto grupal *Usability Test Dashboard 2.0* y para el caso de clase *Aula Abierta*).
  - Reglas de negocio y criterios de aceptación medibles (Gherkin: Dado / Cuando / Entonces).
  - Justificación de decisiones HCI (Nielsen H1, H3, H6 y WCAG 1.4.10, 2.1.1, 2.4.3, 2.5.5).
  - Hipótesis y métricas para la Fase 2.
- **Protocolo de pruebas y métricas SUS:** [`docs/protocolo_pruebas.md`](docs/protocolo_pruebas.md) (Casos TC-01 a TC-10, fórmula SUS y score 92.5/100).

### 3. Evidencias Visuales y Capturas
- Carpeta de capturas: [`04_capturas/`](04_capturas/)
  - `boceto-A-360.png`: Boceto inicial a 360 px evidenciando el recorte horizontal del panel de estado.
  - `movil-360-disponible.png`: Prototipo en móvil a 360 px (columna única fluida sin scroll horizontal).
  - `movil-360-confirmada.png`: Prototipo en móvil a 360 px con reserva confirmada y foco trasladado.
  - `movil-360-cancelada.png`: Prototipo en móvil a 360 px tras cancelar la reserva.
  - `escritorio-768-confirmada.png`: Punto de corte exacto a 768 px (48rem) con 2 columnas.
  - `escritorio-1366-confirmada.png`: Vista en pantalla ancha de escritorio a 1366 px.

### 4. Documentos de Entrega Formal
- Carpeta de documentos: [`06_documento/`](06_documento/)
  - **Documento corto para Moodle («Archivos enviados»):** `APE5_Fase1_Entrega.pdf` y `APE5_Fase1_Entrega.docx` (Ficha técnica, 2 capturas preliminares e hipótesis de Fase 2).
  - **Informe formal UTA:** `APE5_Fase1_AulaAbierta.pdf` y `APE5_Fase1_AulaAbierta.docx` (Formato institucional de Guía Práctica).

---

## Cómo Ejecutar el Proyecto

### Opción A: Abrir directamente en el navegador
Haga doble clic en el archivo [`src/index.html`](src/index.html) para explorar el prototipo interactivo, o en [`tests/test_runner.html`](tests/test_runner.html) para correr la suite de pruebas automatizadas.

### Opción B: Mediante servidor HTTP local (Python)
```bash
# Iniciar servidor local en el puerto 8765
python -m http.server 8765 --directory src

# En el navegador, abrir:
http://localhost:8765
```

---

## Política de Commits y Trazabilidad

Los commits de este repositorio han sido registrados con autoría individual explícita según la naturaleza técnica de la tarea:
- **Melany Saleth Cevallos Goyes (`@SalyC15`):** Maquetación HTML5 semántica, cuadrícula CSS Mobile-First y controladores UI.
- **Alison Marcela Cobos Taco (`@Itsuna18`):** Modelo de datos, capa de persistencia y simulación de API REST.
- **Carlos Giovanni Ramos Jácome (`@carlitosgiovanniramos`):** Protocolos de prueba, verificación responsiva y métricas SUS.
- **Henry Daniel Lagua Flores (`@Hlagua`):** Arquitectura del sistema, auditorías de calidad y documentación de entrega formal.
