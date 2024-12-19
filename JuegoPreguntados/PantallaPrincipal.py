import pygame
from config import *
from funciones_generales import *
from colores import *
from funciones_pantallas import *
from menu import * 
pygame.init()
def pantalla_principal_juego():
    cambiar_ingreso_nombre = False
    flag_correr = True
    error = False
    boton_empezar = pygame.Rect(200, 450, 350, 50)
    while flag_correr:
        # Dibujar el fondo
        pantalla.blit(imagen_de_fondo, (0, 0))
        crear_botones(pantalla, fuente, (200, 450, 350, 50), COLOR_NORMAL, COLOR_HOVER, "Empezar",  None)
        crear_botones(pantalla, fuente, (10, 10, 100, 50), COLOR_NORMAL, COLOR_HOVER, "Menu",  menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False

            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not cambiar_ingreso_nombre:
                    if event.button == 1 and boton_empezar.collidepoint(mouse):
                        cambiar_ingreso_nombre = True

        if cambiar_ingreso_nombre:
            nombre = mostrar_pantalla_ingreso_nombre(pantalla)
            if nombre.strip():
                cambiar_ingreso_nombre = False
                puntuacion = mostrar_pantalla_opciones(pantalla, fuente)
                print(f"Puntos finales: {puntuacion}")
                flag_correr = False
            else:
                error = True


        pygame.display.flip()
        # Aquí iría la lógica del juego
    pygame.quit()
pantalla_principal_juego()
