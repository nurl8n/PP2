import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 102, 204)
PURPLE = (153, 0, 255)
ORANGE = (255, 102, 0)

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Vincent Van Gogh')
overall = True
prev, cur = None, None

screen.fill(WHITE)

while overall:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      overall = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      prev = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEMOTION:
      cur = pygame.mouse.get_pos()
      if prev:
        pygame.draw.line(screen, RED, prev, cur, 1)
        prev = cur
    if event.type == pygame.MOUSEBUTTONUP:
      prev = None

  pygame.display.flip()

  clock.tick(30)

pygame.quit()
