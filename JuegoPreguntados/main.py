import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pygame
from PantallaPrincipal import pantalla_principal_juego
def main():
    pygame.init()
    pygame.mixer.init()
    pantalla_principal_juego()
    pygame.quit()
if __name__ == "__main__":
    main()