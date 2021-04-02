import pygame
import math
from math import pi, sin, cos

pygame.init()

screen = pygame.display.set_mode((483, 400))
pygame.display.set_caption('Math is Fun')

clock = pygame.time.Clock()
FPS = 60
b = (0, 0, 0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 20)
    text = font.render('0.00', True, (0, 0, 0))
    screen.blit(text, (25, 165))
    text2 = font.render('0.50', True, b)
    text3 = font.render('-0.50', True, b)
    screen.blit(text2, (25, 90))
    screen.blit(text3, (25, 240))
    text4 = font.render('-1.00', True, b)
    text5 = font.render('1.00', True, b)
    screen.blit(text5, (25, 15))
    screen.blit(text4, (25, 305))

    pygame.draw.line(screen, b, (55, 170), (65, 170), 1)
    pygame.draw.line(screen, b, (55, 95), (65, 95), 1)
    pygame.draw.line(screen, b, (55, 245), (65, 245), 1)
    pygame.draw.rect(screen, (0, 0, 0), (60, 20, 363, 300), 2)
    pygame.draw.line(screen, b, (60, 170), (423, 170), 2)
    pygame.draw.line(screen, b, (240, 320), (240, 20), 2)

    text6 = font.render('0', True, b)
    screen.blit(text6, (237.5, 330))

    pygame.draw.line(screen, b, (240.5, 315), (240.5, 325), 1)
    pygame.draw.line(screen, b, (180, 315), (180, 325), 1)
    pygame.draw.line(screen, b, (120, 315), (120, 325), 1)
    pygame.draw.line(screen, b, (302, 315), (302, 325), 1)
    pygame.draw.line(screen, b, (363, 315), (363, 325), 1)
    text7 = font.render('-p', True, b)
    text8 = font.render('-2p', True, b)
    text9 = font.render('-3p', True, b)
    text10 = font.render('p', True, b)
    text11 = font.render('2p', True, b)
    text12 = font.render('3p', True, b)
    screen.blit(text7, (177, 330))
    screen.blit(text8, (117, 330))
    screen.blit(text9, (57, 330))
    screen.blit(text10, (299, 330))
    screen.blit(text11, (360, 330))
    screen.blit(text12, (420, 330))
    text13 = font.render('X', True, b)
    screen.blit(text13, (237.5, 365))

    for x in range(60, 420):
        cos_y1 = 150 * cos((x - 60) / 60 * pi)
        cos_y2 = 150 * cos((x - 59) / 60 * pi)
        pygame.draw.aalines(screen, (0, 0, 255), False, [(x, 170 + cos_y1), ((x + 3), 170 + cos_y2)])

        sin_y1 = 150 * sin((x - 60) / 60 * pi)
        sin_y2 = 150 * sin((x - 59) / 60 * pi)
        pygame.draw.aalines(screen, (255, 0, 0), False, [(x, 170 + sin_y1), ((x + 3), 170 + sin_y2)])

    pygame.display.update()


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

