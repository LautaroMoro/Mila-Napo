import pygame
import json
import random
from colores import *
import datetime
import csv
from config import *
import config
from config import RUTA_LOGO
from config import RUTA_RANKING_CSV
import pygame_menu as pm
pygame.init()
pygame.font.init()
def cargar_preguntas() -> str:
    """Permite agregar nuevas preguntas al juego mediante una interfaz gráfica.
    Returns:
        str: retorna las preguntas que carga del Json
    """
    with open(RUTA_PREGUNTAS_JSON, 'r', encoding='utf-8') as file:
        preguntas = json.load(file)
    return preguntas
preguntas = cargar_preguntas()

def guardar_preguntas_json(preguntas_por_categoria, nombre_archivo="preguntas_juego.json"):
    """Guarda las preguntas en un archivo JSON.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(preguntas_por_categoria, archivo, indent=4, ensure_ascii=False)
        print(f"Preguntas guardadas correctamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar las preguntas: {e}")

def manejar_string(cadena: str) -> str:
    """
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
    """
    if duracion_partida == None:
        duracion_partida = None

    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'a', newline='') as file:
        datos = f"{nombre_formateado},{puntuacion},{fecha_actual},{duracion_partida}\n"
        file.write(datos)
    

def crear_botones(pantalla, font, rect, color_normal, color_hover, texto=None, accion=None, opciones=None, tiempo_restante=None):
    font = pygame.font.Font(None, 36)
    rect = pygame.Rect(rect)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if tiempo_restante == None:
        tiempo_restante = 5
    if opciones is None:
        opciones = []
    posiciones_botones = [(200, 443), (570, 443), (200, 514), (570, 514)]
    if len(opciones) > len(posiciones_botones):
        print("Hay más opciones que posiciones disponibles para los botones")
        return []

    buttons = []

    if rect.collidepoint(mouse):
        pygame.draw.rect(pantalla, color_hover, rect)
    

    posiciones_botones = [(200, 443), (570, 443), (200, 514), (570, 514)]
    if len(opciones) > len(posiciones_botones):
        print("Hay más opciones que posiciones disponibles para los botones")
        return []
    buttons = []

    if rect.collidepoint(mouse):
        pygame.draw.rect(pantalla, color_hover, rect)
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_normal, rect)

    texto_superficie = font.render(texto, True, BLACK)
    texto_rect = texto_superficie.get_rect(center=rect.center)
    pantalla.blit(texto_superficie, texto_rect)

    tamaño_boton = (300, 50)

    for pos, opcion in zip(posiciones_botones, opciones):
        boton_rect_opciones = pygame.Rect(pos, tamaño_boton)
        buttons.append((boton_rect_opciones, opcion))
        color = color_hover if boton_rect_opciones.collidepoint(mouse) else color_normal
        pygame.draw.rect(pantalla, color, boton_rect_opciones)
        text_surface = font.render(opcion, True, BLACK)
        pantalla.blit(text_surface, (boton_rect_opciones.left + 10, boton_rect_opciones.top + 10))

    return buttons

estadisticas_preguntas = {}
def actualizar_estadisticas_preguntas(pregunta, respuesta_correcta, respuesta_usuario):
    """Actualiza las estadisticas cada vez que se realiza una pregunta
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

def obtener_input_boxes():
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
    return input_boxes

def agregar_preguntas(pantalla, fuente, preguntas):
    """Permite agregar nuevas preguntas mediante una pantalla alterna.
    """
    input_boxes = obtener_input_boxes()
    boton_retroceder = pygame.Rect(20, 20, 100, 40)
    boton_guardar = pygame.Rect(300, 560, 200, 40)
    activo_campo = None
    corriendo = True
    mostrando_agregar_preguntas = True
    volver_presionado = [False]

    while corriendo:
        pantalla.blit(imagen_de_fondo_pantalla_agregar_preguntas, (0, 0))
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        def volver():
            volver_presionado[0] = True

        crear_botones(pantalla, fuente, boton_retroceder, COLOR_NORMAL, COLOR_HOVER, "Volver", volver)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if mostrando_agregar_preguntas: 
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
                        if categoria in preguntas:
                            preguntas[categoria].append(nueva_pregunta)
                        else:
                            preguntas[categoria] = [nueva_pregunta]

                        guardar_preguntas_json(preguntas)  # Guardar en archivo JSON
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
                    print(f"Campo activo: {activo_campo}")
                
                texto_boton_guardar = fuente.render("Guardar", True, BLACK)
                boton_color = COLOR_HOVER if boton_guardar.collidepoint(mouse) else COLOR_NORMAL
                pygame.draw.rect(pantalla, boton_color, boton_guardar)
                pantalla.blit(texto_boton_guardar, (boton_guardar.x + 50, boton_guardar.y + 5))

            if volver_presionado[0]:
                pygame.time.wait(100)
                return

            pygame.display.flip()

