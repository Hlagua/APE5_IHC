/**
 * APE 5 · Controlador de interacción y gestión accesible del foco (src/interaccion.js)
 * Desarrollado por: Melany Saleth Cevallos Goyes (@SalyC15)
 * Rol: Desarrollador Front-End (Vistas, componentes UI, diseño, wizard)
 *
 * Integra la lógica UI con la API desarrollada por Alison Marcela Cobos Taco.
 * Gestiona los tres momentos de la tarea (Disponible → Confirmada → Cancelada),
 * garantiza el bloqueo de doble reserva y traslada automáticamente el foco
 * de teclado para cumplimiento estricto de accesibilidad WCAG 2.4.3.
 */

document.addEventListener("DOMContentLoaded", () => {
  const btnReservar = document.getElementById("btn-reservar");
  const btnCancelar = document.getElementById("btn-cancelar");
  const estado = document.getElementById("estado");
  const resumen = document.querySelector(".resumen");
  const cupos = document.getElementById("cupos");

  const TALLER_TEXTO = "Interfaces web accesibles · jueves de 14:00 a 16:00 · Laboratorio 2";

  // Verificar si la capa de API de Alison (@Itsuna18) está disponible
  const api = window.ReservaAPI || null;

  // PREVENCIÓN DE ERRORES (Nielsen H5) · Hallazgo H-01 de la fase 2:
  // al confirmar, el foco pasa a «Cancelar»; un segundo Enter accidental
  // (doble pulsación) cancelaba la reserva recién hecha. Durante este margen
  // el botón Cancelar ignora activaciones.
  const MARGEN_DOBLE_PULSACION_MS = 600;
  let cancelarBloqueadoHasta = 0;

  /**
   * Actualiza la interfaz visual y la región accesible según el nuevo estado
   * @param {string} nuevoEstado - 'disponible' | 'confirmada' | 'cancelada'
   * @param {string} [mensajePersonalizado] - Mensaje devuelto por la API
   */
  function pintar(nuevoEstado, mensajePersonalizado) {
    resumen.dataset.estado = nuevoEstado;

    if (nuevoEstado === "confirmada") {
      estado.textContent = mensajePersonalizado || `Reserva confirmada: ${TALLER_TEXTO}.`;
      btnReservar.disabled = true; // Bloquea una segunda reserva (idempotencia)
      btnReservar.textContent = "Ya tienes un lugar";
      btnCancelar.hidden = false;
    } else {
      estado.textContent =
        mensajePersonalizado ||
        (nuevoEstado === "cancelada"
          ? "Cancelaste tu reserva. El lugar vuelve a estar disponible."
          : "Aún no tienes una reserva.");
      btnReservar.disabled = false;
      btnReservar.textContent = "Reservar un lugar";
      btnCancelar.hidden = true;
    }
  }

  // Sincronizar estado inicial desde API si existe persistencia
  if (api) {
    const estadoInicial = api.obtenerEstado();
    if (cupos && estadoInicial.cuposDisponibles !== undefined) {
      cupos.textContent = estadoInicial.cuposDisponibles;
    }
    if (estadoInicial.estado === 'confirmada') {
      pintar('confirmada');
    }
  }

  // Evento: Confirmar reserva
  btnReservar.addEventListener("click", () => {
    if (resumen.dataset.estado === "confirmada") return;

    if (api) {
      const res = api.confirmarReserva();
      if (!res.exito) return;
      cupos.textContent = res.cuposDisponibles;
      pintar("confirmada", res.mensaje);
    } else {
      cupos.textContent = Number(cupos.textContent) - 1;
      pintar("confirmada");
    }

    // GESTIÓN DE FOCO ACCESIBLE (WCAG 2.4.3):
    // Como btnReservar queda disabled, el foco de teclado se mueve explícitamente
    // a la siguiente acción lógica disponible (btnCancelar).
    cancelarBloqueadoHasta = performance.now() + MARGEN_DOBLE_PULSACION_MS;
    btnCancelar.focus();
  });

  // Evento: Cancelar reserva
  btnCancelar.addEventListener("click", () => {
    // Ignora la segunda pulsación de un doble Enter (ver hallazgo H-01).
    if (performance.now() < cancelarBloqueadoHasta) return;

    if (api) {
      const res = api.cancelarReserva();
      if (!res.exito) return;
      cupos.textContent = res.cuposDisponibles;
      pintar("cancelada", res.mensaje);
    } else {
      cupos.textContent = Number(cupos.textContent) + 1;
      pintar("cancelada");
    }

    // GESTIÓN DE FOCO ACCESIBLE (WCAG 2.4.3):
    // Como btnCancelar se oculta (hidden), el foco vuelve a btnReservar para
    // que el usuario no pierda su posición en la navegación por Tab.
    btnReservar.focus();
  });
});
