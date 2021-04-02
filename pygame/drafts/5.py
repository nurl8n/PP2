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
x, y = 200, 200

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_SPACE:
                flag = not flag
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:    # left arrow
                x -= 5
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:   # right arrow
                x += 5
            elif event.key == pygame.K_UP or event.key == pygame.K_w:      # to do this, language should be en
                y -= 5
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 5

    color = RED if flag else BLUE

    screen.fill(WHITE)

    pygame.draw.rect(screen, color, (x, y, 100, 100))

    pygame.display.flip()


    clock.tick(FPS)

pygame.quit()









