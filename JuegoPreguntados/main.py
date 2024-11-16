import pygame
from config import *
pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
icono_juego = pygame.image.load("iconoPreguntados.png")
pygame.display.set_icon(icono_juego)

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

pygame.display.flip()



#Codigo desfuncional
# pantalla = pygame.display.set_mode((500 , 900))

#titulo
# screen = pygame.display.set_mode((500 , 900))
# pygame.display.set_caption("preguntados")



# imagen = pygame.image.load("icono.png")
# pygame.display.set_icon(imagen)

# imagen = pygame.transform.scale(imagen ,(300,300))


# # Cargar y escalar imágenes
# imagen_de_fondo = pygame.image.load("preguntados.png")
# imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (500, 900))

# # # #boton empezar
# # imagen_empezar = pygame.image.load("")
# # imagen_empezar = pygame.transform.scale(imagen_empezar, (0, 0))

# # imagen de fondo 
# imagen_fondo_juego = pygame.image.load("preguntas.png")
# imagen_fondo_juego = pygame.transform.scale(imagen_fondo_juego, (500, 900))



# # #colores a usar 
# # COLOR_CELESTE = (135,206,235)
# # COLOR_AMARILLO = (255,255,0)
# # COLOR_BLANCO = (255,255,255)
# # COLOR_GRIS = (128,128,128)