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
radius = 50
screen.fill(WHITE)
mode = BLACK
go3 = True
draw_on3 = False
firstPos = (0, 0)

def drawCircle(screen, start, width, color):
  a = start[0]
  b = start[1]
  pygame.draw.circle(screen, color, (a, b), width)

while go3:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      go3 = False
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
      draw_on3 = True
      firstPos = event.pos
    if event.type == pygame.MOUSEBUTTONUP:
      if draw_on3:
        drawCircle(screen, firstPos, radius, mode)
  pygame.display.flip()
