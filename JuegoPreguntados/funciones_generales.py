import pygame
from config_2 import *
import json
import random
def cargar_preguntas(file_path: str):
    """_summary_

    Args:
        file_path (_type_): toma el path(camino) del archivo

    Returns:
        _type_: retorna las preguntas que carga del Json
    """
    with open("preguntas_2.json", 'r', encoding='utf-8') as file:
        preguntas = json.load(file)
    return preguntas

def pantalla_de_configuracion_juego():
    pantalla_de_configuracion_juego()

def pantalla_ranking():
    pantalla_ranking()

def pantalla_jugar():
    
    pantalla_jugar()

def seleccionar_categoria(categorias: list) -> str:
    return random.choice(categorias)

def seleccionar_pregunta(pregunta_por_categoria: list) -> str:
    if not pregunta_por_categoria:  # Manejo de listas vacías
        return "No hay preguntas disponibles en esta categoría"
    return random.choice(pregunta_por_categoria)            



