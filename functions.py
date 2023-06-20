import pygame
import screen
import count
import colors
import square

def square_print():
    if count.minus_count == 0:
        pygame.draw.rect(screen.screen, colors.current_color,
                         pygame.Rect(square.square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
        square.square_positions.append(square.square_pos)
        pygame.draw.rect(screen.screen, colors.BLACK,
                         (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
        pygame.display.update()
    if count.minus_count == 1:
        square_pos = (square.square_pos[0] + 25, square.square_pos[1])
        pygame.draw.rect(screen.screen, colors.current_color,
                         pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
        pygame.draw.rect(screen.screen, colors.BLACK,
                         pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
        square_pos = (square_pos[0] - 25, square_pos[1])
        square.square_positions.append(square_pos)
        pygame.draw.line(screen.screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                         (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
        pygame.display.update()

