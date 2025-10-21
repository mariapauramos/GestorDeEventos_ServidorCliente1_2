package com.businessdevelop.POCEvento.controller;

import com.businessdevelop.POCEvento.model.Evento;
import com.businessdevelop.POCEvento.model.EventoCultural;
import com.businessdevelop.POCEvento.model.EventoDeportivo;
import com.businessdevelop.POCEvento.servicio.ServicioEvento;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/eventos")
public class ControladorEvento {

    private final ServicioEvento servicioEvento;

    public ControladorEvento(ServicioEvento servicioEvento) {
        this.servicioEvento = servicioEvento;
    }

    @GetMapping("/healthCheck")
    public String healthCheck() {
        return "Status ok!";
    }

    @PostMapping("/ED")
    public ResponseEntity<?> crearED(@Valid @RequestBody EventoDeportivo evento) {
        try {
            return ResponseEntity.status(HttpStatus.CREATED).body(servicioEvento.crearEvento(evento));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).body(e.getMessage());
        }
    }

    @PostMapping("/EC")
    public ResponseEntity<?> crearEC(@Valid @RequestBody EventoCultural evento) {
        try {
            return ResponseEntity.status(HttpStatus.CREATED).body(servicioEvento.crearEvento(evento));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).body(e.getMessage());
        }
    }

    @GetMapping("/{idEvento}")
    public ResponseEntity<Evento> buscarEvento(@PathVariable String idEvento) {
        return servicioEvento.buscarEvento(idEvento)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/ED")
    public ResponseEntity<List<EventoDeportivo>> listarDeportivos() {
        return ResponseEntity.ok(servicioEvento.listarED());
    }

    @GetMapping("/EC")
    public ResponseEntity<List<EventoCultural>> listarCulturales() {
        return ResponseEntity.ok(servicioEvento.listarEC());
    }

    @GetMapping("/filtroED")
    public ResponseEntity<?> filtrarED(
            @RequestParam(required = false) String ciudad,
            @RequestParam(required = false) String tipoDeporte) {

        if (ciudad == null && tipoDeporte == null) {
            return ResponseEntity.badRequest()
                    .body("Debes ingresar al menos un filtro: ciudad o tipoDeporte");
        }
        return ResponseEntity.ok(servicioEvento.listarFiltroED(ciudad, tipoDeporte));
    }

    @GetMapping("/filtroEC")
    public ResponseEntity<?> filtrarEC(
            @RequestParam(required = false) String tipoCultura,
            @RequestParam(required = false) String artistaPrincipal) {

        if (tipoCultura== null && artistaPrincipal == null) {
            return ResponseEntity.badRequest()
                    .body("Debes ingresar al menos un filtro: tipoCultura o artistaPrincipal");
        }
        return ResponseEntity.ok(servicioEvento.listarFiltroEC(tipoCultura, artistaPrincipal));
    }

    @PutMapping("/ED/{idEvento}")
    public ResponseEntity<?> actualizarED(
            @PathVariable String idEvento,
            @RequestBody EventoDeportivo eventoActualizado) {
        boolean actualizado = servicioEvento.actualizarEvento(idEvento, eventoActualizado);
        return actualizado ? ResponseEntity.ok("Evento deportivo actualizado")
                : ResponseEntity.status(HttpStatus.NOT_FOUND).body("No encontrado");
    }

    @PutMapping("/EC/{idEvento}")
    public ResponseEntity<?> actualizarEC(
            @PathVariable String idEvento,
            @RequestBody EventoCultural eventoActualizado) {
        boolean actualizado = servicioEvento.actualizarEvento(idEvento, eventoActualizado);
        return actualizado ? ResponseEntity.ok("Evento cultural actualizado")
                : ResponseEntity.status(HttpStatus.NOT_FOUND).body("No encontrado");
    }

    @DeleteMapping("/{idEvento}")
    public ResponseEntity<?> eliminarEvento(@PathVariable String idEvento) {
        boolean eliminado = servicioEvento.eliminarEvento(idEvento);
        return eliminado ?
                ResponseEntity.ok("Evento eliminado correctamente") :
                ResponseEntity.status(HttpStatus.NOT_FOUND).body("Evento no encontrado");
    }
}
