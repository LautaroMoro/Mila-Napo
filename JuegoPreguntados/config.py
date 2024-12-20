import pygame

ALTO = 600
ANCHO = 800
puntuacion = 0
vidas = 3
nombre = ""
respuesta_correcta = ""
cambiar_ingreso_nombre = False
error = False
tiempo_restante = 10
ultimo_tiempo = pygame.time.get_ticks()
categorias = ["geografia", "historia", "entretenimiento", "deportes", "ciencia", "tecnologia"]
pregunta = None
tema_random = None


pygame.init() 
pygame.mixer.init() 
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

imagen_de_fondo_pantalla_mini_menu = pygame.image.load("Game_assets/imagenes/imagen_para_mini_menu.jpg")
imagen_de_fondo_pantalla_mini_menu = pygame.transform.scale(imagen_de_fondo_pantalla_mini_menu, (ANCHO, ALTO))

imagen_de_fondo_pantalla_ranking = pygame.image.load("Game_assets/imagenes/imagen_para_ranking.jpg")
imagen_de_fondo_pantalla_ranking = pygame.transform.scale(imagen_de_fondo_pantalla_ranking, (ANCHO, ALTO))

imagen_de_fondo_pantalla_agregar_preguntas = pygame.image.load("Game_assets/imagenes/imagen_para_agregar_preguntas.jpg")
imagen_de_fondo_pantalla_agregar_preguntas = pygame.transform.scale(imagen_de_fondo_pantalla_agregar_preguntas, (ANCHO, ALTO))

sonido_correcto = pygame.mixer.Sound("Game_assets/sonidos/respuesta-correcta.ogg")
sonido_incorrecto = pygame.mixer.Sound("Game_assets/sonidos/respuesta-incorrecta.ogg")
sonido_interfaz_ps2 = pygame.mixer.Sound("Game_assets/Sonidos/ps2-select-sound.ogg")

musica_fondo = pygame.mixer.music.load("Game_assets/sonidos/musica_fondo.ogg")


fuente = pygame.font.SysFont("arial", 20)













