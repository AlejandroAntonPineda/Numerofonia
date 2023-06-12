# importar e iniciar
import pygame
import sys

print(sys.path)
pygame.init()

# Pantalla
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
screen_size = screen.get_size()

# Colores
RED = (213, 0, 0)
ORANGE = (245, 124, 0)
YELLOW = (255, 235, 59)
LIME = (205, 220, 57)
GREEN = (46, 125, 50)
ESMERALDA = (0, 131, 143)
CIAN = (77, 208, 225)
COBALTO = (21, 101, 192)
AZUL = (26, 35, 126)
VIOLETA = (94, 53, 177)
Magenta = (156, 39, 176)
Purple = (224, 64, 251)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Current_color = RED
ALL_COLORS = [RED, ORANGE, YELLOW, LIME, GREEN, ESMERALDA,
              CIAN, COBALTO, AZUL, VIOLETA, Magenta, Purple]

# Definir sonidos

# Definir variables del cuadrado cuadrado
SQUARE_SIZE = 50
square_pos = (screen_size[0] - 1340, 260)
square_marg = pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)), 2)
LIG_SIZE = (20, 13)
OCT_SIZE = 15

square_positions = []


# Fuentes
font = pygame.font.Font(None, 45)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 30)
font4 = pygame.font.Font(None, 20)
# Titulo
text = font.render("NUMEROFONÍA DE ASCHERO", True, BLACK)
text_pos = (150, 100)
screen.blit(text, text_pos)
# Subtítulo
text4 = font4.render("Programa de Alejandro Anton Pineda", True, BLACK)
text_pos4 = (150, 150)
screen.blit(text4, text_pos4)
# Texto Instrucciones
text2 = font2.render("Instrucciones", True, BLACK)
text_pos2 = screen_size[0] - 600, 50
screen.blit(text2, text_pos2)