def mostrar_input(campo_rect, texto, activo):
    """Muestra un campo de entrada de texto en la pantalla.
    Args:
        campo_rect (Rect): rectángulo que define la posición y tamaño del campo de entrada.
        texto (str): texto actual del campo de entrada.
        activo (bool): indica si el campo de entrada está activo (seleccionado) o no."""

    color = COLOR_HOVER if activo else WHITE
    pygame.draw.rect(pantalla, color, campo_rect)
    texto_superficie = fuente.render(texto, True, BLACK)
    pantalla.blit(texto_superficie, (campo_rect.x + 10, campo_rect.y + 10))



def menu_configuracion(pantalla):
    """
    Muestra un menú de configuración con opciones para que el jugador modifique la cantidad de vidas, la puntuación y el tiempo restante.
    """
    pantalla.blit(imagen_de_fondo_pantalla_mini_menu, (0, 0))
    settings = pm.Menu(title="Configuración", width=800, height=600, theme=pm.themes.THEME_DARK)

    # Entradas de usuario con valores actuales de config.py
    input_vidas = settings.add.text_input("Vidas: ", default=str(config.vidas))
    input_puntuacion = settings.add.text_input("Puntuación: ", default=str(config.puntuacion))
    input_tiempo = settings.add.text_input("Tiempo restante: ", default=str(config.tiempo_restante))

    settings.add.clock(clock_format="%d-%m-%y %H:%M:%S",
                     title_format="Hora : {0}")
    
    settings.add.button(title="Reiniciar", action=settings.reset_value, 
                    font_color=WHITE, background_color=ROJO) 

    # Función para guardar cambios sin crear archivos
    def guardar_cambios():
        """Guarda las variables modificadas por el usuario en el menú de configuración.
        """
        config.vidas = int(input_vidas.get_value())
        config.puntuacion = int(input_puntuacion.get_value())
        config.tiempo_restante = int(input_tiempo.get_value())
        settings.disable()  # Cierra el menú

    settings.add.button("Guardar", guardar_cambios)
    settings.add.button(title="Volver al menu", action=lambda: settings.disable(), align=pm.locals.ALIGN_CENTER) 

    settings.mainloop(pantalla)




def obtener_top_10(file_path):

    try:
        with open(file_path, newline="", encoding="latin-1") as file:

            lector = csv.reader(file)
            datos = []
            for fila in lector:
                if len(fila) >= 2 and fila[1].isdigit():
                    datos.append(fila)
                else:
                    print(" Fila ignorada por formato inválido:", fila)
            datos.sort(key=lambda x: int(x[1]), reverse=True)
            return datos[:10]
    except Exception as e:
        print(" Error al leer ranking:", e)
        return []

import pygame
import json
import random
from colores import *
import datetime
import csv
from config import *
import config
from config import RUTA_LOGO
from config import RUTA_RANKING_CSV
import pygame_menu as pm
pygame.init()
pygame.font.init()
def cargar_preguntas() -> str:
    """Permite agregar nuevas preguntas al juego mediante una interfaz gráfica.
    Returns:
        str: retorna las preguntas que carga del Json
    """
    with open(RUTA_PREGUNTAS_JSON, 'r', encoding='utf-8') as file:
        preguntas = json.load(file)
    return preguntas
preguntas = cargar_preguntas()

def guardar_preguntas_json(preguntas_por_categoria, nombre_archivo="preguntas_juego.json"):
    """Guarda las preguntas en un archivo JSON.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(preguntas_por_categoria, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar las preguntas: {e}")

def manejar_string(cadena: str) -> str:
    """
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
    """
    if duracion_partida == None:
        duracion_partida = None

    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'a', newline='') as file:
        datos = f"{nombre_formateado},{puntuacion},{fecha_actual},{duracion_partida}\n"
        file.write(datos)
    

def crear_botones(pantalla, font, rect, color_normal, color_hover, texto=None, accion=None, opciones=None, tiempo_restante=None):
    font = pygame.font.Font(None, 36)
    rect = pygame.Rect(rect)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if tiempo_restante == None:
        tiempo_restante = 5
    if opciones is None:
        opciones = []
  
    posiciones_botones = [(200, 443), (570, 443), (200, 514), (570, 514)]
    if len(opciones) > len(posiciones_botones):
        print("Hay más opciones que posiciones disponibles para los botones")
        return []
    buttons = []

    if rect.collidepoint(mouse):
        pygame.draw.rect(pantalla, color_hover, rect)
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_normal, rect)

    texto_superficie = font.render(texto, True, BLACK)
    texto_rect = texto_superficie.get_rect(center=rect.center)
    pantalla.blit(texto_superficie, texto_rect)

    tamaño_boton = (300, 50)

    for pos, opcion in zip(posiciones_botones, opciones):
        boton_rect_opciones = pygame.Rect(pos, tamaño_boton)
        buttons.append((boton_rect_opciones, opcion))
        color = color_hover if boton_rect_opciones.collidepoint(mouse) else color_normal
        pygame.draw.rect(pantalla, color, boton_rect_opciones)
        text_surface = font.render(opcion, True, BLACK)
        pantalla.blit(text_surface, (boton_rect_opciones.left + 10, boton_rect_opciones.top + 10))

    return buttons

estadisticas_preguntas = {}
def actualizar_estadisticas_preguntas(pregunta, respuesta_correcta, respuesta_usuario):
    """Actualiza las estadisticas cada vez que se realiza una pregunta
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

