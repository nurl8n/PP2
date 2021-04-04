import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
done = False

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color = RED

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()          # return tuple of t or f of pressed buttons
    if pressed[pygame.K_SPACE]:
        if color == RED:
            color = GREEN
        else:
            color = RED
    # print(pressed)

    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()

pygame.quit()
