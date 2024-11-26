import pygame
from funciones_generales_2 import *
from config_2 import *
from prueba_2 import *
pygame.init()

def pantalla_principal_juego():
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
                    tema_random = seleccionar_categoria(categorias)  # Selecciona una categoría aleatoria
                    pregunta = seleccionar_pregunta(preguntas.get(tema_random, []))  # Selecciona una pregunta

                print(f"Tema seleccionado: {tema_random}")
                print(f"Pregunta: {pregunta}")
        
        # Aquí iría la lógica del juego
        pygame.display.flip()
            
    pygame.quit()
pantalla_principal_juego()
    
