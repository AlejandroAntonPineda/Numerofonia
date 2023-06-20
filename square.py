import screen
import pygame
import colors

pygame.init()

SQUARE_SIZE = 50
LIG_SIZE = (20, 13)
LIG_SIZE_2 = (70, 13)
OCT_SIZE = 15
square_pos = (screen.screen_size[0] - 1340, 260)
square_positions = []
square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                               pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)), 2)
