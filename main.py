# importar e iniciar
import pygame
import sys
import colors
import functions
import screen
import sounds
import maquetado
import blink
import directions

print(sys.path)
pygame.init()

# pantalla principal
screen.main_screen()

# maquetado
maquetado.title()
maquetado.subtitle()
maquetado.instrunctions()
# maquetado - instructions
maquetado.red_color()
maquetado.orange_color()
maquetado.yellow_color()
maquetado.lime_color()
maquetado.green_color()
maquetado.esmerald_color()
maquetado.cyan_color()
maquetado.cobalt_color()
maquetado.blue_color()
maquetado.violet_color()
maquetado.magenta_color()
maquetado.purple_color()
maquetado.black_color()
maquetado.division_line()
maquetado.tie()
maquetado.esc()
maquetado.directions()
# limites
maquetado.up_limits()
maquetado.down_limits()
maquetado.right_limits()
maquetado.left_limits()
# Definir límites visibles
functions.visible_limits()
# Surface
functions.saved_screen()
# parpadeo
blink.blink()

while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                functions.save()

            if event.key == pygame.K_1:
                colors.current_color = colors.RED
                functions.square_print()

            if event.key == pygame.K_2:
                colors.current_color = colors.ORANGE
                functions.square_print()

            if event.key == pygame.K_3:
                colors.current_color = colors.YELLOW
                functions.square_print()

            if event.key == pygame.K_4:
                colors.current_color = colors.LIME
                functions.square_print()

            if event.key == pygame.K_5:
                colors.current_color = colors.GREEN
                functions.square_print()

            if event.key == pygame.K_6:
                colors.current_color = colors.ESMERALD
                functions.square_print()
            if event.key == pygame.K_7:
                colors.current_color = colors.CYAN
                functions.square_print()

            if event.key == pygame.K_8:
                colors.current_color = colors.COBALT
                functions.square_print()

            if event.key == pygame.K_9:
                colors.current_color = colors.BLUE
                functions.square_print()

            if event.key == pygame.K_q:
                colors.current_color = colors.VIOLET
                functions.square_print()

            if event.key == pygame.K_w:
                colors.current_color = colors.MAGENTA
                functions.square_print()

            if event.key == pygame.K_e:
                colors.current_color = colors.PURPLE
                functions.square_print()

            if event.key == pygame.K_PERIOD:
                current_color = colors.BLACK
                functions.square_print()

            if event.key == pygame.K_0:
                functions.white_square()

            if event.key == pygame.K_COMMA:
                functions.print_comma()

            if event.key == pygame.K_o:
                functions.octave()

            if event.key == pygame.K_MINUS:
                functions.division()

            if event.key == pygame.K_BACKSPACE:
                current_color = colors.WHITE
                functions.erase()

            if event.key == pygame.K_RIGHT:
                current_color = colors.WHITE
                directions.right_movement()

            if event.key == pygame.K_LEFT:
                current_color = colors.WHITE
                directions.left_movement()

            if event.key == pygame.K_DOWN:
                current_color = colors.WHITE
                directions.down_movement()

            if event.key == pygame.K_UP:
                current_color = colors.WHITE
                directions.up_movement()

            sounds.sounds()

        elif event.type == blink.BLINK_EVENT:
            blink.blink()
