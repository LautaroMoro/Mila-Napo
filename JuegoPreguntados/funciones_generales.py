import pygame
import json
import random
import colores
import datetime
pygame.init()

def empezar_juego():
    global cambiar_ingreso_nombre
    cambiar_ingreso_nombre = True  # Activa la bandera para cambiar de pantalla
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




def guardar_ranking(file_path, puntuacion, nombre_formateado, duracion_partida):
    """Guarda en un archivo formato "csv" el nombre, el timepo de la partida total y los puntos optenidos por el jugador.

    Args:
        file_path (_type_): camino hacia el archivo
        puntuacion (_type_): variable que guarda los puntos obtenidos por el jugador
        nombre (_type_): guarda el nombre ingresado por el jugador
        tiempo_total_partida (_type_, optional): variable que guarda el tiempo que duró la partida. Defaults to None.
        
    """
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'a', newline='') as file:
        datos = f"{nombre_formateado},{puntuacion},{fecha_actual},{duracion_partida}\n"
        file.write(datos)
    

def crear_botones(pantalla, texto, font, rect, color_normal, color_hover, accion=None, opciones=None , tiempo_restante=None):
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

    if tiempo_restante == None:
        tiempo_restante = 15
    posiciones_botones = [
        (220, 443),
        (590, 443),
        (220, 514),
        (590, 514)
    ]
    
    if opciones is None:
        opciones = []
    elif not isinstance(opciones, (list, tuple)):
        print(f"{opciones} debe ser una lista o tupla, pero se recibió: {type(opciones)}")
    elif len(opciones) > len (posiciones_botones):
        print(f"Hay mas opciones que posiciones disponibles para los botones")


        
    buttons = []

    # Cambia color si el mouse está sobre el botón
    if rect.collidepoint(mouse):
        pygame.draw.rect(pantalla, color_hover, rect)
        # Verificar si se hace clic en el botón
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_normal, rect)

    texto_superficie = font.render(str(texto), True, colores.COLOR_TEXTO)
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