def obtener_input_boxes():
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
    return input_boxes

def agregar_preguntas(pantalla, fuente, preguntas):
    """Permite agregar nuevas preguntas mediante una pantalla alterna.
    """
    input_boxes = obtener_input_boxes()
    boton_retroceder = pygame.Rect(20, 20, 100, 40)
    boton_guardar = pygame.Rect(300, 560, 200, 40)
    activo_campo = None
    corriendo = True
    mostrando_agregar_preguntas = True
    volver_presionado = [False]

    while corriendo:
        pantalla.blit(imagen_de_fondo_pantalla_agregar_preguntas, (0, 0))
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        def volver():
            volver_presionado[0] = True

        crear_botones(pantalla, fuente, boton_retroceder, COLOR_NORMAL, COLOR_HOVER, "Volver", volver)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if mostrando_agregar_preguntas: 
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
                        if categoria in preguntas:
                            preguntas[categoria].append(nueva_pregunta)
                        else:
                            preguntas[categoria] = [nueva_pregunta]

                        guardar_preguntas_json(preguntas)  # Guardar en archivo JSON
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
                    print(f"Campo activo: {activo_campo}")
                
                texto_boton_guardar = fuente.render("Guardar", True, BLACK)
                boton_color = COLOR_HOVER if boton_guardar.collidepoint(mouse) else COLOR_NORMAL
                pygame.draw.rect(pantalla, boton_color, boton_guardar)
                pantalla.blit(texto_boton_guardar, (boton_guardar.x + 50, boton_guardar.y + 5))

            if volver_presionado[0]:
                pygame.time.wait(100)
                return

            pygame.display.flip()

def mostrar_input(campo_rect, texto, activo):
    """Muestra un campo de entrada de texto en la pantalla.
    Args:
        campo_rect (Rect): rectángulo que define la posición y tamaño del campo de entrada.
        texto (str): texto actual del campo de entrada.
        activo (bool): indica si el campo de entrada está activo (seleccionado) o no."""

    color = COLOR_HOVER if activo else WHITE
    pygame.draw.rect(pantalla, color, campo_rect)
    texto_superficie = fuente.render(texto, True, BLACK)
    pantalla.blit(texto_superficie, (campo_rect.x + 10, campo_rect.y + 10))



def menu_configuracion(pantalla):
    """
    Muestra un menú de configuración con opciones para que el jugador modifique la cantidad de vidas, la puntuación y el tiempo restante.
    """
    pantalla.blit(imagen_de_fondo_pantalla_mini_menu, (0, 0))
    settings = pm.Menu(title="Configuración", width=800, height=600, theme=pm.themes.THEME_DARK)

    # Entradas de usuario con valores actuales de config.py
    input_vidas = settings.add.text_input("Vidas: ", default=str(config.vidas))
    input_puntuacion = settings.add.text_input("Puntuación: ", default=str(config.puntuacion))
    input_tiempo = settings.add.text_input("Tiempo restante: ", default=str(config.tiempo_restante))

    settings.add.clock(clock_format="%d-%m-%y %H:%M:%S",
                     title_format="Hora : {0}")
    
    settings.add.button(title="Reiniciar", action=settings.reset_value, 
                    font_color=WHITE, background_color=ROJO) 

    # Función para guardar cambios sin crear archivos
    def guardar_cambios():
        """Guarda las variables modificadas por el usuario en el menú de configuración.
        """
        config.vidas = int(input_vidas.get_value())
        config.puntuacion = int(input_puntuacion.get_value())
        config.tiempo_restante = int(input_tiempo.get_value())
        settings.disable()  # Cierra el menú

    settings.add.button("Guardar", guardar_cambios)
    settings.add.button(title="Volver al menu", action=lambda: settings.disable(), align=pm.locals.ALIGN_CENTER) 

    settings.mainloop(pantalla)




def obtener_top_10(file_path):

    try:
        with open(file_path, newline="", encoding="latin-1") as file:

            lector = csv.reader(file)
            datos = []
            for fila in lector:
                if len(fila) >= 2 and fila[1].isdigit():
                    datos.append(fila)
                else:
                    print(" Fila ignorada por formato inválido:", fila)
            datos.sort(key=lambda x: int(x[1]), reverse=True)
            return datos[:10]
    except Exception as e:
        print(" Error al leer ranking:", e)
        return []
