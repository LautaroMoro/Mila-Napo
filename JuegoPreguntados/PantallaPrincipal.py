import pygame
from config import *
from funciones_generales import *
from colores import *
from funciones_pantallas import *
from menu import * 
pygame.init()
pygame.mixer.init()
def pantalla_principal_juego():
    cambiar_ingreso_nombre = False
    mostrando_pantalla_ranking = False
    flag_correr = True
    error = False
    sonido_interfaz_ps2.set_volume(0.5)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    boton_empezar = pygame.Rect(200, 450, 350, 50)
    boton_salir = pygame.Rect(650, 10, 150, 40)
    while flag_correr:
        # Dibujar el fondo
        pantalla.blit(imagen_de_fondo, (0, 0))
        crear_botones(pantalla, fuente, (200, 450, 350, 50), COLOR_NORMAL, COLOR_HOVER, "Empezar",  None)
        crear_botones(pantalla, fuente, (10, 10, 100, 50), COLOR_NORMAL, COLOR_HOVER, "Menu",  menu)
        crear_botones(pantalla, fuente, (200, 520, 350, 50), COLOR_NORMAL, COLOR_HOVER, "Ver ranking", lambda: mostrar_top_10(pantalla, fuente, "ranking.csv")) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                sonido_interfaz_ps2.play()
                pygame.time.delay(200)
                if not cambiar_ingreso_nombre:
                    if event.button == 1 and boton_empezar.collidepoint(mouse):
                        cambiar_ingreso_nombre = True

        if cambiar_ingreso_nombre:
            nombre = mostrar_pantalla_ingreso_nombre(pantalla)
            if nombre.strip():
                try:
                    puntuacion = mostrar_pantalla_opciones(pantalla, fuente, nombre)
                    print(f"Puntos finales: {puntuacion}")
                    mostrando_pantalla_ranking = True
                except ValueError as e:
                    print(e)
                    flag_correr = False
                cambiar_ingreso_nombre = False
            else:
                error = True
        if mostrando_pantalla_ranking:
            mostrar_top_10(pantalla, fuente, "ranking.csv")
            mostrando_pantalla_ranking = False

        texto_boton_salir = fuente.render("Salir", True, BLACK)
        boton_color = COLOR_HOVER if boton_salir.collidepoint(mouse) else COLOR_NORMAL
        pygame.draw.rect(pantalla, boton_color, boton_salir)
        pantalla.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 5))

        if boton_salir.collidepoint(mouse) and click[0] == 1:
            flag_correr = False


  
        pygame.display.flip()
    pygame.mixer.music.stop()