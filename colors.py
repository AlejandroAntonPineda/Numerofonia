import pygame

pygame.init()


# Colores
RED = (213, 0, 0)
ORANGE = (245, 124, 0)
YELLOW = (255, 235, 59)
LIME = (205, 220, 57)
GREEN = (46, 125, 50)
ESMERALD = (0, 131, 143)
CYAN = (77, 208, 225)
COBALT = (21, 101, 192)
BLUE = (26, 35, 126)
VIOLET = (94, 53, 177)
MAGENTA = (156, 39, 176)
PURPLE = (224, 64, 251)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (101, 67, 33)
current_color = WHITE

all_colors = [RED, ORANGE, YELLOW, LIME, GREEN, ESMERALD,
              CYAN, COBALT, BLUE, VIOLET, MAGENTA, PURPLE]


def obtener_color_pixel(screen, x, y):
    color = screen.screen.get_at((x, y))

    return color
