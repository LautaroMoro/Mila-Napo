import pygame
import os
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

RUTA_BASE = os.path.dirname(os.path.dirname(__file__))

# 📁 Rutas a carpetas
RUTA_IMAGENES = os.path.join(RUTA_BASE, "Game_assets", "imagenes")
RUTA_SONIDOS = os.path.join(RUTA_BASE, "Game_assets", "Sonidos")

# 📄 Rutas a archivos
RUTA_LOGO = os.path.join(RUTA_IMAGENES, "LogoJuegoPreguntas.png")
RUTA_FONDO_PREGUNTAS = os.path.join(RUTA_IMAGENES,  "fondoPreguntados.png")
RUTA_PREGUNTAS_JSON = os.path.join(RUTA_BASE, "preguntas_juego.json")
RUTA_RANKING_CSV = os.path.join(RUTA_BASE, "ranking.csv")
RUTA_FONDO_OPCIONES = os.path.join(RUTA_IMAGENES,  "fondo_pantalla_opciones.png")
RUTA_FONDO_MINI_MENU = os.path.join(RUTA_IMAGENES,  "imagen_para_mini_menu.jpg")
RUTA_FONDO_RANKING = os.path.join(RUTA_IMAGENES,  "imagen_para_ranking.jpg")
RUTA_FONDO_AGREGAR_PREGUNTAS = os.path.join(RUTA_IMAGENES,  "imagen_para_agregar_preguntas.jpg")

RUTA_MUSICA = os.path.join(RUTA_SONIDOS,  "musica_fondo.ogg")
RUTA_SONIDO_CO = os.path.join(RUTA_SONIDOS,  "respuesta-correcta.ogg")
RUTA_SONIDO_INC = os.path.join(RUTA_SONIDOS,  "respuesta-incorrecta.ogg")
RUTA_SONIDO_MENU = os.path.join(RUTA_SONIDOS,  "ps2-select-sound.ogg")
pygame.init() 
pygame.mixer.init() 
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados")
icono_juego = pygame.image.load(RUTA_LOGO)
pygame.display.set_icon(icono_juego)


# # Cargar y escalar imágenes
imagen_de_fondo = pygame.image.load(RUTA_FONDO_PREGUNTAS)
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO, ALTO))
pantalla.blit(imagen_de_fondo, (0, 0))

imagen_de_fondo_pantalla_opciones = pygame.image.load(RUTA_FONDO_OPCIONES)
imagen_de_fondo_pantalla_opciones = pygame.transform.scale(imagen_de_fondo_pantalla_opciones, (ANCHO, ALTO))

imagen_de_fondo_pantalla_mini_menu = pygame.image.load(RUTA_FONDO_MINI_MENU)
imagen_de_fondo_pantalla_mini_menu = pygame.transform.scale(imagen_de_fondo_pantalla_mini_menu, (ANCHO, ALTO))

imagen_de_fondo_pantalla_ranking = pygame.image.load(RUTA_FONDO_RANKING)
imagen_de_fondo_pantalla_ranking = pygame.transform.scale(imagen_de_fondo_pantalla_ranking, (ANCHO, ALTO))

imagen_de_fondo_pantalla_agregar_preguntas = pygame.image.load(RUTA_FONDO_AGREGAR_PREGUNTAS)
imagen_de_fondo_pantalla_agregar_preguntas = pygame.transform.scale(imagen_de_fondo_pantalla_agregar_preguntas, (ANCHO, ALTO))

sonido_correcto = pygame.mixer.Sound(RUTA_SONIDO_CO)
sonido_incorrecto = pygame.mixer.Sound(RUTA_SONIDO_INC)
sonido_interfaz_ps2 = pygame.mixer.Sound(RUTA_SONIDO_MENU)

musica_fondo = pygame.mixer.music.load(RUTA_MUSICA)


fuente = pygame.font.SysFont("arial", 20)













