import sys
import pygame
import os
def ruta_recurso(rel_path):
   try:
      base_path = sys._MEIPASS
   except AttributeError:
      base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
   return os.path.join(base_path, rel_path)


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


# 📄 Rutas a archivos
RUTA_LOGO = ruta_recurso("Game_assets/imagenes/LogoJuegoPreguntas.png")
RUTA_FONDO_PREGUNTAS = ruta_recurso("Game_assets/imagenes/fondoPreguntados.png")
RUTA_PREGUNTAS_JSON = ruta_recurso("preguntas_juego.json")
RUTA_RANKING_CSV = ruta_recurso("ranking.csv")
RUTA_FONDO_OPCIONES = ruta_recurso("Game_assets/imagenes/fondo_pantalla_opciones.png")
RUTA_FONDO_MINI_MENU = ruta_recurso("Game_assets/imagenes/imagen_para_mini_menu.jpg")
RUTA_FONDO_RANKING = ruta_recurso("Game_assets/imagenes/imagen_para_ranking.jpg")
RUTA_FONDO_AGREGAR_PREGUNTAS = ruta_recurso("Game_assets/imagenes/imagen_para_agregar_preguntas.jpg")

RUTA_MUSICA = ruta_recurso("Game_assets/Sonidos/musica_fondo.ogg")
RUTA_SONIDO_CO = ruta_recurso("Game_assets/Sonidos/respuesta-correcta.ogg")
RUTA_SONIDO_INC = ruta_recurso("Game_assets/Sonidos/respuesta-incorrecta.ogg")
RUTA_SONIDO_MENU = ruta_recurso("Game_assets/Sonidos/ps2-select-sound.ogg")

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





