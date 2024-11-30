import pygame
ALTO = 600
ANCHO = 800
puntuacion = 0
tiempo_restante = 30
respuesta_correcta = ""
nombre = ""
manejar_string = None
error = False
pregunta = None
categorias = ["geografia", "historia", "entretenimiento", "deportes", "ciencia", "tecnologia"]
nombre = ""
manejar_string = None
error = False


pygame.init()  
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados")
icono_juego = pygame.image.load("Game_assets/imagenes/LogoJuegoPreguntas.png")
pygame.display.set_icon(icono_juego)


# # Cargar y escalar imágenes
imagen_de_fondo = pygame.image.load("Game_assets/imagenes/fondoPreguntados.png")
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO, ALTO))
pantalla.blit(imagen_de_fondo, (0, 0))


fuente = pygame.font.SysFont("arial", 20)












