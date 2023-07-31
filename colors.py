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
    # Obtener el color del píxel en las coordenadas (x, y) de la superficie "screen"
    color = screen.screen.get_at((x, y))

    return color


# value = 0
# increment = 1
# color = (value, value, value)
#
# while current_color != color:
#     # Incrementar o decrementar el valor de 'value'
#     value += increment
#
#     # Asegurarse de que 'value' esté dentro del rango de 0 a 255
#     value = max(0, min(255, value))
#
#     # Actualizar el color con el nuevo valor de 'value'
#     color = (value, value, value)
#
#     # Aquí puedes usar 'color' para lo que necesites, como actualizar la apariencia de un elemento en pantalla
#
#     # Comparar solo los componentes de color gris de 'current_color' y 'color'
#     if current_color[0] == color[0] and current_color[1] == color[1] and current_color[2] == color[2]:
#         break
#
#     # Cambiar la dirección del incremento cuando llegamos a los límites (0 o 255)
#     if value == 255:
#         increment = -1
#     elif value == 0:
#         increment = 1
