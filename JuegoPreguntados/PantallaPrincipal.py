import pygame
from config import *
from funciones_generales import *
from colores import *
from funciones_pantallas import *
import time

pygame.init()
def pantalla_principal_juego():
    global puntuacion
    global vidas
    global error
    global nombre
    global cambiar_ingreso_nombre
    global ultimo_tiempo
    global  tiempo_restante
    tema_random = None
    flag_correr = True
    tiempo_inicial = None
    while flag_correr:
        # Dibujar el fondo
        pantalla.blit(imagen_de_fondo, (0, 0))
        crear_botones(pantalla, "Empezar", fuente, (200, 450, 350, 50), COLOR_NORMAL, COLOR_HOVER, empezar_juego)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not cambiar_ingreso_nombre:
                    if event.button == 1:
                        cambiar_ingreso_nombre = True

            elif tema_random is None:
                tema_random = seleccionar_categoria(categorias)
                pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))  # Selecciona una pregunta
                opciones = pregunta['opciones']
                respuesta_correcta = pregunta['respuesta_correcta']
                dificultad = ["dificultad"]
                botones = crear_botones(pantalla, [pregunta["pregunta"]], fuente,(100, 50, 600, 50), WHITE, COLOR_HOVER, opciones)

        if cambiar_ingreso_nombre:
            nombre = mostrar_pantalla_ingreso_nombre(pantalla)
            if nombre.strip():
                cambiar_ingreso_nombre = False
                tiempo_restante = 15
                tiempo_inicial = pygame.time.get_ticks()
                ultimo_tiempo = pygame.time.get_ticks()
            else:
                error = True
        else:
            for boton in botones:
                    if boton[0].collidepoint(event.pos):
                        if boton[1] == respuesta_correcta:
                            match dificultad:
                                case "Facil":
                                    print("correcto!")
                                    #SONIDO ACA
                                    puntuacion += 1
                                case "Intermedio":
                                    print("correcto")
                                    #SONIDO ACA
                                    puntuacion += 3
                                case "Dificil":
                                    #SONIDO ACA
                                    print("CORRECTOO, estaba dificil esa eh")
                                    puntuacion += 6
                            guardar_ranking("ranking.csv", puntuacion, nombre, duracion_partida)
                        else:
                            #SONIDO ACA
                            print("Incorrecto")
                            vidas -= 1
                            guardar_ranking("ranking.csv", puntuacion, nombre, duracion_partida)
            
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - ultimo_tiempo >= 1000:
                tiempo_restante -= 1
                ultimo_tiempo = tiempo_actual
            texto_tiempo = fuente.render(f"Tiempo restante: {tiempo_restante}", True, BLACK)
            pantalla.blit(texto_tiempo, (20, 20))


            if tiempo_restante <= 0 and vidas != 0:
                vidas -= 1
                print("se te resto una vida por no contestar la pregunta")
            elif tiempo_restante <= 0 and vidas == 0:
                flag_correr = False

        pygame.display.flip()

    tiempo_final = pygame.time.get_ticks()
    duracion_partida = (tiempo_final - tiempo_inicial) / 1000  # Tiempo en segundos
    print(f"La partida duró: {duracion_partida:.2f} segundos")

    # Guardar el tiempo en el ranking
    guardar_ranking("ranking.csv", puntuacion, nombre, duracion_partida)

        # Aquí iría la lógica del juego
    pygame.quit()
pantalla_principal_juego()
