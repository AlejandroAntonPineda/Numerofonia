import pygame
import colors
import founts
import screen
import square
import sys

pygame.init()

def title():
    text = founts.font2.render("NUMEROFONÍA DE ASCHERO", True, colors.BLACK)
    text_pos = (150, 100)
    screen.screen.blit(text, text_pos)


def subtitle():
    text4 = founts.font4.render("Programa de Alejandro Anton Pineda", True, colors.BLACK)
    text_pos4 = (150, 150)
    screen.screen.blit(text4, text_pos4)


def instrunctions():
    text2 = founts.font2.render("Instrucciones", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 600, 50
    screen.screen.blit(text2, text_pos2)


def red_color():
    text2 = founts.font2.render("1", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 600, 100
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.RED,
                     pygame.Rect(screen.screen_size[0] - 580, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 580, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def orange_color():
    text2 = founts.font2.render("2", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 530, 100
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.ORANGE,
                     pygame.Rect(screen.screen_size[0] - 510, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 510, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def yellow_color():
    text2 = founts.font2.render("3", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 460, 100
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.YELLOW,
                     pygame.Rect(screen.screen_size[0] - 440, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 440, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def lime_color():
    text2 = founts.font2.render("4", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 390, 100
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.LIME,
                     pygame.Rect(screen.screen_size[0] - 370, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 370, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def green_color():
    text2 = founts.font2.render("5", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 320, 100
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.GREEN,
                     pygame.Rect(screen.screen_size[0] - 300, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 300, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def esmerald_color():
    text2 = founts.font2.render("6", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 250, 100
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.ESMERALD,
                     pygame.Rect(screen.screen_size[0] - 230, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 230, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def cyan_color():
    text2 = founts.font2.render("7", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 600, 150
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.CYAN,
                     pygame.Rect(screen.screen_size[0] - 580, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 580, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def cobalt_color():
    text2 = founts.font2.render("8", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 530, 150
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.COBALT,
                     pygame.Rect(screen.screen_size[0] - 510, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 510, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def blue_color():
    text2 = founts.font2.render("9", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 460, 150
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.BLUE,
                     pygame.Rect(screen.screen_size[0] - 440, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 440, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def violet_color():
    text2 = founts.font2.render("q", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 390, 150
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.VIOLET,
                     pygame.Rect(screen.screen_size[0] - 370, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 370, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def magenta_color():
    text2 = founts.font2.render("w", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 325, 150
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.MAGENTA,
                     pygame.Rect(screen.screen_size[0] - 300, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 300, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def purple_color():
    text2 = founts.font2.render("e", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 250, 150
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.PURPLE,
                     pygame.Rect(screen.screen_size[0] - 230, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 230, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def black_color():
    text2 = founts.font2.render(".", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 600, 195
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 580, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 580, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def division_line():
    text2 = founts.font2.render("-", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 530, 200
    screen.screen.blit(text2, text_pos2)
    start_line = screen.screen_size[0] - 498, 200
    end_line = screen.screen_size[0] - 498, 223
    pygame.draw.line(screen.screen, colors.BLACK, start_line, end_line, 2)
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 510, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def tie():
    text2 = founts.font2.render(",", True, colors.BLACK)
    text_pos2 = screen.screen_size[0] - 460, 200
    screen.screen.blit(text2, text_pos2)
    pygame.draw.rect(screen.screen, colors.BLACK,
                     pygame.Rect(screen.screen_size[0] - 440, 215, square.LIG_SIZE[0], square.LIG_SIZE[1]), 2)


def esc():
    text3 = founts.font3.render("exit = esc", True, colors.BLACK)
    text_pos3 = screen.screen_size[0] - 380, 205
    screen.screen.blit(text3, text_pos3)
    pygame.display.update()


def directions():
    vertices = (screen.screen_size[0] - 700, 140), (screen.screen_size[0] - 680, 140), (screen.screen_size[0] - 690, 120)
    tri_up = pygame.draw.polygon(screen.screen, colors.BLACK, vertices)
    pygame.draw.line(screen.screen, colors.BLACK, (screen.screen_size[0] - 690, 140), (screen.screen_size[0] - 690, 145), 4)
    vertices = (screen.screen_size[0] - 710, 150), (screen.screen_size[0] - 710, 170), (screen.screen_size[0] - 730, 160)
    tri_left = pygame.draw.polygon(screen.screen, colors.BLACK, vertices)
    pygame.draw.line(screen.screen, colors.BLACK, (screen.screen_size[0] - 710, 160), (screen.screen_size[0] - 705, 160), 4)
    vertices = (screen.screen_size[0] - 670, 150), (screen.screen_size[0] - 670, 170), (screen.screen_size[0] - 650, 160)
    tri_right = pygame.draw.polygon(screen.screen, colors.BLACK, vertices)
    pygame.draw.line(screen.screen, colors.BLACK, (screen.screen_size[0] - 670, 160), (screen.screen_size[0] - 675, 160), 4)
    vertices = (screen.screen_size[0] - 700, 180), (screen.screen_size[0] - 680, 180), (screen.screen_size[0] - 690, 200)
    tri_down = pygame.draw.polygon(screen.screen, colors.BLACK, vertices)
    pygame.draw.line(screen.screen, colors.BLACK, (screen.screen_size[0] - 690, 180), (screen.screen_size[0] - 690, 175), 4)


def up_limits():
    start_line_2 = (screen.screen_size[0] - 200, 320)
    end_line_2 = (screen.screen_size[0] - 1400, 320)
    start_line_3 = (screen.screen_size[0] - 200, 700)
    rect_up = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
    return rect_up


rect_up = up_limits()


def down_limits():
    start_line_2 = (screen.screen_size[0] - 200, 200)
    end_line_2 = (screen.screen_size[0] - 1400, 200)
    start_line_3 = (screen.screen_size[0] - 200, 600)
    rect_down = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
    return rect_down


rect_down = down_limits()


def right_limits():
    start_line_2 = (screen.screen_size[0] - 320, 200)
    end_line_2 = (screen.screen_size[0] - 1400, 200)
    start_line_3 = (screen.screen_size[0] - 320, 700)
    rect_right = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
    return rect_right


rect_right = right_limits()


def left_limits():
    start_line_2 = (screen.screen_size[0] - 200, 200)
    end_line_2 = (screen.screen_size[0] - 1260, 200)
    start_line_3 = (screen.screen_size[0] - 200, 700)
    rect_left = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
    return rect_left


rect_left = left_limits()


def visible_limits():
    start_line_21 = screen.screen_size[0] - 200, 240
    end_line_21 = screen.screen_size[0] - 1370, 240
    start_line_31 = screen.screen_size[0] - 200, 700
    rect = (end_line_21[0], end_line_21[1], start_line_21[0] - end_line_21[0], start_line_31[1] - start_line_21[1])
    pygame.draw.rect(screen.screen, colors.BLACK, rect, 4)


def screen_img():
    start_line_21 = screen.screen_size[0] - 200, 240
    end_line_21 = screen.screen_size[0] - 1370, 240
    start_line_31 = screen.screen_size[0] - 200, 700
    altura = abs(start_line_21[1] - start_line_31[1])
    ancho = abs(start_line_21[0] - end_line_21[0])
    rect_img = (ancho, altura)
    rect_surface = pygame.Surface(rect_img)
    return rect_surface, rect_img

rect_surface = screen_img()
rect_img = screen_img()

def img_print():
    rect_surface.blit(screen.screen, (0, 0), rect_img)
    pygame.image.save(rect_surface, "captura_pantalla.png")
    pygame.quit()
    sys.exit()

