import pygame
from pygame import mixer
import screen
import square
import colors
import time


pygame.init()
mixer.init()

do = pygame.mixer.Sound('sounds/c.mp3')
re = pygame.mixer.Sound('sounds/d.mp3')
mi = pygame.mixer.Sound('sounds/e.mp3')
fa = pygame.mixer.Sound('sounds/f.mp3')
sol = pygame.mixer.Sound('sounds/g.mp3')
la = pygame.mixer.Sound('sounds/a.mp3')
si = pygame.mixer.Sound('sounds/h.mp3')


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

    time.sleep(1/2)
    corchea()


def corchea():
    if screen.screen.get_at((square.square_pos[0] + 25, square.square_pos[1] + 10)) == colors.BLACK:
        if screen.screen.get_at((square.square_pos[0] + 27, square.square_pos[1] + 5)) == colors.RED:
            do.play()
        if screen.screen.get_at((square.square_pos[0] + 27, square.square_pos[1] + 5)) == colors.YELLOW:
            re.play()
        if screen.screen.get_at((square.square_pos[0] + 27, square.square_pos[1] + 5)) == colors.GREEN:
            mi.play()
        if screen.screen.get_at((square.square_pos[0] + 27, square.square_pos[1] + 5)) == colors.ESMERALD:
            fa.play()
        if screen.screen.get_at((square.square_pos[0] + 27, square.square_pos[1] + 5)) == colors.COBALT:
            sol.play()
        if screen.screen.get_at((square.square_pos[0] + 27, square.square_pos[1] + 5)) == colors.VIOLET:
            la.play()
        if screen.screen.get_at((square.square_pos[0] + 27, square.square_pos[1] + 5)) == colors.PURPLE:
            si.play()
