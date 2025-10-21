package com.businessdevelop.POCEvento.model;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;
import java.time.LocalDate;

@Data
@NoArgsConstructor
@ToString
public abstract class Evento {

    private String idEvento;
    private String nombre;
    private String ciudad;
    private int asistentes;
    @JsonFormat(pattern = "yyyy-MM-dd")
    private LocalDate fecha;
    private double valorEntrada;

    public Evento(String idEvento, String nombre, String ciudad, int asistentes,
                  LocalDate fecha, double valorEntrada) {
        this.idEvento = idEvento;
        this.nombre = nombre;
        this.ciudad = ciudad;
        this.asistentes = asistentes;
        this.fecha = fecha;
        this.valorEntrada = valorEntrada;
    }

    public abstract double calcularValor();
}