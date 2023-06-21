import pygame
from pygame import mixer
import screen
import square
import colors

pygame.init()
mixer.init()

do = pygame.mixer.Sound('do.wav')
re = pygame.mixer.Sound('re.wav')
mi = pygame.mixer.Sound('mi.wav')
fa = pygame.mixer.Sound('fa.wav')
sol = pygame.mixer.Sound('sol.wav')
la = pygame.mixer.Sound('la.wav')
si = pygame.mixer.Sound('si.wav')


def sounds():
    if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 5)) == colors.RED:
        do.play()
    if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 5)) == colors.YELLOW:
        re.play()
    if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 5)) == colors.GREEN:
        mi.play()
    if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 5)) == colors.ESMERALD:
        fa.play()
    if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 5)) == colors.COBALT:
        sol.play()
    if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 5)) == colors.VIOLET:
        la.play()
    if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 5)) == colors.PURPLE:
        si.play()
