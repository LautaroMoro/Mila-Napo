import pygame
from config import *
from colores import *

def pantalla_de_configuracion_juego():
    pantalla_de_configuracion_juego()

def pantalla_ranking():
    pantalla_ranking()

def mostrar_pantalla_ingreso_nombre(pantalla, nombre):
    input_box = pygame.Rect(312, 226, 393, 49)
    introduciendo_nombre = True
    error = False

    while introduciendo_nombre:
        pantalla.fill(BLACK)
        text_surface = fuente.render("Introduce tu nombre:", True, WHITE)
        pantalla.blit(text_surface, (310, 200))
        pygame.draw.rect(pantalla, WHITE, input_box, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre.strip():
                        introduciendo_nombre = False
                    else:
                        error = True
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode

        # Mostrar nombre en el cuadro de texto
        nombre_surface = fuente.render(nombre, True, WHITE)
        pantalla.blit(nombre_surface, (input_box.x + 5, input_box.y + 5))

        # Mostrar mensaje de error
        if error:
            error_surface = fuente.render("¡Debes ingresar un nombre!", True, ROJO)
            pantalla.blit(error_surface, (310, 300))

        pygame.display.flip()