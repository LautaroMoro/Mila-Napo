import pygame
from PantallaPrincipal import *
def main():
    pygame.init()
    pygame.mixer.init()
    pantalla_principal_juego()
    pygame.quit()
if __name__ == "__main__":
    main()