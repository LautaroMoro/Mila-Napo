import pygame
from config import *
from funciones_generales import *
pygame.init()

def menu():
    flag_correr = True
    while flag_correr:
        pantalla.blit(imagen_de_fondo, (0, 0))
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:
                flag_correr = False

        if crear_boton("Game_assets/imagenes/Boton.webp", (coordenada_x_boton, coordenada_y_boton), (240, 60), (COLOR_CELESTE), funcion = None):
            print("Boton apretado")
        #BOTONES Y PANTALLAS ACÁ   
        pygame.display.flip()
    pygame.quit()
menu()