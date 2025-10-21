package com.businessdevelop.POCEvento.config;

import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;

@Configuration
@EnableWebSecurity

public class SecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        // Deshabilitar CSRF, necesario para APIs REST consumidas por clientes externos
        http.csrf().disable();

        // Configurar la autorización de las peticiones
        http.authorizeHttpRequests(auth -> auth
                // Permitir acceso a un endpoint público sin autenticación (ej. /publico/**)
                .requestMatchers("/publico/**").permitAll()
                // Requerir autenticación para cualquier otra petición
                .anyRequest().authenticated()
        );

        // Habilitar la autenticación básica (usuario:contraseña)
        http.httpBasic();

        // Construir y retornar el SecurityFilterChain
        return http.build();
    }


}
