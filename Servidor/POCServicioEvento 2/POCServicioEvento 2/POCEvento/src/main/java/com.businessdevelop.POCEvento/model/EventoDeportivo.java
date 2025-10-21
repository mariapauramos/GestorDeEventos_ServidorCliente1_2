package com.businessdevelop.POCEvento.model;

import lombok.*;

import java.time.LocalDate;

/**
 *
 * @author mariaramos
 */
@Data
@NoArgsConstructor
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
public class EventoDeportivo extends Evento {

    private String tipoDeporte;

    public EventoDeportivo(String idEvento, String nombre, String ciudad, int asistentes,
                           LocalDate fecha, double valorEntrada, String tipoDeporte) {
        super(idEvento, nombre, ciudad, asistentes, fecha, valorEntrada);
        this.tipoDeporte = tipoDeporte;
    }

    // Método para calcular el valor del evento para cualquier persona (valor entrada + IVA (19%))
    @Override
    public double calcularValor() {

        return getValorEntrada() * 1.19;
    }
}