import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
screen_size = screen.get_size()


def main_screen():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen_size = screen.get_size()
