import pygame
from config import *
from colores import * 
from funciones_generales import *
opciones_mini_menu = ["Agregar Pregunta", "Jugar", "Configuración", "Salir"]
pygame.init()

def menu():
    flag_correr = True
    while flag_correr:
        #CAMBIE EL .FILL POR UN BLITEO DEL FONDO
        pantalla.blit(imagen_de_fondo, (0, 0))
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:
                flag_correr = False
    #cambie el nombre de las vars de opciones del mini menu y sus posiciones
    posiciones_botones_mini_menu = [(220, 200 + i * 70) for i in range(len(opciones_mini_menu))]

    while True:
        #aca se bliteo tmb
        pantalla.blit(imagen_de_fondo, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i, (opcion, pos) in enumerate(zip(opciones_mini_menu, posiciones_botones_mini_menu)):
            boton_rect = pygame.Rect(pos, (400, 50))
            #Saque los corchetes y strs de los colores
            color = COLOR_HOVER if boton_rect.collidepoint(mouse) else WHITE
            pygame.draw.rect(pantalla, color, boton_rect)

            if boton_rect.collidepoint(mouse) and click[0] == 1:
                pygame.time.wait(200)  # Breve pausa para evitar múltiples clics
                if i == 0:
                    agregar_preguntas()
                elif i == 1:
                    empezar_juego()
                elif i == 2:
                    menu_configuracion()
                elif i == 3:
                    pygame.quit()
                    quit()
            #PUSE UN BLIT PARA QUESE DIBUJEN LAS PREGUNTAS Y CAMBIE EL NOMBRE DE LA VARIABLE DE TEXTO A TEXTO_OPCION_MINI_MENU
            texto_de_opcion_menu_mini = fuente.render(opcion, True, (0, 0, 0))  # Se extrae el texto
            pantalla.blit(texto_de_opcion_menu_mini, (boton_rect.x + 10, boton_rect.y + 10))


        #BOTONES Y PANTALLAS ACÁ   
        pygame.display.flip()
menu()