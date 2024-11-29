import pygame
import config
import json
import random

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
    text_surface = font.render("Introduce tu nombre:", True, config.AQUAMARINE4)
    pantalla.blit(text_surface, (310, 200))

    input_box = pygame.Rect(312, 226, 393, 49)
    pygame.draw.rect(pantalla, config.COLOR_CELESTE, input_box, 2)

    button_rect = pygame.Rect(450, 300, 100, 50)
    pygame.draw.rect(pantalla, config.COLOR_CELESTE, button_rect, 2)
    text_surface = font.render("JUGAR", True, config.AQUAMARINE4)
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



def crear_boton_arranque(pantalla, texto, x, y, ancho, alto, color_normal, color_hover, accion=None):
    """_summary_

    Args:
        pantalla (_type_): pantalla donde se dibujara el boton
        texto (_type_): texto del boton
        x (_type_): coordenada del boton
        y (_type_): coordenada del boton
        ancho (_type_): ancho del boton
        alto (_type_): alto del boton
        color_normal (_type_): color normal del boton
        color_hover (_type_): color del boton cuando las coordenadas(x,y), del mouse, se superponen a la superficie de este
        accion (_type_, optional): que hace el boton(Su Default es None)
    Returns:
    Retorna un boton dibujado en la pantalla con texto en su superficie y la opcion de que al presionarlo, tenga alguna funcion
    """
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Cambia color si el mouse está sobre el botón
    if x < mouse[0] < x + ancho and y < mouse[1] < y + alto:
        pygame.draw.rect(pantalla, color_hover, (x, y, ancho, alto))
        # Verificar si se hace clic en el botón
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_normal, (x, y, ancho, alto))

    # Agregar texto al botón
    fuente = pygame.font.Font(None, 36)
    texto_superficie = fuente.render(texto, True, config.COLOR_TEXTO)
    texto_rect = texto_superficie.get_rect(center=(x + ancho // 2, y + alto // 2))
    pantalla.blit(texto_superficie, texto_rect)

def temporizador_pregunta(duracion_ms):
    inicio_ticks = pygame.time.get_ticks()  # Obtén el tiempo inicial en milisegundos

        # Calcula el tiempo restante
    tiempo_restante = duracion_ms - (pygame.time.get_ticks() - inicio_ticks)
    # Actualiza la pantalla
    fuente_temporizador = pygame.font.Font(None, 74)
    texto_temporizador = fuente_temporizador.render(f"Tiempo: {tiempo_restante // 1000}", True, (config.WHITE))
    config.pantalla.blit(texto_temporizador, (100, 100))
tiempo_respuestas = temporizador_pregunta(15000)

def crear_botones_opciones(pantalla, texto, fuente, color, rect, opciones, tiempo_respuestas):
    """_summary_

    Args:
        pantalla (_type_): pantalla donde se dibujara el boton
        fuente: Fuente para renderizar texto.
        posiciones_botones: Lista de posiciones (x, y) de los botones.
        tamaño_botones: Tamaño (ancho, alto) de los botones.
        color_normal (_type_): color normal del boton
        opciones (_type_): opciones de la pregunta aleatoria
        tiempo_respuestas (_type_): tiempo para responder la pregunta
    Returns:
    Retorna 4 botones dibujados en la pantalla con texto en su superficie y las opciones a elegir para la pregunta

    """
    rect = pygame.Rect(rect)

    buttons = []

    for i in texto:
        text_surface = fuente.render(i, True, color)
        pantalla.blit(text_surface, (238, 360))

    posiciones_botones = [
        (220, 443),
        (590, 443),
        (220, 514),
        (590, 514)
    ]
    tamaño_boton = (300, 50)

    for pos, opcion in zip(posiciones_botones, opciones):
        boton_rect = pygame.Rect(pos, tamaño_boton)
        if i < len(opciones):
            buttons.append((boton_rect, opcion))
            pygame.draw.rect(pantalla, config.WHITE, boton_rect, 2)
            text_surface = fuente.render(opciones[i], True, color)
            pantalla.blit(text_surface, (boton_rect.x + 10, boton_rect.y + 10))

    return buttons
    
def empezar_juego():
    print("Juego Iniciado!")









def pantalla_de_configuracion_juego():
    pantalla_de_configuracion_juego()

def pantalla_ranking():
    pantalla_ranking()



