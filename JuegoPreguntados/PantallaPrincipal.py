import pygame
from funciones_generales import *
from config import *
pygame.init()

def pantalla_principal_juego():
    flag_correr = True
    while flag_correr:
        # Dibujar el fondo
        pantalla.blit(imagen_de_fondo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False

        # Aquí iría la lógica del juego
        pygame.display.flip()
            
    pygame.quit()
pantalla_principal_juego()
    