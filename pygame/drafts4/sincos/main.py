import pygame
from math import pi, sin, cos

pygame.init()
screen = pygame.display.set_mode((800, 600))
isDone = False

while not isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = True
    screen.fill((255, 255, 255))

    for x in range(50, 750):
        sin_y1 = 240 * sin((x-100)/100*pi)
        sin_y2 = 240 * sin((x-99)/100*pi)
        pygame.draw.aalines(screen, (255, 0, 0), True, [(x, 280 + sin_y1), ((x+1), 280 + sin_y2)])

    for x in range(50, 750):
        cos_y1 = 240 * cos((x-100)/100*pi)
        cos_y2 = 240* cos((x-99)/100*pi)
        pygame.draw.aalines(screen, (0, 0, 255), True, [(x, 280 + cos_y1), ((x+1), 280 + cos_y2)])
    pygame.display.update()

pygame.quit()


