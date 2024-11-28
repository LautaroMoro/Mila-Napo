import pygame
import json
ALTO = 600
ANCHO = 800
COLOR_CELESTE = (135,206,235)
AQUAMARINE4 = (69, 139, 116)
COLOR_NORMAL = (0, 128, 255)
COLOR_HOVER = (0, 200, 255)
COLOR_TEXTO = (0, 0, 0)
puntuacion = 0
tiempo_restante = 30
respuesta_correcta = ""
nombre = ""
categorias = ["ciencia", "entretenimiento", "deportes", "geografia", "tecnologia", "historia"]
nombre = ""
manejar_string = None
error = False
pregunta = None
ancho_boton = 237
alto_boton = -286

coordenada_x_boton = (ANCHO - ancho_boton) // 2
coordenada_y_boton = (ALTO - alto_boton) // 2
pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados")
icono_juego = pygame.image.load("Game_assets/imagenes/LogoJuegoPreguntas.png")
pygame.display.set_icon(icono_juego)


# # Cargar y escalar imágenes
imagen_de_fondo = pygame.image.load("Game_assets/imagenes/fondoPreguntados.png")
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO, ALTO))
pantalla.blit(imagen_de_fondo, (0, 0))

#Boton de arranque
imagen_boton = pygame.image.load("Game_assets/imagenes/Boton.webp")
imagen_boton = pygame.transform.scale(imagen_boton, (0, 0))
fuente = pygame.font.SysFont("arial", 20)









