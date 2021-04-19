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
radius = 1
screen.fill(WHITE)
mode = BLACK
go2 = True
draw_on2 = False
first_pos, second_pos = (0, 0), (0, 0)

def drawRect(screen, end, start, width, color):
  a = start[0]
  b = start[1]
  c = end[0]
  d = end[1]
  x = abs(start[0] - end[0])
  y = abs(start[1] - end[1])
  if a < c and b < d:
    pygame.draw.rect(screen, color, (a, b, x, y))
  if a > c and b > d:
    pygame.draw.rect(screen, color, (c, d, x, y))
  if a > c and b < d:
    pygame.draw.rect(screen, color, (c, b, x, y))
  if a < c and b > d:
    pygame.draw.rect(screen, color, (a, d, x, y))

while go2:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      go2 = False
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
      draw_on2 = True
      first_pos = event.pos
    if event.type == pygame.MOUSEBUTTONUP:
      second_pos = event.pos
      if draw_on2:
        drawRect(screen, second_pos, first_pos, radius, mode)

  pygame.display.flip()
