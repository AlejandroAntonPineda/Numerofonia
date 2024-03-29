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
    if count.minus_count == 2:
        if screen.screen.get_at((square.square_pos[0] + 10, square.square_pos[1] + 10)) == colors.current_color:
            pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect
                             (square.square_pos, square.SQUARE_TRES))
            square.square_positions.append(square.square_pos)
            pygame.display.update()
    if count.minus_count == 3:
        if screen.screen.get_at((square.square_pos[0] + 10, square.square_pos[1] + 10)) == colors.current_color\
                and count.square_count == 0:
            pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect(square.square_pos, square.SQUARE_TRES))
            square.square_positions.append(square.square_pos)
            pygame.display.update()
            count.square_count += 1
        # mirar como hacerlo independiente de la funcion semicorchea.
        elif count.square_count == 1:
            color_pixel = colors.obtener_color_pixel(screen, square.square_pos[0] + 15, square.square_pos[1] + 5)
            color_pixel_2 = colors.obtener_color_pixel(screen, square.square_pos[0] + 40, square.square_pos[1] + 5)
            if color_pixel == color_pixel_2:
                pygame.draw.rect(screen.screen, colors.current_color, pygame.Rect
                                 (square.square_pos, square.SQUARE_SEMI))
                square.square_positions.append(square.square_pos)
                pygame.display.update()
                count.square_count += 1


def tresillo():
    color_pixel = colors.obtener_color_pixel(screen, square.square_pos[0] + 20, square.square_pos[1] + 5)
    if count.minus_count == 2 and count.tresillo_count == 0:
        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 20,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()

        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 40,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()

        count.tresillo_count += 1

    elif count.tresillo_count == 1:
        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 40,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()


def semicorchea():
    color_pixel = colors.obtener_color_pixel(screen, square.square_pos[0] + 15, square.square_pos[1] + 5)
    if count.minus_count == 3 and count.semicorchea_count == 0:
        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 15,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()

        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 28,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()

        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 40,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()

        count.semicorchea_count += 1

    elif count.semicorchea_count == 1:
        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 28,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()

        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 40,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
        pygame.display.update()

        count.semicorchea_count += 1

    elif count.semicorchea_count == 2:
        color_pixel = colors.obtener_color_pixel(screen, square.square_pos[0] + 40, square.square_pos[1] + 5)
        connected_pixels = draw_connected_pixels(screen.screen, square.square_pos[0] + 40,
                                                 square.square_pos[1] + 5, color_pixel)
        for pixel in connected_pixels:
            new_color = colors.current_color
            x, y = pixel
            pygame.draw.rect(screen.screen, new_color, pygame.Rect(x, y, 1, 1))
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
        count.minus_count += 1


def visible_limits():
    start_line_21 = screen.screen_size[0] - 200, 240
    end_line_21 = screen.screen_size[0] - 1370, 240
    start_line_31 = screen.screen_size[0] - 200, 700
    rect = (end_line_21[0], end_line_21[1], start_line_21[0] - end_line_21[0], start_line_31[1] - start_line_21[1])
    pygame.draw.rect(screen.screen, colors.BLACK, rect, 4)


def draw_connected_pixels(surface, x, y, target_color, visited=None):
    if visited is None:
        visited = set()
    width, height = surface.get_size()
    if not (0 <= x < width and 0 <= y < height):
        return set()
    if (x, y) in visited:
        return set()
    visited.add((x, y))
    if surface.get_at((x, y)) != target_color:
        return set()
    visited.add((x, y))
    pixels = {(x, y)}
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for neighbor in neighbors:
        nx, ny = neighbor
        pixels.update(draw_connected_pixels(surface, nx, ny, target_color, visited))

    return pixels
