import pygame
pygame.init()
WIDTH, HEIGHT = 1000, 800
ORANGE = (255, 102, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint for Linux)')
radiusEraser = 10
screen.fill((0, 0, 0))
mode = WHITE
go4 = True
lastPos = (0, 0)
draw_on4 = False

def drawEraser(screen, start, end, width, color):
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

while go4:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      go4 = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        radiusEraser += 2
      if event.key == pygame.K_DOWN:
        radiusEraser -= 2
    if event.type == pygame.MOUSEBUTTONDOWN:
      draw_on4 = True
    if event.type == pygame.MOUSEBUTTONUP:
      draw_on4 = False
    if event.type == pygame.MOUSEMOTION:
      if draw_on4:
        drawEraser(screen, lastPos, event.pos, radiusEraser, mode)
      lastPos = event.pos
  pygame.display.flip()
