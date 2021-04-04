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
        if event.type == pygame.KEYDOWN:            # pressing the button
            if event.key == pygame.K_SPACE:         # changing the color of rectangle
                if color == RED:
                    color = GREEN
                else:
                    color = RED
    # drawing objects should be before the flipping
    # left and top corners, width and height
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()           # updating to the next frame

pygame.quit()
