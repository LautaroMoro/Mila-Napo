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
            if tema_random is None:
                tema_random = seleccionar_categoria(categorias)
                pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))  # Selecciona una pregunta
                opciones = pregunta['opciones']
                respuesta_correcta = pregunta['respuesta_correcta']
                print(f"Tema seleccionado: {tema_random}")
                print(f"Pregunta: {pregunta}")
                print(f"opciones {opciones}")
                print(f"respuesta_correcta {respuesta_correcta}")
                
        crear_boton(pantalla, "Empezar", 200, 450, 350, 50, COLOR_NORMAL, COLOR_HOVER, empezar_juego)
        # Aquí iría la lógica del juego
        pygame.display.flip()
    pygame.quit()
pantalla_principal_juego()
