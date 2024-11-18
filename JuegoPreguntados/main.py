import pygame
from config import *
pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntas Para Basados")
icono_juego = pygame.image.load("Game_assets/LogoJuegoPreguntas.png")
#Pude cambiar el icono, basicamente el error estaba en que la imagen tenia que estar en la carpeta general,
#  además de que la imagen tenia que ser formato 32x32 pixeles.   
pygame.display.set_icon(icono_juego)

# # Cargar y escalar imágenes
imagen_de_fondo = pygame.image.load("Game_assets/fondoPreguntados.png")
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO, ALTO))
pantalla.blit(imagen_de_fondo, (0, 0))
pygame.display.flip()
#Pude cambiar la imagen del fondo, nos faltó posicionar la foto y se ve que la actualizacion de la pantalla tiene que ir antes de que corra el juego
# (Eso hay que preguntarselo al profe), porque si pongo el .flip() desp del bucle no me pone el fondo

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

pygame.quit()


#Codigo desfuncional
# # # #boton empezar
# # imagen_empezar = pygame.image.load("")
# # imagen_empezar = pygame.transform.scale(imagen_empezar, (0, 0))

# # #colores a usar 
# # COLOR_CELESTE = (135,206,235)
# # COLOR_AMARILLO = (255,255,0)
# # COLOR_BLANCO = (255,255,255)
# # COLOR_GRIS = (128,128,128)