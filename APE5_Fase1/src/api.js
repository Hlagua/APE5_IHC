/**
 * APE 5 · Fase 1 · Capa de Persistencia y Simulación de Endpoints API
 * Desarrollado por: Alison Marcela Cobos Taco (@Itsuna18)
 * Rol: Desarrollador Back-End (API, modelos, persistencia, endpoints)
 *
 * Simula la capa de servicios REST y persistencia local para la gestión
 * de reservas de talleres y bitácora de observaciones.
 */

(function (global) {
  'use strict';

  // Configuración y estado inicial por defecto
  const TALLER_DEFAULT = {
    id: "taller-web-01",
    titulo: "Interfaces web accesibles",
    horario: "Jueves, 14:00 a 16:00",
    lugar: "Laboratorio 2",
    cuposTotales: 12,
    cuposDisponibles: 12
  };

  const STORAGE_KEY = 'ape5_reserva_estado_v1';

  /**
   * Servicio de datos y simulación de API REST
   */
  const ReservaAPI = {
    /**
     * Obtiene los datos del taller (Simula GET /api/talleres/:id)
     * @returns {Object} Datos del taller y cupos actuales
     */
    obtenerTaller: function () {
      const persistido = this._cargarEstado();
      return {
        ...TALLER_DEFAULT,
        cuposDisponibles: persistido.cuposDisponibles
      };
    },

    /**
     * Obtiene el estado actual de la reserva del usuario (Simula GET /api/reservas/mi-reserva)
     * @returns {Object} { estado: 'disponible'|'confirmada'|'cancelada', cuposDisponibles: number, fecha: string|null }
     */
    obtenerEstado: function () {
      return this._cargarEstado();
    },

    /**
     * Procesa la solicitud de reserva (Simula POST /api/reservas)
     * Regla de negocio: No se puede reservar si no hay cupos o si ya está confirmada.
     * @returns {Object} Resultado de la transacción
     */
    confirmarReserva: function () {
      const estadoActual = this._cargarEstado();

      if (estadoActual.estado === 'confirmada') {
        return {
          exito: false,
          mensaje: 'Ya cuentas con una reserva confirmada para este taller.',
          cuposDisponibles: estadoActual.cuposDisponibles
        };
      }

      if (estadoActual.cuposDisponibles <= 0) {
        return {
          exito: false,
          mensaje: 'No hay cupos disponibles para este taller.',
          cuposDisponibles: 0
        };
      }

      const nuevoEstado = {
        estado: 'confirmada',
        cuposDisponibles: estadoActual.cuposDisponibles - 1,
        fecha: new Date().toISOString()
      };

      this._guardarEstado(nuevoEstado);

      return {
        exito: true,
        mensaje: `Reserva confirmada: ${TALLER_DEFAULT.titulo} · ${TALLER_DEFAULT.horario} · ${TALLER_DEFAULT.lugar}.`,
        cuposDisponibles: nuevoEstado.cuposDisponibles,
        datos: nuevoEstado
      };
    },

    /**
     * Cancela la reserva activa (Simula DELETE /api/reservas/mi-reserva)
     * Regla de negocio: Libera exactamente 1 cupo y devuelve el estado a 'cancelada'.
     * @returns {Object} Resultado de la cancelación
     */
    cancelarReserva: function () {
      const estadoActual = this._cargarEstado();

      if (estadoActual.estado !== 'confirmada') {
        return {
          exito: false,
          mensaje: 'No existe una reserva activa para cancelar.',
          cuposDisponibles: estadoActual.cuposDisponibles
        };
      }

      const cuposRestituidos = Math.min(
        TALLER_DEFAULT.cuposTotales,
        estadoActual.cuposDisponibles + 1
      );

      const nuevoEstado = {
        estado: 'cancelada',
        cuposDisponibles: cuposRestituidos,
        fecha: new Date().toISOString()
      };

      this._guardarEstado(nuevoEstado);

      return {
        exito: true,
        mensaje: 'Cancelaste tu reserva. El lugar vuelve a estar disponible.',
        cuposDisponibles: nuevoEstado.cuposDisponibles,
        datos: nuevoEstado
      };
    },

    /**
     * Restablece los datos a su estado inicial
     */
    reiniciar: function () {
      try {
        sessionStorage.removeItem(STORAGE_KEY);
      } catch (e) {
        // En entornos sin storage permitido
      }
      return {
        estado: 'disponible',
        cuposDisponibles: TALLER_DEFAULT.cuposTotales,
        fecha: null
      };
    },

    // --- Métodos privados de persistencia ---
    _cargarEstado: function () {
      try {
        const raw = sessionStorage.getItem(STORAGE_KEY);
        if (raw) {
          return JSON.parse(raw);
        }
      } catch (e) {
        // Fallback en memoria si sessionStorage está bloqueado
      }
      return {
        estado: 'disponible',
        cuposDisponibles: TALLER_DEFAULT.cuposTotales,
        fecha: null
      };
    },

    _guardarEstado: function (datos) {
      try {
        sessionStorage.setItem(STORAGE_KEY, JSON.stringify(datos));
      } catch (e) {
        // Fallback silencioso
      }
    }
  };

  // Exponer al objeto global del navegador
  global.ReservaAPI = ReservaAPI;

})(typeof window !== 'undefined' ? window : this);
