package com.businessdevelop.POCEvento.model;
import lombok.*;

import java.time.LocalDate;

@Data
@NoArgsConstructor
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)

public class EventoCultural extends Evento {
    private String tipoCultura;
    private String artistaPrincipal;

    public EventoCultural(String idEvento, String nombre, String ciudad, int asistentes,
                           LocalDate fecha, double valorEntrada, String tipoCultura, String artistaPrincipal) {
        super(idEvento, nombre, ciudad, asistentes, fecha, valorEntrada);
        this.tipoCultura = tipoCultura;
        this.artistaPrincipal = artistaPrincipal;
    }

    @Override
    public double calcularValor() {
        return getValorEntrada() * 1.19;
    }
}
