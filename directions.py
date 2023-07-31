import pygame
import screen
import count
import colors
import square
import maquetado
import blink


def right_movement():
    if pygame.Rect.colliderect(square.square_marg, maquetado.rect_right):
        square.square_pos = (square.square_pos[0] + 70, square.square_pos[1])
        if screen.screen.get_at((square.square_pos[0] - 65, square.square_pos[1] + 5)) == colors.WHITE:
            pygame.draw.rect(screen.screen, colors.WHITE,
                             (square.square_pos[0] - 70, square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE),
                             2)
            square.square_marg = pygame.draw.rect(screen.screen, blink.draw_outline,
                                                  (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE,
                                                   square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0
        if screen.screen.get_at((square.square_pos[0] - 65, square.square_pos[1] + 5)) != colors.WHITE:
            pygame.draw.rect(screen.screen, colors.BLACK,
                             (square.square_pos[0] - 70, square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE),
                             2)
            square.square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                                                  (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE,
                                                   square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0


def left_movement():
    if pygame.Rect.colliderect(square.square_marg, maquetado.rect_left):
        square.square_pos = (square.square_pos[0] - 70, square.square_pos[1])
        if screen.screen.get_at((square.square_pos[0] + 75, square.square_pos[1] + 5)) == colors.WHITE:
            pygame.draw.rect(screen.screen, colors.WHITE,
                             (square.square_pos[0] + 70, square.square_pos[1],
                              square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                                                  (square.square_pos[0], square.square_pos[1],
                                                   square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0
        if screen.screen.get_at((square.square_pos[0] + 75, square.square_pos[1] + 5)) != colors.WHITE:
            pygame.draw.rect(screen.screen, colors.BLACK,
                             (square.square_pos[0] + 70, square.square_pos[1],
                              square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                                                  (square.square_pos[0], square.square_pos[1],
                                                   square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0


def down_movement():
    if pygame.Rect.colliderect(square.square_marg, maquetado.rect_down):
        square.square_pos = (square.square_pos[0], square.square_pos[1] + 70)
        if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] - 65)) == colors.WHITE:
            pygame.draw.rect(screen.screen, colors.WHITE,
                             (square.square_pos[0], square.square_pos[1] - 70,
                              square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                                                  (square.square_pos[0], square.square_pos[1],
                                                   square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0
        if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] - 65)) != colors.WHITE:
            pygame.draw.rect(screen.screen, colors.BLACK,
                             (square.square_pos[0], square.square_pos[1] - 70,
                              square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                                                  (square.square_pos[0], square.square_pos[1],
                                                   square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0


def up_movement():
    if pygame.Rect.colliderect(square.square_marg, maquetado.rect_up):
        square.square_pos = (square.square_pos[0], square.square_pos[1] - 70)
        if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 75)) == colors.WHITE:
            pygame.draw.rect(screen.screen, colors.WHITE,
                             (square.square_pos[0], square.square_pos[1] + 70,
                              square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                                                  (square.square_pos[0], square.square_pos[1],
                                                   square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0
        if screen.screen.get_at((square.square_pos[0] + 5, square.square_pos[1] + 75)) != colors.WHITE:
            pygame.draw.rect(screen.screen, colors.BLACK,
                             (square.square_pos[0], square.square_pos[1] + 70,
                              square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_marg = pygame.draw.rect(screen.screen, colors.BLACK,
                                                  (square.square_pos[0], square.square_pos[1],
                                                   square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.minus_count = 0
            count.oct_count = 0
            count.comma_count = 0
            count.tresillo_count = 0
            count.semicorchea_count = 0


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
        count.tresillo_count = 0
        count.semicorchea_count = 0
    else:
        pygame.draw.rect(screen.screen, (255, 255, 255),
                         (square.square_pos[0], square.square_pos[1] - 35,
                          square.SQUARE_SIZE + 20, square.SQUARE_SIZE + 35))
        count.minus_count = 0
        count.oct_count = 0
        count.comma_count = 0
        count.tresillo_count = 0
        count.semicorchea_count = 0


# def square_mouse():
#     mouse_pos = pygame.mouse.get_pos()
#     square.square_pos = mouse_pos
#     pygame.draw.rect(screen.screen, colors.BLACK,
#                      (square.square_pos[0], square.square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
#     square.square_positions.append(square.square_pos)
#     pygame.display.update()

