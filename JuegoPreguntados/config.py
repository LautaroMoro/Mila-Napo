import pygame

ALTO = 600
ANCHO = 800
puntuacion = 0
vidas = 3
nombre = ""
respuesta_correcta = ""
cambiar_ingreso_nombre = False
error = False
tiempo_restante = 5
ultimo_tiempo = pygame.time.get_ticks()
categorias = ["geografia", "historia", "entretenimiento", "deportes", "ciencia", "tecnologia"]
pregunta = None
tema_random = None


pygame.init()  
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados")
icono_juego = pygame.image.load("Game_assets/imagenes/LogoJuegoPreguntas.png")
pygame.display.set_icon(icono_juego)


# # Cargar y escalar imágenes
imagen_de_fondo = pygame.image.load("Game_assets/imagenes/fondoPreguntados.png")
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO, ALTO))
pantalla.blit(imagen_de_fondo, (0, 0))

imagen_de_fondo_pantalla_opciones = pygame.image.load("Game_assets/imagenes/fondo_pantalla_opciones.png")
imagen_de_fondo_pantalla_opciones = pygame.transform.scale(imagen_de_fondo_pantalla_opciones, (ANCHO, ALTO))
fuente = pygame.font.SysFont("arial", 20)












