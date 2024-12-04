import pygame
from config import *
from funciones_generales import *
pygame.init()

def menu():
    flag_correr = True
    while flag_correr:
        pantalla.blit(imagen_de_fondo, (0, 0))
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:
                flag_correr = False
    opciones = ["Agregar Pregunta", "Jugar", "Configuración", "Salir"]
    posiciones_botones = [(220, 200 + i * 70) for i in range(len(opciones))]

    while True:
        pantalla.fill(["WHITE"])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i, (opcion, pos) in enumerate(zip(opciones, posiciones_botones)):
            boton_rect = pygame.Rect(pos, (400, 50))
            color = ["BUTTON_HOVER"] if boton_rect.collidepoint(mouse) else ["BUTTON"]
            pygame.draw.rect(pantalla, color, boton_rect)
            render_texto(opcion, (boton_rect.x + 10, boton_rect.y + 10))

            if boton_rect.collidepoint(mouse) and click[0] == 1:
                pygame.time.wait(200)  # Breve pausa para evitar múltiples clics
                if i == 0:
                    agregar_preguntas()
                elif i == 1:
                    jugar()
                elif i == 2:
                    menu_configuracion()
                elif i == 3:
                    pygame.quit()
                    quit()


        #BOTONES Y PANTALLAS ACÁ   
        pygame.display.flip()
menu()