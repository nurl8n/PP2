import pygame
pygame.init()
WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 102, 204)
ORANGE = (255, 102, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint for Linux)')
FPS = 30
clock = pygame.time.Clock()
go = False
radius = 1
screen.fill(WHITE)
mode = BLACK
last_pos = (0, 0)
drawLine2, draw_on = True, False


def drawLine(screen, start, end, width, color):
  x1 = start[0]
  y1 = start[1]
  x2 = end[0]
  y2 = end[1]

  dx = abs(x1 - x2)
  dy = abs(y1 - y2)

  A = y2 - y1
  B = x1 - x2
  C = x2 * y1 - x1 * y2

  if dx > dy:
    if x1 > x2:
      x1, x2 = x2, x1
      y1, y2 = y2, y1

    for x in range(x1, x2):
      y = (-C - A * x) / B
      pygame.draw.circle(screen, color, (x, y), width)
  else:
    if y1 > y2:
      x1, x2 = x2, x1
      y1, y2 = y2, y1
    for y in range(y1, y2):
      x = (-C - B * y) / A
      pygame.draw.circle(screen, color, (x, y), width)

screen.fill(WHITE)

while drawLine2:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      drawLine2 = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      prev = pygame.mouse.get_pos()
      if 20 < prev[0] < 52 and 20 < prev[1] < 52:
        go = True
  line = pygame.image.load('line.png')
  rectangle = pygame.image.load('rectangle.png')
  circle = pygame.image.load('circle.png')
  eraser = pygame.image.load('eraser.png')

  line2 = rectangle.get_rect(bottomright=(52, 52))
  rectangle2 = rectangle.get_rect(bottomright=(52, 122))
  circle2 = circle.get_rect(bottomright=(52, 192))
  eraser2 = eraser.get_rect(bottomright=(52, 262))
  screen.blit(line, line2)
  screen.blit(rectangle, rectangle2)
  screen.blit(circle, circle2)
  screen.blit(eraser, eraser2)

  while go:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        drawLine2 = False
        go = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          mode = RED
        if event.key == pygame.K_b:
          mode = BLUE
        if event.key == pygame.K_g:
          mode = GREEN
        if event.key == pygame.K_w:
          mode = WHITE
        if event.key == pygame.K_1:
          mode = BLACK
        if event.key == pygame.K_y:
          mode = YELLOW
        if event.key == pygame.K_p:
          mode = PINK
        if event.key == pygame.K_o:
          mode = ORANGE
        if event.key == pygame.K_UP:
          radius += 1
        if event.key == pygame.K_DOWN:
          radius -= 1
      if event.type == pygame.MOUSEBUTTONDOWN:
        draw_on = True
      if event.type == pygame.MOUSEBUTTONUP:
        draw_on = False
      if event.type == pygame.MOUSEMOTION:
        if draw_on:
          drawLine(screen, last_pos, event.pos, radius, mode)
        last_pos = event.pos

    pygame.display.flip()

  pygame.display.flip()

pygame.quit()


