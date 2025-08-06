import pygame
import os
from config import *
from colores import * 
from funciones_generales import *
opciones_mini_menu = ["Agregar Pregunta", "Configuración", "Salir"]
pygame.init()

def menu():
    flag_correr = True
    while flag_correr:

        pantalla.blit(imagen_de_fondo_pantalla_mini_menu, (0, 0))

        posiciones_botones_mini_menu = [(220, 200 + i * 70) for i in range(len(opciones_mini_menu))]

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i, (opcion, pos) in enumerate(zip(opciones_mini_menu, posiciones_botones_mini_menu)):
            boton_rect = pygame.Rect(pos, (400, 50))
            color = COLOR_HOVER if boton_rect.collidepoint(mouse) else WHITE
            pygame.draw.rect(pantalla, color, boton_rect)

            if boton_rect.collidepoint(mouse) and click[0] == 1:
                pygame.time.wait(200)  
                if i == 0:
                    agregar_preguntas(pantalla, fuente, preguntas)
                elif i == 1:
                    menu_configuracion(pantalla)
                elif i == 2:
                    flag_correr = False
                    return
            texto_de_opcion_menu_mini = fuente.render(opcion, True, BLACK) # extrae el texto
            pantalla.blit(texto_de_opcion_menu_mini, (boton_rect.x + 10, boton_rect.y + 10))
        pygame.display.flip()
    pygame.quit()
