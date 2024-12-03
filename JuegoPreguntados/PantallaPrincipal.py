import pygame
from config import *
from funciones_generales import *
from colores import *
from funciones_pantallas import *
import time

pygame.init()
ultimo_tiempo = pygame.time.get_ticks()
def pantalla_principal_juego():
    global cambiar_ingreso_nombre
    global ultimo_tiempo
    global  tiempo_restante
    error = False
    introduciendo_nombre = True
    tema_random = None
    flag_correr = True
    while flag_correr:
        # Dibujar el fondo
        pantalla.blit(imagen_de_fondo, (0, 0))
        crear_botones(pantalla, "Empezar", fuente, (200, 450, 350, 50), COLOR_NORMAL, COLOR_HOVER, empezar_juego)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False

            elif tema_random is None:
                tema_random = seleccionar_categoria(categorias)
                pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))  # Selecciona una pregunta
                opciones = pregunta['opciones']
                respuesta_correcta = pregunta['respuesta_correcta']
                dificultad = ["dificultad"]
                botones = crear_botones(pantalla, [pregunta["pregunta"]], fuente,(100, 50, 600, 50), WHITE, COLOR_HOVER, opciones)

        if cambiar_ingreso_nombre:
            mostrar_pantalla_ingreso_nombre(pantalla, nombre)
            cambiar_ingreso_nombre = False
            introduciendo_nombre = True
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
                            guardar_ranking("ranking.csv", puntuacion, nombre, ultimo_tiempo)
                        else:
                            #SONIDO ACA
                            print("Incorrecto")
                            guardar_ranking("ranking.csv", puntuacion, nombre, ultimo_tiempo)
            else:
                tiempo_actual = time.time()
                if tiempo_actual - ultimo_tiempo >= 1000:
                    tiempo_restante -= 1
                    ultimo_tiempo = tiempo_actual
                texto_tiempo = fuente.render(f"Tiempo restante: {tiempo_restante}", True, BLACK)
                pantalla.blit(texto_tiempo, (20, 20))

        # Aquí iría la lógica del juego
        pygame.display.flip()
    pygame.quit()
pantalla_principal_juego()
