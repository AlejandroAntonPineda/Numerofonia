# importar e iniciar
import pygame
import sys
import colors
import functions
import sounds
import square
import maquetado

print(sys.path)
pygame.init()

# Pantalla
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
screen_size = screen.get_size()

# Colores
current_color = colors.WHITE

# Definir posiciones del cuadrado
square_positions = []
square_pos = (screen_size[0] - 1340, 260)
square_marg = pygame.draw.rect(screen, colors.BLACK,
                               pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)), 2)
# cuenta
minus_count = 0
oct_count = 0
comma_count = 0

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
start_line_21 = screen_size[0] - 200, 240
end_line_21 = screen_size[0] - 1370, 240
start_line_31 = screen_size[0] - 200, 700
rect = (end_line_21[0], end_line_21[1], start_line_21[0] - end_line_21[0], start_line_31[1] - start_line_21[1])
pygame.draw.rect(screen, colors.BLACK, rect, 4)
# Surface
altura = abs(start_line_21[1] - start_line_31[1])
ancho = abs(start_line_21[0] - end_line_21[0])
rect_img = (ancho, altura)
rect_surface = pygame.Surface(rect_img)

# Parpadeo
draw_outline = colors.BLACK
BLINK_INTERVAL = 1000
BLINK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BLINK_EVENT, BLINK_INTERVAL)

