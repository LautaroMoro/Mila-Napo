import pygame
from funciones_generales import *
from config import *
pygame.init()
input_box, boton_rect = mostrar_pantalla_inicio(pantalla, fuente)
def pantalla_principal_juego():
    tema_random = None
    introducir_nombre = True
    flag_correr = True
    while flag_correr:
        # Dibujar el fondo
        pantalla.blit(imagen_de_fondo, (0, 0))
        crear_boton_arranque(pantalla, "Empezar", 200, 450, 350, 50, COLOR_NORMAL, COLOR_HOVER, empezar_juego)
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
                pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))
                tiempo_respuestas  # Selecciona una pregunta
                opciones = pregunta['opciones']
                respuesta_correcta = pregunta['respuesta_correcta']
                botones = crear_botones_opciones(pantalla, [pregunta["pregunta"]], fuente, config.WHITE,(100, 50), (600, 50), opciones, tiempo_respuestas)
            
                
        # Aquí iría la lógica del juego
        pygame.display.flip()
    pygame.quit()
pantalla_principal_juego()
