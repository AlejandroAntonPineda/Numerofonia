# importar e iniciar
import pygame
import sys
import colors
import sounds
import square


print(sys.path)
pygame.init()

# Pantalla
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
screen_size = screen.get_size()
# Colores
Current_color = colors.WHITE
# Definir posiciones del cuadrado
square_positions = []
square_pos = (screen_size[0] - 1340, 260)
square_marg = pygame.draw.rect(screen, colors.BLACK,
                               pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)), 2)
# Fuentes
font = pygame.font.Font(None, 45)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 30)
font4 = pygame.font.Font(None, 20)
# Titulo
text = font.render("NUMEROFONÍA DE ASCHERO", True, colors.BLACK)
text_pos = (150, 100)
screen.blit(text, text_pos)
# Subtítulo
text4 = font4.render("Programa de Alejandro Anton Pineda", True, colors.BLACK)
text_pos4 = (150, 150)
screen.blit(text4, text_pos4)
# Texto Instrucciones
text2 = font2.render("Instrucciones", True, colors.BLACK)
text_pos2 = screen_size[0] - 600, 50
screen.blit(text2, text_pos2)
# Instrucciones
# 1 Color Rojo
text2 = font2.render("1", True, colors.BLACK)
text_pos2 = screen_size[0] - 600, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.RED,
                 pygame.Rect(screen_size[0] - 580, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 580, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 2 Color Naranja
text2 = font2.render("2", True, colors.BLACK)
text_pos2 = screen_size[0] - 530, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.ORANGE,
                 pygame.Rect(screen_size[0] - 510, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 510, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 3 Color Amarillo
text2 = font2.render("3", True, colors.BLACK)
text_pos2 = screen_size[0] - 460, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.YELLOW,
                 pygame.Rect(screen_size[0] - 440, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 440, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 4 Color Lima
text2 = font2.render("4", True, colors.BLACK)
text_pos2 = screen_size[0] - 390, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.LIME,
                 pygame.Rect(screen_size[0] - 370, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 370, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 5 Color Verde
text2 = font2.render("5", True, colors.BLACK)
text_pos2 = screen_size[0] - 320, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.GREEN,
                 pygame.Rect(screen_size[0] - 300, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 300, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 6 Color Esmeralda
text2 = font2.render("6", True, colors.BLACK)
text_pos2 = screen_size[0] - 250, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.ESMERALD,
                 pygame.Rect(screen_size[0] - 230, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 230, 100, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 7 Color Cian
text2 = font2.render("7", True, colors.BLACK)
text_pos2 = screen_size[0] - 600, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.CYAN,
                 pygame.Rect(screen_size[0] - 580, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 580, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 8 Color Cobalto
text2 = font2.render("8", True, colors.BLACK)
text_pos2 = screen_size[0] - 530, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.COBALT,
                 pygame.Rect(screen_size[0] - 510, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 510, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# 9 Color Azul
text2 = font2.render("9", True, colors.BLACK)
text_pos2 = screen_size[0] - 460, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.BLUE,
                 pygame.Rect(screen_size[0] - 440, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 440, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# q color Violeta
text2 = font2.render("q", True, colors.BLACK)
text_pos2 = screen_size[0] - 390, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.VIOLET,
                 pygame.Rect(screen_size[0] - 370, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 370, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# w color Magenta
text2 = font2.render("w", True, colors.BLACK)
text_pos2 = screen_size[0] - 325, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.MAGENTA,
                 pygame.Rect(screen_size[0] - 300, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 300, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# e color purple
text2 = font2.render("e", True, colors.BLACK)
text_pos2 = screen_size[0] - 250, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.PURPLE,
                 pygame.Rect(screen_size[0] - 230, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 230, 150, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# . color negro - silencio
text2 = font2.render(".", True, colors.BLACK)
text_pos2 = screen_size[0] - 600, 195
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 580, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2))
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 580, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# - linea divisoria
text2 = font2.render("-", True, colors.BLACK)
text_pos2 = screen_size[0] - 530, 200
screen.blit(text2, text_pos2)
start_line = screen_size[0] - 498, 200
end_line = screen_size[0] - 498, 223
pygame.draw.line(screen, colors.BLACK, start_line, end_line, 2)
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 510, 200, square.SQUARE_SIZE / 2, square.SQUARE_SIZE / 2), 2)
# , ligadura
text2 = font2.render(",", True, colors.BLACK)
text_pos2 = screen_size[0] - 460, 200
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, colors.BLACK,
                 pygame.Rect(screen_size[0] - 440, 215, square.LIG_SIZE[0], square.LIG_SIZE[1]), 2)
# salir
text3 = font3.render("exit = esc", True, colors.BLACK)
text_pos3 = screen_size[0] - 380, 205
screen.blit(text3, text_pos3)
pygame.display.update()
# triángulos
vertices = (screen_size[0] - 700, 140), (screen_size[0] - 680, 140), (screen_size[0] - 690, 120)
tri_up = pygame.draw.polygon(screen, colors.BLACK, vertices)
pygame.draw.line(screen, colors.BLACK, (screen_size[0] - 690, 140), (screen_size[0] - 690, 145), 4)
vertices = (screen_size[0] - 710, 150), (screen_size[0] - 710, 170), (screen_size[0] - 730, 160)
tri_left = pygame.draw.polygon(screen, colors.BLACK, vertices)
pygame.draw.line(screen, colors.BLACK, (screen_size[0] - 710, 160), (screen_size[0] - 705, 160), 4)
vertices = (screen_size[0] - 670, 150), (screen_size[0] - 670, 170), (screen_size[0] - 650, 160)
tri_right = pygame.draw.polygon(screen, colors.BLACK, vertices)
pygame.draw.line(screen, colors.BLACK, (screen_size[0] - 670, 160), (screen_size[0] - 675, 160), 4)
vertices = (screen_size[0] - 700, 180), (screen_size[0] - 680, 180), (screen_size[0] - 690, 200)
tri_down = pygame.draw.polygon(screen, colors.BLACK, vertices)
pygame.draw.line(screen, colors.BLACK, (screen_size[0] - 690, 180), (screen_size[0] - 690, 175), 4)
# Parpadeo
draw_outline = colors.BLACK
BLINK_INTERVAL = 1000
BLINK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BLINK_EVENT, BLINK_INTERVAL)
# Contador
minus_count = 0
oct_count = 0
comma_count = 0
# Definir límites arriba
start_line_2 = screen_size[0] - 200, 320
end_line_2 = screen_size[0] - 1400, 320
start_line_3 = screen_size[0] - 200, 700
rect_up = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
#  Definir limites abajo
start_line_2 = screen_size[0] - 200, 200
end_line_2 = screen_size[0] - 1400, 200
start_line_3 = screen_size[0] - 200, 600
rect_down = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
#  Definir limites derecha
start_line_2 = screen_size[0] - 320, 200
end_line_2 = screen_size[0] - 1400, 200
start_line_3 = screen_size[0] - 320, 700
rect_right = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
#  Definir limites izquierda
start_line_2 = screen_size[0] - 200, 200
end_line_2 = screen_size[0] - 1260, 200
start_line_3 = screen_size[0] - 200, 700
rect_left = (end_line_2[0], end_line_2[1], start_line_2[0] - end_line_2[0], start_line_3[1] - start_line_2[1])
# Definir límites visibles
start_line_21 = screen_size[0] - 200, 240
end_line_21 = screen_size[0] - 1370, 240
start_line_31 = screen_size[0] - 200, 700
rect = (end_line_21[0], end_line_21[1], start_line_21[0] - end_line_21[0], start_line_31[1] - start_line_21[1])
pygame.draw.rect(screen, colors.BLACK, rect, 4)
# Surface
altura = abs(start_line_21[1] - start_line_31[1])
ancho = abs(start_line_21[0] - end_line_21[0])
rect_img = (ancho, altura)
rect_surface = pygame.Surface(rect_img)

while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                rect_surface.blit(screen, (0, 0), rect)
                pygame.image.save(rect_surface, "captura_pantalla.png")
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_1:
                Current_color = colors.RED
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK,
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_2:
                Current_color = colors.ORANGE
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK,
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_3:
                Current_color = colors.YELLOW
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK,
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_4:
                Current_color = colors.LIME
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color,
                                     pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK,
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_5:
                Current_color = colors.GREEN
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_6:
                Current_color = colors.ESMERALD
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_7:
                Current_color = colors.CYAN
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_8:
                Current_color = colors.COBALT
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_9:
                Current_color = colors.BLUE
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_q:
                Current_color = colors.VIOLET
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_w:
                Current_color = colors.MAGENTA
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_e:
                Current_color = colors.PURPLE
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_PERIOD:
                Current_color = colors.BLACK
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE, square.SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)))
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_0:
                if minus_count == 0:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 70, square_pos[1])
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(square_pos, (square.SQUARE_SIZE / 2, square.SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    square_pos = (square_pos[0] + 70, square_pos[1])
                    pygame.display.update()

            if event.key == pygame.K_COMMA:
                if comma_count == 0:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 50, square_pos[1] + 35)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, square.LIG_SIZE))
                    pygame.display.flip()
                    pygame.draw.line(screen, colors.BLACK, square_pos, (square_pos[0] + square.LIG_SIZE[0], square_pos[1]), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0], square_pos[1] + square.LIG_SIZE[1]),
                                     (square_pos[0] + square.LIG_SIZE[0], square_pos[1] + square.LIG_SIZE[1]), 2)
                    square_pos = (square_pos[0] + 20, square_pos[1] - 35)
                    pygame.display.update()
                    minus_count = 0
                    oct_count = 0
                    comma_count += 1
                elif comma_count == 1:
                    square_pos = (square_pos[0], square_pos[1] + 35)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, square.LIG_SIZE_2))
                    pygame.display.flip()
                    pygame.draw.line(screen, colors.BLACK, square_pos,
                                     (square_pos[0] + square.LIG_SIZE_2[0], square_pos[1]), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0], square_pos[1] + square.LIG_SIZE[1]),
                                     (square_pos[0] + square.LIG_SIZE_2[0], square_pos[1] + square.LIG_SIZE[1]), 2)
                    square_pos = (square_pos[0] + 70, square_pos[1] - 35)
                    pygame.display.update()
                    minus_count = 0
                    oct_count = 0

            if event.key == pygame.K_o:
                if oct_count == 0:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 17, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 17, square_pos[1] + 16)
                    pygame.display.update()
                elif oct_count == 1:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 7, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 7, square_pos[1] + 16)
                    pygame.display.update()
                    oct_count += 1
                elif oct_count == 2:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 30, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 30, square_pos[1] + 16)
                    pygame.display.update()
                    oct_count += 1
                elif oct_count == 3:
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 7, square_pos[1] - 16)
                    pygame.draw.rect(screen, colors.WHITE, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.WHITE, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 7, square_pos[1] + 16)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 30, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (square.OCT_SIZE, square.OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, colors.BLACK, (square_pos[0], square_pos[1], square.OCT_SIZE, square.OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 30, square_pos[1] + 16)
                    pygame.display.update()

            if event.key == pygame.K_MINUS:
                if minus_count == 0:
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                    minus_count += 1
                    oct_count += 1
                elif minus_count == 1:
                    pygame.draw.line(screen, Current_color, (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + 2),
                                     (square_pos[0] + square.SQUARE_SIZE / 2, square_pos[1] + square.SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE / 3, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE / 3, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE * 2 // 3, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE * 2 / 3, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                    minus_count += 1
                elif minus_count == 2:
                    pygame.draw.line(screen, Current_color, (square_pos[0] + square.SQUARE_SIZE // 3, square_pos[1] + 2),
                                     (square_pos[0] + square.SQUARE_SIZE // 3, square_pos[1] + square.SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, Current_color, (square_pos[0] + square.SQUARE_SIZE * 2 // 3, square_pos[1] + 2),
                                     (square_pos[0] + square.SQUARE_SIZE * 2 // 3, square_pos[1] + square.SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE // 4, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE // 4, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE // 2, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE // 2, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, colors.BLACK, (square_pos[0] + square.SQUARE_SIZE * 3 // 4, square_pos[1]),
                                     (square_pos[0] + square.SQUARE_SIZE * 3 // 4, square_pos[1] + square.SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_BACKSPACE:
                Current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, rect_left):
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (square_pos[0], square_pos[1] - 35, square.SQUARE_SIZE + 20, square.SQUARE_SIZE + 35))
                    square_pos = (square_pos[0] - 70, square_pos[1])
                    square_marg = pygame.draw.rect(screen, draw_outline,
                                                   (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                    minus_count = 0
                    oct_count = 0
                    comma_count = 0
                else:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (square_pos[0], square_pos[1], square.SQUARE_SIZE + 20, square.SQUARE_SIZE))
                    minus_count = 0
                    oct_count = 0
                    comma_count = 0

            if event.key == pygame.K_RIGHT:
                Current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, rect_right):
                    square_pos = (square_pos[0] + 70, square_pos[1])
                    if screen.get_at((square_pos[0] - 65, square_pos[1] + 5)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0] - 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, draw_outline,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] - 65, square_pos[1] + 5)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0] - 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if event.key == pygame.K_LEFT:
                Current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, rect_left):
                    square_pos = (square_pos[0] - 70, square_pos[1])
                    if screen.get_at((square_pos[0] + 75, square_pos[1] + 5)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0] + 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] + 75, square_pos[1] + 5)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0] + 70, square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if event.key == pygame.K_DOWN:
                Current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, rect_down):
                    square_pos = (square_pos[0], square_pos[1] + 70)
                    if screen.get_at((square_pos[0] + 5, square_pos[1] - 65)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0], square_pos[1] - 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] + 5, square_pos[1] - 65)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0], square_pos[1] - 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if event.key == pygame.K_UP:
                Current_color = colors.WHITE
                if pygame.Rect.colliderect(square_marg, rect_up):
                    square_pos = (square_pos[0], square_pos[1] - 70)
                    if screen.get_at((square_pos[0] + 5, square_pos[1] + 75)) == colors.WHITE:
                        pygame.draw.rect(screen, colors.WHITE,
                                         (square_pos[0], square_pos[1] + 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0
                    if screen.get_at((square_pos[0] + 5, square_pos[1] + 75)) != colors.WHITE:
                        pygame.draw.rect(screen, colors.BLACK,
                                         (square_pos[0], square_pos[1] + 70, square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, colors.BLACK,
                                                       (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                        oct_count = 0
                        comma_count = 0

            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.RED:
                sounds.do.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.YELLOW:
                sounds.re.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.GREEN:
                sounds.mi.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.ESMERALD:
                sounds.fa.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.COBALT:
                sounds.sol.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.VIOLET:
                sounds.la.play()
            if screen.get_at((square_pos[0] + 5, square_pos[1] + 5)) == colors.PURPLE:
                sounds.si.play()

        elif event.type == BLINK_EVENT:
            draw_outline = colors.WHITE if draw_outline == colors.BLACK else colors.BLACK
            pygame.draw.rect(screen, draw_outline, (square_pos[0], square_pos[1], square.SQUARE_SIZE, square.SQUARE_SIZE), 2)
            pygame.display.update()
