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
            elif tema_seleccionado:
                tema_seleccionado = elegir_categoria_aleatoria(preguntas[categoria])
                pregunta_actual = None
                if pregunta_actual:
                    opciones = pregunta_actual["opciones"]
                    respuesta = pregunta_actual["respuesta"]
            print(tema_seleccionado)
        # Aquí iría la lógica del juego
        pygame.display.flip()
            
    pygame.quit()
pantalla_principal_juego()
    
