package com.businessdevelop.POCEvento.servicio;
import com.businessdevelop.POCEvento.model.Evento;
import com.businessdevelop.POCEvento.model.EventoCultural;
import com.businessdevelop.POCEvento.model.EventoDeportivo;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class ServicioEvento {

    private List<Evento> eventos = new ArrayList<>();

    public Evento crearEvento(Evento evento) {
        boolean existe = eventos.stream()
                .anyMatch(e -> e.getIdEvento().equalsIgnoreCase(evento.getIdEvento()));

        if (existe) {
            throw new IllegalArgumentException("Ya existe un evento con id: " + evento.getIdEvento());
        }

        eventos.add(evento);
        return evento;
    }


    public Optional<Evento> buscarEvento(String idEvento) {
        return eventos.stream()
                .filter(e -> e.getIdEvento().equalsIgnoreCase(idEvento))
                .findFirst();
    }

    public List<Evento> listarEventos() {
        return eventos;
    }

    public List<EventoDeportivo> listarED() {
        return eventos.stream()
                .filter(e -> e instanceof EventoDeportivo)
                .map(e -> (EventoDeportivo) e)
                .toList();
    }

    public List<EventoCultural> listarEC() {
        return eventos.stream()
                .filter(e -> e instanceof EventoCultural)
                .map(e -> (EventoCultural) e)
                .toList();
    }

    public List<EventoDeportivo> listarFiltroED(String ciudad, String tipoDeporte) {
        return listarED().stream()
                .filter(e -> {
                    if (ciudad == null && tipoDeporte == null) return false;
                    if (ciudad != null && tipoDeporte == null)
                        return e.getCiudad().equalsIgnoreCase(ciudad);
                    else if (tipoDeporte != null && ciudad == null)
                        return e.getTipoDeporte().equalsIgnoreCase(tipoDeporte);
                    else
                        return e.getCiudad().equalsIgnoreCase(ciudad)
                                && e.getTipoDeporte().equalsIgnoreCase(tipoDeporte);
                })
                .collect(Collectors.toList());
    }

    public List<EventoCultural> listarFiltroEC(String tipoCultura, String artistaPrincipal) {
        return listarEC().stream()
                .filter(e -> {
                    if (tipoCultura == null && artistaPrincipal == null) return false;
                    if (tipoCultura != null && artistaPrincipal == null)
                        return e.getTipoCultura().equalsIgnoreCase(tipoCultura);
                    else if (artistaPrincipal != null && tipoCultura == null)
                        return e.getArtistaPrincipal().equalsIgnoreCase(artistaPrincipal);
                    else
                        return e.getTipoCultura().equalsIgnoreCase(tipoCultura)
                                && e.getArtistaPrincipal().equalsIgnoreCase(artistaPrincipal);
                })
                .collect(Collectors.toList());
    }

    public boolean actualizarEvento(String idEvento, Evento eventoActualizado) {
        for (Evento e : eventos) {
            if (e.getIdEvento().equalsIgnoreCase(idEvento)) {
                if (e.getClass() != eventoActualizado.getClass()) {
                    throw new IllegalArgumentException("El tipo de evento no coincide");
                }

                e.setNombre(eventoActualizado.getNombre());
                e.setCiudad(eventoActualizado.getCiudad());
                e.setAsistentes(eventoActualizado.getAsistentes());
                e.setFecha(eventoActualizado.getFecha());
                e.setValorEntrada(eventoActualizado.getValorEntrada());

                if (e instanceof EventoDeportivo edOriginal && eventoActualizado instanceof EventoDeportivo edNuevo) {
                    edOriginal.setTipoDeporte(edNuevo.getTipoDeporte());
                } else if (e instanceof EventoCultural ecOriginal && eventoActualizado instanceof EventoCultural ecNuevo) {
                    ecOriginal.setTipoCultura(ecNuevo.getTipoCultura());
                    ecOriginal.setArtistaPrincipal(ecNuevo.getArtistaPrincipal());
                }

                return true;
            }
        }
        return false;
    }


    public boolean eliminarEvento(String idEvento) {
        return eventos.removeIf(e -> e.getIdEvento().equalsIgnoreCase(idEvento));
    }
}
