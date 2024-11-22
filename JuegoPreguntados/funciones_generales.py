import pygame
def crear_boton(path : str, dimensiones: tuple, posicion: tuple, color: tuple, funcion):

    boton = {}
    boton["surface"] = pygame.image.load(path)
    boton["surface"] = pygame.transform.scale(boton["surface"], dimensiones)
    boton["rect_pos"] = pygame.Rect(posicion, dimensiones)
    boton["surface"] = color
    boton["funcion"] = funcion
    return boton


def pantalla_de_configuracion_juego():
    pantalla_de_configuracion_juego()

def pantalla_ranking():
    pantalla_ranking()

def pantalla_jugar():
    pantalla_jugar()

