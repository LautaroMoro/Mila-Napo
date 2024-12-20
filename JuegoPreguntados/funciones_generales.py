import pygame
import json
import random
from colores import *
import datetime
import csv
from config import *
pygame.init()

def cargar_preguntas(file_path: str) -> str:
    """Permite agregar nuevas preguntas al juego mediante una interfaz gráfica.

    Args:
        file_path (_type_): toma el path(camino) del archivo

    Returns:
        str: retorna las preguntas que carga del Json
    """
    with open("preguntas_juego.json", 'r', encoding='utf-8') as file:
        preguntas = json.load(file)
    return preguntas
preguntas = cargar_preguntas('preguntas_juego.json')

def guardar_preguntas_json(preguntas_por_categoria, nombre_archivo="preguntas_juego.json"):
    """Guarda las preguntas en un archivo JSON.

    Args:
        preguntas_por_categoria (list): lista de preguntas segun la categoria escogida
        nombre_archivo (json, optional): archivo.json opcional para guardar las preguntas. Defaults to "preguntas_juego.json".
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(preguntas_por_categoria, archivo, indent=4, ensure_ascii=False)
        print(f"Preguntas guardadas correctamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar las preguntas: {e}")

def manejar_string(cadena: str) -> str:
    """_summary_

    Args:
        cadena (str): nombre que ingresa el usuario

    Returns:
        str: retorna la cadena modificada con mayuscula y guion en caso de espacio
    """
    cadena_mayusculas = cadena.capitalize()
    # Reemplazar espacios con guiones bajos
    cadena_modificada = cadena_mayusculas.replace(' ', '_')
    return cadena_modificada



def seleccionar_categoria(categorias: list) -> str:
    """Selecciona una categoría aleatoria de una lista de categorías.

    Args:
    categorias: list: keys del archivo .json donde random.choise elige aleatoriamente 

    Returns:
    str: retorna una categoria aleatoria en formato de str
    """
    return random.choice(categorias)



def seleccionar_pregunta(pregunta_por_categoria: list) -> str:
    """_summary_

    Args:
    pregunta_por_categoria (list): lista de preguntas de cada categoria
    Returns:
    pregunta_por_categoria: lista de preguntas de la categoria elegida aleatoriamente 
    """
    if not pregunta_por_categoria:
        raise ValueError("No hay preguntas disponibles para la categoría seleccionada.")
    return random.choice(pregunta_por_categoria)


def guardar_ranking(file_path, puntuacion, nombre_formateado, duracion_partida=None):
    """Guarda en un archivo formato "csv" el nombre, el timepo de la partida total y los puntos optenidos por el jugador.

    Args:
        file_path (_type_): camino hacia el archivo
        puntuacion (_type_): variable que guarda los puntos obtenidos por el jugador
        nombre (_type_): guarda el nombre ingresado por el jugador
        tiempo_total_partida (_type_, optional): variable que guarda el tiempo que duró la partida. Defaults to None.
        
    """
    if duracion_partida == None:
        duracion_partida = None

    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'a', newline='') as file:
        datos = f"{nombre_formateado},{puntuacion},{fecha_actual},{duracion_partida}\n"
        file.write(datos)
    

def crear_botones(pantalla, font, rect, color_normal, color_hover, texto=None, accion=None, opciones=None , tiempo_restante=None):
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
        tiempo_restante = 5
    
    if opciones is None:
        opciones = []
    
    posiciones_botones = [
        (200, 443),  # Botón 1
        (570, 443),  # Botón 2
        (200, 514),  # Botón 3
        (570, 514)
    ]
    if len(opciones) > len (posiciones_botones):
        print(f"Hay mas opciones que posiciones disponibles para los botones")
        return []


        
    buttons = []


    if rect.collidepoint(mouse):
        pygame.draw.rect(pantalla, color_hover, rect)
 
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_normal, rect)

    texto_superficie = font.render(texto, True, BLACK)
    texto_rect = texto_superficie.get_rect(center=(rect.left + rect.width // 2, rect.top + rect.height // 2))
    pantalla.blit(texto_superficie, texto_rect)

    tamaño_boton = (300, 50)

    for pos, opcion in zip(posiciones_botones, opciones):
        boton_rect_opciones = pygame.Rect(pos, tamaño_boton)
        buttons.append((boton_rect_opciones, opcion))
        

        if boton_rect_opciones.collidepoint(mouse):
            pygame.draw.rect(pantalla, color_hover, boton_rect_opciones)

        else:
            pygame.draw.rect(pantalla, color_normal, boton_rect_opciones)


        text_surface = font.render(opcion, True, BLACK)  # Texto negro
        pantalla.blit(text_surface, (boton_rect_opciones.left + 10, boton_rect_opciones.top + 10))

    return buttons

estadisticas_preguntas = {}
def actualizar_estadisticas_preguntas(pregunta, respuesta_correcta, respuesta_usuario):
    """Actualiza las estadisticas cada vez que se realiza una pregunta

    Args:
        pregunta (clave del dikt): pregunta realizada mediante el json
        respuesta_correcta (clave del dikt): respuesta correcta de la pregunta
        respuesta_usuario (clave del dikt): respuesta del usuario
    """
    if pregunta not in estadisticas_preguntas:
        estadisticas_preguntas[pregunta] = {
            "total_preguntas": 0,
            "respuestas_correctas": 0,
            "respuestas_incorrectas": 0    
        }

    estadisticas_preguntas[pregunta]["total_preguntas"] += 1

    # Incrementar las respuestas correctas o incorrectas
    if respuesta_usuario == respuesta_correcta:
        estadisticas_preguntas[pregunta]["respuestas_correctas"] += 1
    else:
        estadisticas_preguntas[pregunta]["respuestas_incorrectas"] += 1


def guardar_estadisticas_preguntas_realizadas_csv():
    """guarda y escribe las estadisticas actualizadas en un csv
    """
    with open("estadisticas_preguntas.csv", mode="w", newline="", encoding="utf-8") as file:
        campos = ["Pregunta hecha", "Veces que se preguntó", "Respuestas acertadas", "Respuestas erradas", "Porcentaje Aciertos"]
        escrito = csv.DictWriter(file, fieldnames=campos)
        escrito.writeheader()

        for pregunta, estadisticas in estadisticas_preguntas.items():
            if estadisticas["total_preguntas"] > 0:
                porcentaje_aciertos = (estadisticas["respuestas_correctas"] / estadisticas["total_preguntas"]) * 100
            else:
                porcentaje_aciertos = 0
            fila = {
            'Pregunta hecha': pregunta,
            'Veces que se preguntó': estadisticas['total_preguntas'],
            'Respuestas acertadas': estadisticas['respuestas_correctas'],
            'Respuestas erradas': estadisticas['respuestas_incorrectas'],
            'Porcentaje Aciertos': f"{porcentaje_aciertos:.2f}%"  
            }

            escrito.writerow(fila)



def agregar_preguntas():
    """
    Permite agregar nuevas preguntas mediante una pantalla alterna.
    """
    global preguntas_por_categoria
    preguntas_por_categoria = preguntas
    input_boxes = [
        {"rect": pygame.Rect(220, 150, 360, 30), "texto": "", "activo": False, "etiqueta": "Categoría"},
        {"rect": pygame.Rect(220, 210, 560, 30), "texto": "", "activo": False, "etiqueta": "Texto de la Pregunta"},
        {"rect": pygame.Rect(220, 270, 460, 30), "texto": "", "activo": False, "etiqueta": "Opción 1"},
        {"rect": pygame.Rect(220, 330, 460, 30), "texto": "", "activo": False, "etiqueta": "Opción 2"},
        {"rect": pygame.Rect(220, 390, 460, 30), "texto": "", "activo": False, "etiqueta": "Opción 3"},
        {"rect": pygame.Rect(220, 450, 460, 30), "texto": "", "activo": False, "etiqueta": "Opción 4"},
        {"rect": pygame.Rect(220, 510, 460, 30), "texto": "", "activo": False, "etiqueta": "Respuesta Correcta"},
        {"rect": pygame.Rect(220, 570, 460, 30), "texto": "", "activo": False, "etiqueta": "Dificultad"}
    ]
    boton_guardar = pygame.Rect(300, 560, 200, 40)
    activo_campo = None
    corriendo = True

    while corriendo:
        pantalla.blit(imagen_de_fondo_pantalla_agregar_preguntas, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i, input_box in enumerate(input_boxes):
                    if input_box["rect"].collidepoint(evento.pos):
                        activo_campo = i
                        input_box["activo"] = True
                    else:
                        input_box["activo"] = False

                if boton_guardar.collidepoint(evento.pos):
                    categoria = input_boxes[0]["texto"]
                    nueva_pregunta = {
                        "pregunta": input_boxes[1]["texto"],
                        "opciones": [
                            input_boxes[2]["texto"],
                            input_boxes[3]["texto"],
                            input_boxes[4]["texto"],
                            input_boxes[5]["texto"]
                        ],
                        "respuesta_correcta": input_boxes[6]["texto"],
                        "dificultad": input_boxes[7]["texto"]
                    }
                     # Agregar la nueva pregunta a la categoría correspondiente
                    if categoria in preguntas_por_categoria:
                        preguntas_por_categoria[categoria].append(nueva_pregunta)
                    else:
                        preguntas_por_categoria[categoria] = [nueva_pregunta]

                    guardar_preguntas_json(preguntas_por_categoria)  # Guardar en archivo JSON
                    print("¡Pregunta agregada con éxito!")
                    corriendo = False

            if evento.type == pygame.KEYDOWN and activo_campo is not None:
                if evento.key == pygame.K_BACKSPACE:
                    input_boxes[activo_campo]["texto"] = input_boxes[activo_campo]["texto"][:-1]
                else:
                    input_boxes[activo_campo]["texto"] += evento.unicode

        for input_box in input_boxes:
            etiqueta = fuente.render(input_box["etiqueta"], True, BLACK)
            pantalla.blit(etiqueta, ( input_box["rect"].x, input_box["rect"].y - 30))
            mostrar_input(input_box["rect"], input_box["texto"], input_box["activo"])
        
        texto_boton_guardar = fuente.render("Guardar", True, BLACK)
        
        mouse = pygame.mouse.get_pos()
        boton_color = COLOR_HOVER if boton_guardar.collidepoint(mouse) else COLOR_NORMAL
        pygame.draw.rect(pantalla, boton_color, boton_guardar)
        pantalla.blit(texto_boton_guardar, (boton_guardar.x + 50, boton_guardar.y + 5))

        pygame.display.flip()

def mostrar_input(campo_rect, texto, activo):
    """Muestra un campo de entrada de texto en la pantalla.

    Args:
        campo_rect (Rect): Rectángulo que define la posición y tamaño del campo de entrada.
        texto (str): Texto actual del campo de entrada.
        activo (bool): Indica si el campo de entrada está activo (seleccionado) o no.
    """
    color = COLOR_HOVER if activo else WHITE
    pygame.draw.rect(pantalla, color, campo_rect)
    texto_superficie = fuente.render(texto, True, BLACK)
    pantalla.blit(texto_superficie, (campo_rect.x + 10, campo_rect.y + 10))



def menu_configuracion():
    """
    Muestra un menú de configuración con opciones para modificar la puntuación, vidas y tiempo entre preguntas.
    """
    global puntuacion, vidas, tiempo_restante

    opciones = [
        f"Modificar Puntos por Respuesta Correcta (Actual: {puntuacion})",
        f"Modificar Cantidad de Vidas (Actual: {vidas})",
        f"Modificar Tiempo entre Preguntas (Actual: {tiempo_restante}s)",
        "Volver al Menú Principal"
    ]
    posiciones_botones = [(100, 200 + i * 70) for i in range(len(opciones))]

    corriendo = True
    while corriendo:
        pantalla.blit(imagen_de_fondo_pantalla_mini_menu, (0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i, (opcion, pos) in enumerate(zip(opciones, posiciones_botones)):
            boton_rect = pygame.Rect(pos, (600, 50))
            color = COLOR_HOVER if boton_rect.collidepoint(mouse) else COLOR_NORMAL
            pygame.draw.rect(pantalla, color, boton_rect)

            if boton_rect.collidepoint(mouse) and click[0] == 1:
                pygame.time.wait(200)  # Breve pausa para evitar múltiples clics
                if i == 0:
                    puntuacion = modificar_valor("Puntos por Respuesta Correcta", puntuacion)
                elif i == 1:
                    vidas = modificar_valor("Cantidad de Vidas", vidas)
                elif i == 2:
                    tiempo_restante = modificar_valor("Tiempo entre Preguntas (en segundos)", tiempo_restante)
                elif i == 3:
                    corriendo = False
            texto = fuente.render(opcion, True, BLACK)
            pantalla.blit(texto, (boton_rect.x + 10, boton_rect.y + 10))


        pygame.display.flip()

def modificar_valor(etiqueta, valor_actual):
    """Permite modificar un valor entero mediante una pantalla alterna.

    Args:
        etiqueta (str): etiqueta mostrada en pantalla paraayudar al usuario a identificar que dato esta por modificar.
        valor_actual (str): valor que se quiere modificar.

    Returns:
        _type_: _description_
    """
    input_rect = pygame.Rect(250, 300, 300, 50)
    activo = False
    texto = str(valor_actual)

    while True:
        pantalla.blit(imagen_de_fondo, (0, 0))
        color = COLOR_HOVER if activo else WHITE
        pygame.draw.rect(pantalla, color, input_rect)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(evento.pos):
                    activo = True
                else:
                    activo = False
            if evento.type == pygame.KEYDOWN and activo:
                if evento.key == pygame.K_RETURN:
                    return int(texto)
                elif evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                else:
                    texto += evento.unicode

        texto_surface = fuente.render(texto, True, BLACK)
        pantalla.blit(texto_surface, (input_rect.x + 10, input_rect.y + 10))
        pygame.display.flip()



def obtener_top_10(file_path):
    """obtinene el top 10 de los jugadores con mayor puntuacion en el ranking.

    Args:
        file_path (csv): camino hacia el archivo csv

    Returns:
        datos[:10]: retorna los 10 primeros datos del archivo csv(ordenados en base a su puntuacion, tiempo de partida y nombre)
    """

    try:
        with open(file_path, newline="") as file:
            archivo = csv.reader(file)
            next(archivo)
            datos = sorted(archivo, key=lambda x: int(x[1]), reverse=True)
            return datos[:10]
    except FileNotFoundError:
        return [] 
    except ValueError:
        return [] 


