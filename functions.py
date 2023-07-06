import pygame
import sys
import screen
import count
import colors
import square
import maquetado
import blink


def square_print():
    if count.minus_count == 0:
        pygame.draw.rect(screen.screen, colors.current_color,
                         pygame.Rect(square.square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
        square.square_positions.append(square.square_pos)
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE),
                         2)
        pygame.display.update()
    if count.minus_count == 1:
        square.square_pos = (square.square_pos[0] + 25, square.square_pos[1])
        pygame.draw.rect(screen.screen, colors.current_color,
                         pygame.Rect(square.square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
        pygame.draw.rect(screen.screen, colors.BLACK,
                         pygame.Rect(square.square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
        square.square_pos = (square.square_pos[0] - 25, square.square_pos[1])
        square.square_positions.append(square.square_pos)
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE / 2, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE / 2,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.display.update()


def white_square():
    if count.minus_count == 0:
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        square.square_pos = (square.square_pos[0] + 70, square.square_pos[1])
        pygame.display.update()
    if count.minus_count == 1:
        square.square_pos = (square.square_pos[0] + 25, square.square_pos[1])
        pygame.draw.rect(screen.screen, colors.BLACK, pygame.Rect(square.square_pos,
                                                                  (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
        square.square_pos = (square.square_pos[0] - 25, square.square_pos[1])
        square.square_positions.append(square.square_pos)
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE / 2, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE / 2,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        square.square_pos = (square.square_pos[0] + 70, square.square_pos[1])
        pygame.display.update()


def square_mouse():
    mouse_pos = pygame.mouse.get_pos()
    square.square_pos = mouse_pos
    pygame.draw.rect(screen.screen, colors.BLACK,
                     (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
    square.square_positions.append(square.square_pos)
    pygame.display.update()


def print_comma():
    if count.comma_count == 0:
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        square.square_pos = (square.square_pos[0] + 50, square.square_pos[1] + 35)
        pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect(square.square_pos, square.LIG_SIZE))
        pygame.display.flip()
        pygame.draw.line(screen.screen, colors.BLACK, square.square_pos,
                         (square.square_pos[0] + square.LIG_SIZE[0], square.square_pos[1]), 2)
        pygame.draw.line(screen.screen, colors.BLACK, (square.square_pos[0], square.square_pos[1] + square.LIG_SIZE[1]),
                         (square.square_pos[0] + square.LIG_SIZE[0], square.square_pos[1] + square.LIG_SIZE[1]), 2)
        square.square_pos = (square.square_pos[0] + 20, square.square_pos[1] - 35)
        pygame.display.update()
        count.minus_count = 0
        count.oct_count = 0
        count.comma_count += 1
    elif count.comma_count == 1:
        square.square_pos = (square.square_pos[0], square.square_pos[1] + 35)
        pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect(square.square_pos, square.LIG_SIZE_2))
        pygame.display.flip()
        pygame.draw.line(screen.screen, colors.BLACK, square.square_pos,
                         (square.square_pos[0] + square.LIG_SIZE_2[0], square.square_pos[1]), 2)
        pygame.draw.line(screen.screen, colors.BLACK, (square.square_pos[0], square.square_pos[1] + square.LIG_SIZE[1]),
                         (square.square_pos[0] + square.LIG_SIZE_2[0], square.square_pos[1] + square.LIG_SIZE[1]), 2)
        square.square_pos = (square.square_pos[0] + 70, square.square_pos[1] - 35)
        pygame.display.update()
        count.minus_count = 0
        count.oct_count = 0


def octave():
    if count.oct_count == 0:
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE),
                         2)
        square.square_pos = (square.square_pos[0] + 17, square.square_pos[1] - 16)
        pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect
                         (square.square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
        square.square_positions.append(square.square_pos)
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
        square.square_pos = (square.square_pos[0] - 17, square.square_pos[1] + 16)
        pygame.display.update()
    elif count.oct_count == 1:
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        square.square_pos = (square.square_pos[0] + 7, square.square_pos[1] - 16)
        pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect(square.square_pos,
                                                                          (square.OCT_SIZE, square.OCT_SIZE)))
        square.square_positions.append(square.square_pos)
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
        square.square_pos = (square.square_pos[0] - 7, square.square_pos[1] + 16)
        pygame.display.update()
        count.oct_count += 1
    elif count.oct_count == 2:
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        square.square_pos = (square.square_pos[0] + 30, square.square_pos[1] - 16)
        pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect(square.square_pos,
                                                                          (square.OCT_SIZE, square.OCT_SIZE)))
        square.square_positions.append(square.square_pos)
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
        square.square_pos = (square.square_pos[0] - 30, square.square_pos[1] + 16)
        pygame.display.update()
        count.oct_count += 1
    elif count.oct_count == 3:
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        square.square_pos = (square.square_pos[0] + 7, square.square_pos[1] - 16)
        pygame.draw.rect(screen.screen, colors.WHITE, pygame.Rect
                         (square.square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
        square.square_positions.append(square.square_pos)
        pygame.draw.rect(screen.screen, colors.WHITE,
                         (square.square_pos[0], square.square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
        square.square_pos = (square.square_pos[0] - 7, square.square_pos[1] + 16)
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        square.square_pos = (square.square_pos[0] + 30, square.square_pos[1] - 16)
        pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect(square.square_pos,
                                                                          (square.OCT_SIZE, square.OCT_SIZE)))
        square.square_positions.append(square.square_pos)
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
        square.square_pos = (square.square_pos[0] - 30, square.square_pos[1] + 16)
        pygame.display.update()


def division():
    if count.minus_count == 0:
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE / 2, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE / 2,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.display.update()
        count.minus_count += 1
        count.oct_count += 1
    elif count.minus_count == 1:
        pygame.draw.line(screen.screen, colors.current_color,
                         (square.square_pos[0] + square.SQUARE_SIZE / 2, square.square_pos[1] + 2),
                         (square.square_pos[0] + square.SQUARE_SIZE / 2,
                          square.square_pos[1] + square.SQUARE_SIZE - 3), 2)
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE / 3, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE / 3,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE * 2 // 3, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE * 2 / 3,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.display.update()
        count.minus_count += 1
    elif count.minus_count == 2:
        pygame.draw.line(screen.screen, colors.current_color,
                         (square.square_pos[0] + square.SQUARE_SIZE // 3, square.square_pos[1] + 2),
                         (square.square_pos[0] + square.SQUARE_SIZE // 3,
                          square.square_pos[1] + square.SQUARE_SIZE - 3), 2)
        pygame.draw.line(screen.screen, colors.current_color,
                         (square.square_pos[0] + square.SQUARE_SIZE * 2 // 3, square.square_pos[1] + 2),
                         (square.square_pos[0] + square.SQUARE_SIZE * 2 // 3,
                          square.square_pos[1] + square.SQUARE_SIZE - 3), 2)
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE // 4, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE // 4,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE // 2, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE // 2,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.draw.line(screen.screen, colors.BLACK,
                         (square.square_pos[0] + square.SQUARE_SIZE * 3 // 4, square.square_pos[1]),
                         (square.square_pos[0] + square.SQUARE_SIZE * 3 // 4,
                          square.square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.display.update()


def erase():
    if pygame.Rect.colliderect(square.square_marg, maquetado.rect_left):
        pygame.draw.rect(screen.screen, (255, 255, 255),
                         (square.square_pos[0], square.square_pos[1] - 35,
                          square.SQUARE_SIZE + 20, square.SQUARE_SIZE + 35))
        square.square_pos = (square.square_pos[0] - 70, square.square_pos[1])
        square.square_marg = pygame.draw.rect(screen.screen, blink.draw_outline,
                                              (square.square_pos[0], square.square_pos[1],
                                               square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        count.minus_count = 0
        count.oct_count = 0
        count.comma_count = 0
    else:
        pygame.draw.rect(screen.screen, (255, 255, 255),
                         (square.square_pos[0], square.square_pos[1] - 35,
                          square.SQUARE_SIZE + 20, square.SQUARE_SIZE + 35))
        count.minus_count = 0
        count.oct_count = 0
        count.comma_count = 0


def visible_limits():
    start_line_21 = screen.screen_size[0] - 200, 240
    end_line_21 = screen.screen_size[0] - 1370, 240
    start_line_31 = screen.screen_size[0] - 200, 700
    rect = (end_line_21[0], end_line_21[1], start_line_21[0] - end_line_21[0], start_line_31[1] - start_line_21[1])
    pygame.draw.rect(screen.screen, colors.BLACK, rect, 4)


def saved_screen():
    start_line_21 = screen.screen_size[0] - 200, 240
    end_line_21 = screen.screen_size[0] - 1370, 240
    start_line_31 = screen.screen_size[0] - 200, 700
    rect = (end_line_21[0], end_line_21[1], start_line_21[0] - end_line_21[0], start_line_31[1] - start_line_21[1])
    pygame.draw.rect(screen.screen, colors.BLACK, rect, 4)
    altura = abs(start_line_21[1] - start_line_31[1])
    ancho = abs(start_line_21[0] - end_line_21[0])
    rect_img = (ancho, altura)
    rect_surface = pygame.Surface(rect_img)
    return rect_surface, rect


rect_surface, rect = saved_screen()


def save():
    rect_surface.blit(screen.screen, (0, 0), rect)
    pygame.image.save(rect_surface, "captura_pantalla.png")
    pygame.quit()
    sys.exit()
