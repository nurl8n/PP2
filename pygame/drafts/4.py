import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My First Game')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
FPS = 60
PI = 3.14
flag = True
color = (255, 0, 0)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:                  # if keyboard is clicked
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_SPACE:               # clicking on PROBEL
                flag = not flag

    # changing the color of rectangle by clicking on K_SPACE
    color = RED if flag else BLUE

    screen.fill(WHITE)

    pygame.draw.rect(screen, color, (50, 50, 100, 100))

    pygame.display.flip()


    clock.tick(FPS)

pygame.quit()









