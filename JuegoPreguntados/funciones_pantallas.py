import pygame
import sys
from config import *
from colores import *
from funciones_generales import *

def mostrar_pantalla_ingreso_nombre(pantalla):
    """Muestra un rectangulo, en una pantalla alterna para ingresar el nombre del jugador y poder arrancar a responder las preguntas

    Args:
        pantalla (surface): pantalla alterna en negro, donde se mostrara el rectangulo para poner el nombre

    Returns:
        nombre (str): Retorna el nombre puesto por el jugador
    """
    global error
    global nombre
    input_box = pygame.Rect(312, 226, 393, 49)
    introduciendo_nombre = True
    

    while introduciendo_nombre:
        pantalla.fill(BLACK)
        text_surface = fuente.render("Introduce tu nombre:", True, WHITE)
        pantalla.blit(text_surface, (310, 200))
        pygame.draw.rect(pantalla, WHITE, input_box, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre.strip():
                        introduciendo_nombre = False
                        return nombre
                    else:
                        error = True
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < 35:
                        nombre += event.unicode

        # Mostrar nombre en el cuadro de texto
        nombre_surface = fuente.render(nombre, True, WHITE)
        pantalla.blit(nombre_surface, (input_box.x + 5, input_box.y + 5))

        # Mostrar mensaje de error
        if error:
            error_surface = fuente.render("¡Debes ingresar un nombre!", True, ROJO)
            pantalla.blit(error_surface, (310, 300))

        pygame.display.flip()


def mostrar_pantalla_opciones(pantalla, fuente):
    global puntuacion, vidas, tiempo_restante

    tema_random = seleccionar_categoria(categorias)
    pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))
    opciones = pregunta["opciones"]
    respuesta_correcta = pregunta["respuesta_correcta"]
    dificultad = pregunta["dificultad"]

    tiempo_inicial = pygame.time.get_ticks()
    ultimo_tiempo = pygame.time.get_ticks()
    flag_correr = True

    while flag_correr:
        pantalla.blit(imagen_de_fondo_pantalla_opciones, (0, 0))

        # Mostrar la pregunta (extraer el texto)
        texto_de_pregunta = fuente.render(pregunta["pregunta"], True, BLACK)  # Se extrae el texto
        pantalla.blit(texto_de_pregunta, (50, 50))

        # Crear los botones de opciones
        botones = crear_botones(pantalla, fuente, (100, 150, 600, 50), WHITE, COLOR_HOVER,None, None, opciones)

        # Temporizador
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_tiempo >= 1000:
            tiempo_restante -= 1
            ultimo_tiempo = tiempo_actual

        texto_tiempo = fuente.render(f"Tiempo restante: {tiempo_restante}s", True, ROJO)
        pantalla.blit(texto_tiempo, (100, 20))

        texto_vidas = fuente.render(f"Vidas: {vidas}", True, ROJO)
        pantalla.blit(texto_vidas, (15, 20))

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for boton in botones:
                    if boton[0].collidepoint(event.pos):
                        if boton[1] == respuesta_correcta:
                            # Respuesta correcta
                            match dificultad:
                                case "Facil":
                                    puntuacion += 1
                                case "Intermedio":
                                    puntuacion += 3
                                case "Dificil":
                                    puntuacion += 6
                            print("¡Correcto!")
                        else:
                            # Respuesta incorrecta
                            print("¡Incorrecto!")
                            vidas -= 1

                        actualizar_estadisticas_preguntas(pregunta["pregunta"], respuesta_correcta, boton[1])

                        guardar_ranking("ranking.csv", puntuacion, nombre)

                        # Actualizar o terminar el juego
                        if vidas > 0:
                            tema_random = seleccionar_categoria(categorias)
                            pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))
                            opciones = pregunta["opciones"]
                            respuesta_correcta = pregunta["respuesta_correcta"]
                            dificultad = pregunta["dificultad"]
                            tiempo_restante = 5
                        else:
                            flag_correr = False

        if tiempo_restante <= 0:
            vidas -= 1
            guardar_ranking("ranking.csv", puntuacion, nombre)
            print("Se te acabó el tiempo.")
            if vidas > 0:
                tema_random = seleccionar_categoria(categorias)
                pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))
                opciones = pregunta["opciones"]
                respuesta_correcta = pregunta["respuesta_correcta"]
                dificultad = pregunta["dificultad"]
                tiempo_restante = 5
            else:
                print("¡Fin del juego!")
                flag_correr = False

        pygame.display.flip()

    tiempo_final = pygame.time.get_ticks()
    duracion_partida = (tiempo_final - tiempo_inicial) / 1000
    print(f"La partida duró: {duracion_partida:.2f} segundos")
    guardar_ranking("ranking.csv", puntuacion, nombre, duracion_partida)

    guardar_estadisticas_preguntas_realizadas_csv()
    return puntuacion