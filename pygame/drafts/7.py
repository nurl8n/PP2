import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My First Game')
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
FPS = 55
PI = 3.14
flag = True
color = (255, 0, 0)
x, y = 50, 50
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
dx = 10
dy = 3


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

    pos = pygame.mouse.get_pos()
    print(pos)
    color = RED if flag else BLUE

    x += dx
    y += dy

    if x + 100 > SCREEN_WIDTH:
        dx *= -1
        flag = not flag

    if x == 0:
        dx *= -1

    if y + 100 > SCREEN_HEIGHT or y < 0:
        dy *= -1


    screen.fill(WHITE)

    pygame.draw.rect(screen, color, (x, y, 100, 100))

    pygame.display.flip()


    clock.tick(FPS)

pygame.quit()









