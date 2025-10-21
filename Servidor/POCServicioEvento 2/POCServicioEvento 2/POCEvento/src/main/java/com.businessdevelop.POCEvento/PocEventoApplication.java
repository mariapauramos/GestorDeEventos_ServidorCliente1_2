package com.businessdevelop.POCEvento;

import com.businessdevelop.POCEvento.servicio.ServicioEvento;
import com.businessdevelop.POCEvento.model.EventoDeportivo;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.time.LocalDate;

@SpringBootApplication
public class PocEventoApplication {

	public static void main(String[] args) {
		SpringApplication.run(PocEventoApplication.class, args);

	}
}


