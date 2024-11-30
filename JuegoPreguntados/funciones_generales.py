import pygame
import config
import json
import random
import colores
import datetime
pygame.init()
def empezar_juego():
    print("Juego Iniciado!")
def cargar_preguntas(file_path: str) -> str:
    """_summary_

    Args:
        file_path (_type_): toma el path(camino) del archivo

    Returns:
        _type_: retorna las preguntas que carga del Json
    """
    with open("JuegoPreguntados/preguntas_juego.json", 'r', encoding='utf-8') as file:
        preguntas = json.load(file)
    return preguntas
preguntas = cargar_preguntas('JuegoPreguntados/preguntas_juego.json')

def manejar_string(cadena: str) -> str:
    """_summary_

    Args:
        cadena (_type_): nombre que ingresa el usuario

    Returns:
        _type_: retorna la cadena modificada con mayuscula y guion en caso de espacio
    """
    cadena_mayusculas = cadena.capitalize()
    # Reemplazar espacios con guiones bajos
    cadena_modificada = cadena_mayusculas.replace(' ', '_')
    return cadena_modificada

def mostrar_pantalla_inicio(pantalla, font):
    """_summary_

    Args:
        pantalla (_type_): pantalla donde blitea
        font (_type_): fuente de la letra

    Returns:
        _type_: retorna el input box donde se va a escribir el nombre de usuario y el button rec que es el rectangulo del boton play
    """
    pantalla.blit(config.imagen_de_fondo, (0, 0))
    text_surface = font.render("Introduce tu nombre:", True, colores.AQUAMARINE4)
    pantalla.blit(text_surface, (310, 200))

    input_box = pygame.Rect(312, 226, 393, 49)
    pygame.draw.rect(pantalla, colores.COLOR_CELESTE, input_box, 2)

    button_rect = pygame.Rect(450, 300, 100, 50)
    pygame.draw.rect(pantalla, colores.COLOR_CELESTE, button_rect, 2)
    text_surface = font.render("JUGAR", True, colores.AQUAMARINE4)
    pantalla.blit(text_surface, (button_rect.x + 20, button_rect.y + 15))
    return input_box, button_rect


def seleccionar_categoria(categorias: list) -> str:
    """_summary_

    Args:
    categorias: _type_: keys del archivo .json donde random.choise elige aleatoriamente 

    Returns:
    _type_: retorna una categoria aleatoria en formato de str
    """
    return random.choice(categorias)

def seleccionar_pregunta(pregunta_por_categoria: list) -> str:
    """_summary_

    Args:
    pregunta_por_categoria (list): _type_: lista de preguntas de cada categoria
    Returns:
    _type_: lista de preguntas de la categoria elegida aleatoriamente 
    """
    return random.choice(pregunta_por_categoria)

###################################################################### FUNCIONES QUE YA FUNCIONAN XD ##################################################################################


def temporizador_pregunta(duracion_ms):
    inicio_ticks = pygame.time.get_ticks()  # Obtén el tiempo inicial en milisegundos
        # Calcula el tiempo restante
    tiempo_restante = duracion_ms - (pygame.time.get_ticks() - inicio_ticks)
    # Actualiza la pantalla
    fuente_temporizador = pygame.font.Font(None, 74)
    texto_temporizador = fuente_temporizador.render(f"Tiempo: {tiempo_restante // 1000}", True, (colores.WHITE))
    config.pantalla.blit(texto_temporizador, (100, 100))
    return tiempo_restante

def guardar_ranking(file_path, puntuacion, nombre, tiempo_total_partida=None):
    """Guarda en un archivo formato "csv" el nombre, el timepo de la partida total y los puntos optenidos por el jugador.

    Args:
        file_path (_type_): camino hacia el archivo
        puntuacion (_type_): variable que guarda los puntos obtenidos por el jugador
        nombre (_type_): guarda el nombre ingresado por el jugador
        tiempo_total_partida (_type_, optional): variable que guarda el tiempo que duró la partida. Defaults to None.
        
    """
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'a', newline='') as file:
        datos = f"{nombre},{puntuacion},{fecha_actual},{tiempo_total_partida}\n"
        file.write(datos)
    

def crear_botones(pantalla, texto, font, rect, color_normal, color_hover, accion=None, opciones=None , tiempo_respuestas=None):
    """_summary_

    Args:
        pantalla (_type_): pantalla donde se dibujara el boton
        texto (_type_): texto del boton
        rect(_type_): rectangulo obtenido mediante "pygame.Rect"
        color_normal (_type_): color normal del boton
        color_hover (_type_): color del boton cuando las coordenadas(x,y), del mouse, se superponen a la superficie de este
        accion (_type_, optional): que hace el boton(Su Default es None)
        opciones(_type_, optional): opciones de respuestas a elegir para las preguntas
        timepo_respuestas(_type_, optional): temporizador para elegir la respuesta a la pregunta
    Returns:
    Retorna un boton dibujado en la pantalla con texto en su superficie y las opciones de que al presionarlo, tenga alguna funcion, que muestre las opciones de las preguntas y/o utilize el temporizador para las preguntas.
    """
    font = pygame.font.Font(None, 36)
    rect = pygame.Rect(rect)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    posiciones_botones = [
        (220, 443),
        (590, 443),
        (220, 514),
        (590, 514)
    ]
    if opciones is None:
        opciones = []
    if tiempo_respuestas is None:
        pass
    buttons = []

    # Cambia color si el mouse está sobre el botón
    if rect.collidepoint(mouse):
        pygame.draw.rect(pantalla, color_hover, rect)
        # Verificar si se hace clic en el botón
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_normal, rect)

    texto_superficie = font.render(texto, True, colores.COLOR_TEXTO)
    texto_rect = texto_superficie.get_rect(center=(rect.left + rect.width // 2, rect.top + rect.height // 2))
    pantalla.blit(texto_superficie, texto_rect)

    tamaño_boton = (300, 50)

    for pos, opcion in zip(posiciones_botones, opciones):
        boton_rect_opciones = pygame.Rect(pos, tamaño_boton)
        buttons.append((boton_rect_opciones, opcion))
        pygame.draw.rect(pantalla, colores.WHITE, boton_rect_opciones, 2)
        text_surface = font.render(opcion, True, color_normal)
        pantalla.blit(text_surface, (boton_rect_opciones.left + 10, boton_rect_opciones.top + 10))
    return buttons







def pantalla_de_configuracion_juego():
    pantalla_de_configuracion_juego()

def pantalla_ranking():
    pantalla_ranking()