# Instrucciones
# 1 Color Rojo
text2 = font2.render("1", True, BLACK)
text_pos2 = screen_size[0] - 600, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, RED, pygame.Rect(screen_size[0] - 580, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 580, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 2 Color Naranja
text2 = font2.render("2", True, BLACK)
text_pos2 = screen_size[0] - 530, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, ORANGE, pygame.Rect(screen_size[0] - 510, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 510, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 3 Color Amarillo
text2 = font2.render("3", True, BLACK)
text_pos2 = screen_size[0] - 460, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, YELLOW, pygame.Rect(screen_size[0] - 440, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 440, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 4 Color Lima
text2 = font2.render("4", True, BLACK)
text_pos2 = screen_size[0] - 390, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, LIME, pygame.Rect(screen_size[0] - 370, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 370, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 5 Color Verde
text2 = font2.render("5", True, BLACK)
text_pos2 = screen_size[0] - 320, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, GREEN, pygame.Rect(screen_size[0] - 300, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 300, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 6 Color Esmeralda
text2 = font2.render("6", True, BLACK)
text_pos2 = screen_size[0] - 250, 100
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, ESMERALDA, pygame.Rect(screen_size[0] - 230, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 230, 100, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 7 Color Cian
text2 = font2.render("7", True, BLACK)
text_pos2 = screen_size[0] - 600, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, CIAN, pygame.Rect(screen_size[0] - 580, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 580, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 8 Color Cobalto
text2 = font2.render("8", True, BLACK)
text_pos2 = screen_size[0] - 530, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, COBALTO, pygame.Rect(screen_size[0] - 510, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 510, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# 9 Color Azul
text2 = font2.render("9", True, BLACK)
text_pos2 = screen_size[0] - 460, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, AZUL, pygame.Rect(screen_size[0] - 440, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 440, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# q color Violeta
text2 = font2.render("q", True, BLACK)
text_pos2 = screen_size[0] - 390, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, VIOLETA, pygame.Rect(screen_size[0] - 370, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 370, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# w color Magenta
text2 = font2.render("w", True, BLACK)
text_pos2 = screen_size[0] - 325, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, Magenta, pygame.Rect(screen_size[0] - 300, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 300, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# e color purple
text2 = font2.render("e", True, BLACK)
text_pos2 = screen_size[0] - 250, 150
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, Purple, pygame.Rect(screen_size[0] - 230, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 230, 150, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# . color negro - silencio
text2 = font2.render(".", True, BLACK)
text_pos2 = screen_size[0] - 600, 195
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 580, 200, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 580, 200, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# - linea divisoria
text2 = font2.render("-", True, BLACK)
text_pos2 = screen_size[0] - 530, 200
screen.blit(text2, text_pos2)
start_line = screen_size[0] - 498, 200
end_line = screen_size[0] - 498, 223
pygame.draw.line(screen, BLACK, start_line, end_line, 2)
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 510, 200, SQUARE_SIZE / 2, SQUARE_SIZE / 2), 2)
# , ligadura
text2 = font2.render(",", True, BLACK)
text_pos2 = screen_size[0] - 460, 200
screen.blit(text2, text_pos2)
pygame.draw.rect(screen, BLACK, pygame.Rect(screen_size[0] - 440, 215, LIG_SIZE[0], LIG_SIZE[1]), 2)
# salir
text3 = font3.render("exit = esc", True, BLACK)
text_pos3 = screen_size[0] - 380, 205
screen.blit(text3, text_pos3)
pygame.display.update()

# triángulos
vertices = (screen_size[0] - 700, 140), (screen_size[0] - 680, 140), (screen_size[0] - 690, 120)
tri_up = pygame.draw.polygon(screen, BLACK, vertices)
pygame.draw.line(screen, BLACK, (screen_size[0] - 690, 140), (screen_size[0] - 690, 145), 4)
vertices = (screen_size[0] - 710, 150), (screen_size[0] - 710, 170), (screen_size[0] - 730, 160)
tri_left = pygame.draw.polygon(screen, BLACK, vertices)
pygame.draw.line(screen, BLACK, (screen_size[0] - 710, 160), (screen_size[0] - 705, 160), 4)
vertices = (screen_size[0] - 670, 150), (screen_size[0] - 670, 170), (screen_size[0] - 650, 160)
tri_right = pygame.draw.polygon(screen, BLACK, vertices)
pygame.draw.line(screen, BLACK, (screen_size[0] - 670, 160), (screen_size[0] - 675, 160), 4)
vertices = (screen_size[0] - 700, 180), (screen_size[0] - 680, 180), (screen_size[0] - 690, 200)
tri_down = pygame.draw.polygon(screen, BLACK, vertices)
pygame.draw.line(screen, BLACK, (screen_size[0] - 690, 180), (screen_size[0] - 690, 175), 4)

# Parpadeo
draw_outline = BLACK
BLINK_INTERVAL = 1000
BLINK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BLINK_EVENT, BLINK_INTERVAL)

# Contador
minus_count = 0
oct_count = 0


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
pygame.draw.rect(screen, BLACK, rect, 4)
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
                Current_color = RED
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_2:
                Current_color = ORANGE
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_3:
                Current_color = YELLOW
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_4:
                Current_color = LIME
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_5:
                Current_color = GREEN
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_6:
                Current_color = ESMERALDA
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_7:
                Current_color = CIAN
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_8:
                Current_color = COBALTO
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_9:
                Current_color = AZUL
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_q:
                Current_color = VIOLETA
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_w:
                Current_color = Magenta
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_e:
                Current_color = Purple
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_PERIOD:
                Current_color = BLACK
                if minus_count == 0:
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE, SQUARE_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    pygame.display.update()
                if minus_count == 1:
                    square_pos = (square_pos[0] + 25, square_pos[1])
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)))
                    pygame.draw.rect(screen, BLACK, pygame.Rect(square_pos, (SQUARE_SIZE / 2, SQUARE_SIZE)), 2)
                    square_pos = (square_pos[0] - 25, square_pos[1])
                    square_positions.append(square_pos)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()

            if event.key == pygame.K_COMMA:
                pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                square_pos = (square_pos[0] + 50, square_pos[1] + 35)
                pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, LIG_SIZE))
                pygame.display.flip()
                pygame.draw.line(screen, BLACK, square_pos, (square_pos[0] + LIG_SIZE[0], square_pos[1]), 2)
                pygame.draw.line(screen, BLACK, (square_pos[0], square_pos[1] + LIG_SIZE[1]),
                                 (square_pos[0] + LIG_SIZE[0], square_pos[1] + LIG_SIZE[1]), 2)
                square_pos = (square_pos[0] + 20, square_pos[1] - 35)
                pygame.display.update()
                minus_count = 0

            if event.key == pygame.K_o:
                if minus_count == 0:
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 17, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (OCT_SIZE, OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], OCT_SIZE, OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 17, square_pos[1] + 16)
                    pygame.display.update()
                elif minus_count == 1:
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 7, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (OCT_SIZE, OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], OCT_SIZE, OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 7, square_pos[1] + 16)
                    pygame.display.update()
                    minus_count += 1
                elif minus_count == 2:
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 30, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (OCT_SIZE, OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], OCT_SIZE, OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 30, square_pos[1] + 16)
                    pygame.display.update()
                    minus_count += 1
                elif minus_count == 3:
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 7, square_pos[1] - 16)
                    pygame.draw.rect(screen, WHITE, pygame.Rect(square_pos, (OCT_SIZE, OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, WHITE, (square_pos[0], square_pos[1], OCT_SIZE, OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 7, square_pos[1] + 16)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    square_pos = (square_pos[0] + 30, square_pos[1] - 16)
                    pygame.draw.rect(screen, Current_color, pygame.Rect(square_pos, (OCT_SIZE, OCT_SIZE)))
                    square_positions.append(square_pos)
                    pygame.draw.rect(screen, BLACK, (square_pos[0], square_pos[1], OCT_SIZE, OCT_SIZE), 2)
                    square_pos = (square_pos[0] - 30, square_pos[1] + 16)
                    pygame.display.update()

            if event.key == pygame.K_MINUS:
                if minus_count == 0:
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                    minus_count += 1
                elif minus_count == 1:
                    pygame.draw.line(screen, Current_color, (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + 2),
                                     (square_pos[0] + SQUARE_SIZE / 2, square_pos[1] + SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE / 3, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE / 3, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE * 2 // 3, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE * 2 / 3, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                    minus_count += 1
                elif minus_count == 2:
                    pygame.draw.line(screen, Current_color, (square_pos[0] + SQUARE_SIZE // 3, square_pos[1] + 2),
                                     (square_pos[0] + SQUARE_SIZE // 3, square_pos[1] + SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, Current_color, (square_pos[0] + SQUARE_SIZE * 2 // 3, square_pos[1] + 2),
                                     (square_pos[0] + SQUARE_SIZE * 2 // 3, square_pos[1] + SQUARE_SIZE - 3), 2)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE // 4, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE // 4, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE // 2, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE // 2, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.draw.line(screen, BLACK, (square_pos[0] + SQUARE_SIZE * 3 // 4, square_pos[1]),
                                     (square_pos[0] + SQUARE_SIZE * 3 // 4, square_pos[1] + SQUARE_SIZE - 2), 2)
                    pygame.display.update()
                    minus_count = 0

            if event.key == pygame.K_BACKSPACE:
                if pygame.Rect.colliderect(square_marg, rect_left):
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (square_pos[0], square_pos[1] - 35, SQUARE_SIZE + 20, SQUARE_SIZE + 35))
                    square_pos = (square_pos[0] - 70, square_pos[1])
                    square_marg = pygame.draw.rect(screen, draw_outline,
                                                   (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                    minus_count = 0
                else:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (square_pos[0], square_pos[1], SQUARE_SIZE + 20, SQUARE_SIZE))
                    minus_count = 0

            if event.key == pygame.K_RIGHT:
                if pygame.Rect.colliderect(square_marg, rect_right):
                    square_pos = (square_pos[0] + 70, square_pos[1])
                    if screen.get_at((square_pos[0] - 65, square_pos[1] + 5)) == WHITE:
                        pygame.draw.rect(screen, WHITE,
                                         (square_pos[0] - 70, square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, draw_outline,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                    if screen.get_at((square_pos[0] - 65, square_pos[1] + 5)) != WHITE:
                        pygame.draw.rect(screen, BLACK,
                                         (square_pos[0] - 70, square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, BLACK,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0

            if event.key == pygame.K_LEFT:
                if pygame.Rect.colliderect(square_marg, rect_left):
                    square_pos = (square_pos[0] - 70, square_pos[1])
                    if screen.get_at((square_pos[0] + 75, square_pos[1] + 5)) == WHITE:
                        pygame.draw.rect(screen, WHITE,
                                         (square_pos[0] + 70, square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, BLACK,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                    if screen.get_at((square_pos[0] + 75, square_pos[1] + 5)) != WHITE:
                        pygame.draw.rect(screen, BLACK,
                                         (square_pos[0] + 70, square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, BLACK,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0

            if event.key == pygame.K_DOWN:
                if pygame.Rect.colliderect(square_marg, rect_down):
                    square_pos = (square_pos[0], square_pos[1] + 70)
                    if screen.get_at((square_pos[0] + 5, square_pos[1] - 65)) == WHITE:
                        pygame.draw.rect(screen, WHITE,
                                         (square_pos[0], square_pos[1] - 70, SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, BLACK,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                    if screen.get_at((square_pos[0] + 5, square_pos[1] - 65)) != WHITE:
                        pygame.draw.rect(screen, BLACK,
                                         (square_pos[0], square_pos[1] - 70, SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, BLACK,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0

            if event.key == pygame.K_UP:
                if pygame.Rect.colliderect(square_marg, rect_up):
                    square_pos = (square_pos[0], square_pos[1] - 70)
                    if screen.get_at((square_pos[0] + 5, square_pos[1] + 75)) == WHITE:
                        pygame.draw.rect(screen, WHITE,
                                         (square_pos[0], square_pos[1] + 70, SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, BLACK,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0
                    if screen.get_at((square_pos[0] + 5, square_pos[1] + 75)) != WHITE:
                        pygame.draw.rect(screen, BLACK,
                                         (square_pos[0], square_pos[1] + 70, SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_marg = pygame.draw.rect(screen, BLACK,
                                                       (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
                        square_positions.append(square_pos)
                        pygame.display.update()
                        minus_count = 0

        elif event.type == BLINK_EVENT:
            draw_outline = WHITE if draw_outline == BLACK else BLACK
            pygame.draw.rect(screen, draw_outline, (square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE), 2)
            pygame.display.update()
