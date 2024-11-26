import pygame
from funciones_generales_2 import * 
ALTO = 600
ANCHO = 800
ancho_boton = 237
alto_boton = -286
COLOR_CELESTE = (135,206,235)
coordenada_x_boton = (ANCHO - ancho_boton) // 2
coordenada_y_boton = (ALTO - alto_boton) // 2
categoria = ["geografia", "historia", "entretenimiento", "deportes", "ciencia", "tecnologia"]
nombre = ""
manejar_string = None
error = False
tema_seleccionado = None

pygame.init()
    
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados")
icono_juego = pygame.image.load("zLogoJuegoPreguntas.png")
pygame.display.set_icon(icono_juego)


# # Cargar y escalar imágenes
imagen_de_fondo = pygame.image.load("zfondoPreguntados.png")
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO, ALTO))
pantalla.blit(imagen_de_fondo, (0, 0))

#Boton de arranque
imagen_boton = pygame.image.load("zBoton.webp")
imagen_boton = pygame.transform.scale(imagen_boton, (0, 0))




