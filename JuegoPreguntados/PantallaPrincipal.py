import pygame
from config import *
from funciones_generales import *
from colores import *
pygame.init()
input_box, boton_rect = mostrar_pantalla_inicio(pantalla, fuente)
def pantalla_principal_juego():
    tema_random = None
    introducir_nombre = True
    flag_correr = True
    while flag_correr:
        # Dibujar el fondo
        pantalla.blit(imagen_de_fondo, (0, 0))
        crear_botones(pantalla, "Empezar", fuente, (200, 450, 350, 50), COLOR_NORMAL, COLOR_HOVER, empezar_juego)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if introducir_nombre:
                    if nombre.strip() != "":
                        nombre_formateado = manejar_string(nombre.strip())
                        introducir_nombre = False
                    else:
                        error = False
            elif tema_random is None:
                tema_random = seleccionar_categoria(categorias)
                pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))  # Selecciona una pregunta
                opciones = pregunta['opciones']
                respuesta_correcta = pregunta['respuesta_correcta']
                tiempo_restante = temporizador_pregunta(15000)
                dificultad = ["dificultad"]
                print(f"tema aleatorio: {tema_random}")
                print(f"pregunta: {pregunta}")
                print(f"opciones: {opciones}")
                print(f" respuesta correcta: {respuesta_correcta}")
                botones = crear_botones(pantalla, [pregunta["pregunta"]], config.fuente,(100, 50, 600, 50), WHITE, COLOR_HOVER, opciones, tiempo_restante)
        else:
            for boton in botones:
                if boton[0].collidepoint(event.pos):
                    if boton[1] == respuesta_correcta :
                        match dificultad:
                            case "Facil":
                                print("correcto!")
                                puntuacion += 1
                            case "Intermedio":
                                print("correcto")
                                puntuacion += 3
                            case "Dificil":
                                print("CORRECTOO, estaba dificil esa eh")
                                puntuacion += 6

        # Aquí iría la lógica del juego
        pygame.display.flip()
    pygame.quit()
pantalla_principal_juego()