while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                rect_surface.blit(screen, (0, 0), rect)
                pygame.image.save(rect_surface, "captura_pantalla.png")
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_1:
                colors.current_color = colors.RED
                functions.square_print()

            if event.key == pygame.K_2:
                current_color = colors.ORANGE
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK,
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_3:
                current_color = colors.YELLOW
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK,
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_4:
                current_color = colors.LIME
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK,
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_5:
                current_color = colors.GREEN
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_6:
                current_color = colors.ESMERALD
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_7:
                current_color = colors.CYAN
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_8:
                current_color = colors.COBALT
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_9:
                current_color = colors.BLUE
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_q:
                current_color = colors.VIOLET
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_w:
                current_color = colors.MAGENTA
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_e:
                current_color = colors.PURPLE
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_PERIOD:
                current_color = colors.BLACK
                if minus_count == 0:
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_0:
                if minus_count == 0:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 70, square_pos[1])
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    square_pos = (square_pos[0] + 70, square_pos[1])
                    pygame.display.update()

            if event.key == pygame.K_COMMA:
                if comma_count == 0:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 50, square_pos[1] + 35)
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, square.LIG_SIZE))
                    pygame.display.flip()
                    pygame.draw.line(screen, colors.BLACK, square_pos, (square_pos[0] + square.LIG_SIZE[0], square_pos[1]), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0], square_pos[1] + square.LIG_SIZE[1]),
                                     (square_pos[0] + square.LIG_SIZE[0], square_pos[1] + square.LIG_SIZE[1]), 2)
                    square_pos = (square_pos[0] + 20, square_pos[1] - 35)
                    pygame.display.update()
                    minus_count = 0
                    oct_count = 0
                    comma_count += 1
                elif comma_count == 1:
                    square_pos = (square_pos[0], square_pos[1] + 35)
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, square.LIG_SIZE_2))
                    pygame.display.flip()
                    pygame.draw.line(screen, colors.BLACK, square_pos,
                                     (square_pos[0] + square.LIG_SIZE_2[0], square_pos[1]), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0], square_pos[1] + square.LIG_SIZE[1]),
                                     (square_pos[0] + square.LIG_SIZE_2[0], square_pos[1] + square.LIG_SIZE[1]), 2)
                    square_pos = (square_pos[0] + 70, square_pos[1] - 35)
                    pygame.display.update()
                    minus_count = 0
                    oct_count = 0

            if event.key == pygame.K_o:
                if oct_count == 0:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 17, square_pos[1] - 16)
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 17, square_pos[1] + 16)
                    pygame.display.update()
                elif oct_count == 1:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 7, square_pos[1] - 16)
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 7, square_pos[1] + 16)
                    pygame.display.update()
                    oct_count += 1
                elif oct_count == 2:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 30, square_pos[1] - 16)
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 30, square_pos[1] + 16)
                    pygame.display.update()
                    oct_count += 1
                elif oct_count == 3:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 7, square_pos[1] - 16)
                    pygame.draw.rect(screen, colors.WHITE, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.WHITE, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 7, square_pos[1] + 16)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 30, square_pos[1] - 16)
                    pygame.draw.rect(screen, current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 30, square_pos[1] + 16)
                    pygame.display.update()

            if event.key == pygame.K_MINUS:
                if minus_count == 0:
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                    minus_count += 1
                    oct_count += 1
                elif minus_count == 1:
                    pygame.draw.line(screen, current_color, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + 2),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 3, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 3, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE * 2 // 3, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE * 2 / 3, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                    minus_count += 1
                elif minus_count == 2:
                    pygame.draw.line(screen, current_color, (square_pos[0] + square.SQUARE_SIZE // 3, square_pos[1] + 2),
                                     (square_pos[0] + square.SQUARE_SIZE // 3, square_pos[1] + square.SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, current_color, (square_pos[0] + square.SQUARE_SIZE * 2 // 3, square_pos[1] + 2),
                                     (square_pos[0] + square.SQUARE_SIZE * 2 // 3, square_pos[1] + square.SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE // 4, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE // 4, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE // 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE // 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE * 3 // 4, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE * 3 // 4, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_BACKSPACE:
                current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, maquetado.rect_left):
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (square_pos[0], square_pos[1] - 35, square.SQUARE_SIZE + 20, square.SQUARE_SIZE + 35))
                    square_pos = (square_pos[0] - 70, square_pos[1])
                    square_marg = pygame.draw.rect(screen, draw_outline,
                                                   (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    minus_count = 0
                    oct_count = 0
                    comma_count = 0
                else:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE + 20, square.SQUARE_SIZE))
                    minus_count = 0
                    oct_count = 0
                    comma_count = 0

            if event.key == pygame.K_RIGHT:
                current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, maquetado.rect_right):
                    square_pos = (square_pos[0] + 70, square_pos[1])
                    if screen.get_at((square_pos[0] - 65, square_pos[1] + 5)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0] - 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, draw_outline,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] - 65, square_pos[1] + 5)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0] - 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if event.key == pygame.K_LEFT:
                current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, maquetado.rect_left):
                    square_pos = (square_pos[0] - 70, square_pos[1])
                    if screen.get_at((square_pos[0] + 75, square_pos[1] + 5)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0] + 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] + 75, square_pos[1] + 5)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0] + 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if event.key == pygame.K_DOWN:
                current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, maquetado.rect_down):
                    square_pos = (square_pos[0], square_pos[1] + 70)
                    if screen.get_at((square_pos[0] + 5, square_pos[1] - 65)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0], square_pos[1] - 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] + 5, square_pos[1] - 65)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0], square_pos[1] - 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if event.key == pygame.K_UP:
                current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, maquetado.rect_up):
                    square_pos = (square_pos[0], square_pos[1] - 70)
                    if screen.get_at((square_pos[0] + 5, square_pos[1] + 75)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0], square_pos[1] + 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] + 5, square_pos[1] + 75)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0], square_pos[1] + 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.RED:
                sounds.do.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.YELLOW:
                sounds.re.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.GREEN:
                sounds.mi.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.ESMERALD:
                sounds.fa.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.COBALT:
                sounds.sol.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.VIOLET:
                sounds.la.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.PURPLE:
                sounds.si.play()

        elif event.type == BLINK_EVENT:
            draw_outline = colors.WHITE if draw_outline == colors.BLACK else colors.BLACK
            pygame.draw.rect(screen, draw_outline, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            pygame.display.update()
