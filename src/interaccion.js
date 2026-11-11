/**
 * APE 5 · CaféU · Controlador de interacción de «Mi pedido»
 * Responsable: Alison Marcela Cobos Taco (@Itsuna18)
 *
 * Tres momentos de la acción: Pendiente → Confirmado → Cancelado (reversible).
 * - Al confirmar: bloquea el doble cobro (disabled), anuncia el resultado en
 *   role="status" y traslada el foco a «Cancelar pedido».
 * - Al cancelar: devuelve el dinero, oculta «Cancelar» y devuelve el foco a
 *   «Confirmar y pagar».
 */
document.addEventListener('DOMContentLoaded', () => {
  const btnConfirmar = document.getElementById('btn-confirmar');
  const btnCancelar = document.getElementById('btn-cancelar');
  const estado = document.getElementById('estado');
  const resumen = document.querySelector('.resumen');
  const saldo = document.getElementById('saldo');
  const api = window.PedidoAPI;
  const D = api.datos;

  const dinero = (n) => '$' + n.toFixed(2);
  const TEXTO_CONFIRMAR = 'Confirmar y pagar · ' + dinero(D.total);

  // PREVENCIÓN DE ERRORES (Nielsen H5) · hallazgo H-01:
  // al confirmar, el foco pasa a «Cancelar pedido»; un segundo Enter accidental
  // (doble pulsación) cancelaría el pedido recién pagado. Durante este margen,
  // «Cancelar pedido» ignora activaciones.
  const MARGEN_DOBLE_PULSACION_MS = 600;
  let cancelarBloqueadoHasta = 0;

  function pintar(s) {
    resumen.dataset.estado = s.estado;
    saldo.textContent = dinero(s.saldo);

    if (s.estado === 'confirmado') {
      estado.textContent = 'Pedido ' + s.numero + ' confirmado y pagado (' + dinero(D.total) +
        '). Estará listo en unos ' + D.minutos + ' minutos en el ' + D.retiro + '.';
      btnConfirmar.disabled = true; // bloquea el doble cobro
      btnConfirmar.textContent = 'Pedido ' + s.numero + ' pagado';
      btnCancelar.hidden = false;
    } else {
      estado.textContent = s.estado === 'cancelado'
        ? 'Cancelaste el pedido ' + s.numero + '. Se devolvieron ' + dinero(D.total) + ' a tu tarjeta universitaria.'
        : 'Aún no confirmas tu pedido. No se ha cobrado nada.';
      btnConfirmar.disabled = false;
      btnConfirmar.textContent = TEXTO_CONFIRMAR;
      btnCancelar.hidden = true;
    }
  }

  // Estado inicial (la API lo conserva por pestaña en sessionStorage)
  pintar(api.obtenerEstado());

  btnConfirmar.addEventListener('click', () => {
    if (resumen.dataset.estado === 'confirmado') return;
    const r = api.confirmarPedido();
    if (!r.exito) return;
    pintar(r);
    // GESTIÓN DEL FOCO (WCAG 2.4.3): el botón pulsado queda disabled,
    // así que el foco pasa a la siguiente acción disponible.
    cancelarBloqueadoHasta = performance.now() + MARGEN_DOBLE_PULSACION_MS;
    btnCancelar.focus();
  });

  btnCancelar.addEventListener('click', () => {
    if (performance.now() < cancelarBloqueadoHasta) return; // H-01
    const r = api.cancelarPedido();
    if (!r.exito) return;
    pintar(r);
    // «Cancelar pedido» se oculta: el foco vuelve a «Confirmar y pagar».
    btnConfirmar.focus();
  });
});
