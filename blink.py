import colors
import pygame
import screen
import square


pygame.init()

draw_outline = colors.BLACK
BLINK_INTERVAL = 1000
BLINK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BLINK_EVENT, BLINK_INTERVAL)


def blink():
    global draw_outline
    draw_outline = colors.WHITE if draw_outline == colors.BLACK else colors.BLACK
    pygame.draw.rect(screen.screen, draw_outline,
                     (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
    pygame.display.update()


