/**
 * APE 5 · CaféU · Capa de datos simulada del pedido
 * Responsable: Alison Marcela Cobos Taco (@Itsuna18) · Desarrollador Back-End
 *
 * Simula el servicio de pedidos de CaféU (APE 4): confirmar y pagar, y cancelar
 * con devolución. Regla de negocio: un pedido se cobra una sola vez.
 * El estado se guarda en sessionStorage (por pestaña).
 */
(function (global) {
  'use strict';

  const STORAGE_KEY = 'ape5_cafeu_pedido_v1';
  const PEDIDO = {
    productos: [
      { nombre: 'Café Americano', precio: 1.50 },
      { nombre: 'Sánduche', precio: 2.75 }
    ],
    total: 4.25,
    retiro: 'Edificio central',
    minutos: 10,
    saldoInicial: 10.00,
    primerNumero: 24 // #A24, como en el prototipo del APE 4
  };

  const inicial = () => ({
    estado: 'pendiente', // pendiente | confirmado | cancelado
    saldo: PEDIDO.saldoInicial,
    numero: null,
    siguiente: PEDIDO.primerNumero,
    cobros: 0
  });

  function cargar() {
    try {
      const raw = sessionStorage.getItem(STORAGE_KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) { /* sin almacenamiento: estado en memoria */ }
    return inicial();
  }

  function guardar(datos) {
    try { sessionStorage.setItem(STORAGE_KEY, JSON.stringify(datos)); } catch (e) { /* sin almacenamiento */ }
  }

  const redondear = (n) => Math.round(n * 100) / 100;

  const PedidoAPI = {
    datos: PEDIDO,

    obtenerEstado: function () {
      return cargar();
    },

    /** Confirma y cobra. Rechaza un segundo cobro del mismo pedido y el saldo insuficiente. */
    confirmarPedido: function () {
      const s = cargar();
      if (s.estado === 'confirmado') {
        return { exito: false, motivo: 'ya_confirmado', ...s };
      }
      if (s.saldo < PEDIDO.total) {
        return { exito: false, motivo: 'saldo_insuficiente', ...s };
      }
      const nuevo = {
        ...s,
        estado: 'confirmado',
        saldo: redondear(s.saldo - PEDIDO.total),
        numero: '#A' + s.siguiente,
        siguiente: s.siguiente + 1,
        cobros: s.cobros + 1
      };
      guardar(nuevo);
      return { exito: true, ...nuevo };
    },

    /** Cancela el pedido confirmado y devuelve el total a la tarjeta. */
    cancelarPedido: function () {
      const s = cargar();
      if (s.estado !== 'confirmado') {
        return { exito: false, motivo: 'sin_pedido', ...s };
      }
      const nuevo = { ...s, estado: 'cancelado', saldo: redondear(s.saldo + PEDIDO.total) };
      guardar(nuevo);
      return { exito: true, ...nuevo };
    },

    /** Vuelve al estado inicial (usar entre un participante y otro). */
    reiniciar: function () {
      try { sessionStorage.removeItem(STORAGE_KEY); } catch (e) { /* sin almacenamiento */ }
      return inicial();
    }
  };

  global.PedidoAPI = PedidoAPI;
})(typeof window !== 'undefined' ? window : this);
