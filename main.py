# importar e iniciar
import pygame
import sys
import os
import colors
import functions
import screen
import sounds
import maquetado
import blink
import directions

print(sys.path)
pygame.init()
directorio_actual = os.getcwd()
print("prev_positions.txt:", directorio_actual)


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
maquetado.octave()
maquetado.esc()
maquetado.directions()
# limites
maquetado.up_limits()
maquetado.down_limits()
maquetado.right_limits()
maquetado.left_limits()
# Definir límites visibles
maquetado.visible_limits()
# Surface
maquetado.saved_screen()
# parpadeo
blink.blink()


while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                maquetado.save()

            if event.key == pygame.K_1:
                colors.current_color = colors.RED
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_2:
                colors.current_color = colors.ORANGE
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_3:
                colors.current_color = colors.YELLOW
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_4:
                colors.current_color = colors.LIME
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_5:
                colors.current_color = colors.GREEN
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_6:
                colors.current_color = colors.ESMERALD
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_7:
                colors.current_color = colors.CYAN
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_8:
                colors.current_color = colors.COBALT
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_9:
                colors.current_color = colors.BLUE
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_q:
                colors.current_color = colors.VIOLET
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_w:
                colors.current_color = colors.MAGENTA
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_e:
                colors.current_color = colors.PURPLE
                functions.semicorchea()
                functions.tresillo()
                functions.square_print()

            if event.key == pygame.K_PERIOD:
                colors.current_color = colors.BLACK
                functions.square_print()

            # capoeira berimbao
            if event.key == pygame.K_a:
                colors.current_color = colors.BROWN
                functions.square_print()
            if event.key == pygame.K_s:
                colors.current_color = colors.COBALT
                functions.square_print()
            if event.key == pygame.K_d:
                colors.current_color = colors.GREEN
                functions.square_print()
            # capoeira berimbao

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
                directions.erase()

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

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()

        # if count.minus_count == 2:
        #     target_color = colors.current_color
        #     connected_pixel_count = functions.count_connected_pixels(screen.screen, square.square_pos[0] + 20,
        #                                                              square.square_pos[1] + 5, target_color)
        #     print("Cantidad de píxeles contiguos del mismo color:", connected_pixel_count)
