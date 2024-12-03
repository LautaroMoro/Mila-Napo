import pygame
ALTO = 600
ANCHO = 800
puntuacion = 0
vidas = 3
respuesta_correcta = ""
manejar_string = None
pregunta = None
categorias = ["geografia", "historia", "entretenimiento", "deportes", "ciencia", "tecnologia"]
nombre = ""
manejar_string = None
ultimo_tiempo = pygame.time.get_ticks()
tiempo_restante = 15
cambiar_ingreso_nombre = True

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












