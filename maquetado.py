import pygame
import colors
import founts
import screen
import square

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
    text_pos2 = screen_size[0] - 600, 195
    screen.blit(text2, text_pos2)
    pygame.draw.rect(screen, colors.BLACK,
                     pygame.Rect(screen_size[0] - 580, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
    pygame.draw.rect(screen, colors.BLACK,
                     pygame.Rect(screen_size[0] - 580, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def division_line():
    text2 = founts.font2.render("-", True, colors.BLACK)
    text_pos2 = screen_size[0] - 530, 200
    screen.blit(text2, text_pos2)
    start_line = screen_size[0] - 498, 200
    end_line = screen_size[0] - 498, 223
    pygame.draw.line(screen, colors.BLACK, start_line, end_line, 2)
    pygame.draw.rect(screen, colors.BLACK,
                     pygame.Rect(screen_size[0] - 510, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)


def tie():
    text2 = founts.font2.render(",", True, colors.BLACK)
    text_pos2 = screen_size[0] - 460, 200
    screen.blit(text2, text_pos2)
    pygame.draw.rect(screen, colors.BLACK,
                     pygame.Rect(screen_size[0] - 440, 215, square.LIG_SIZE[0], square.LIG_SIZE[1]), 2)


def esc():
    text3 = founts.font3.render("exit = esc", True, colors.BLACK)
    text_pos3 = screen_size[0] - 380, 205
    screen.blit(text3, text_pos3)
    pygame.display.update()