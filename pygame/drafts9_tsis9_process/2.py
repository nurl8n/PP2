import pygame
pygame.init()

# 9 colors
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
eraserBool = False
font = pygame.font.SysFont('Arial', 30)
eraser1, eraser1_cur = None, None

screen.fill(WHITE)

while overall:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            overall = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            if 600 < prev[0] < 632 and 20 < prev[1] < 52:
                overall = False
            if 670 < prev[0] < 702 and 20 < prev[1] < 52:
                overall = False
            if 740 < prev[0] < 772 and 20 < prev[1] < 52:
                # overall = False
                eraserBool = True


    if eraserBool:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                eraser1 = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                eraser1_cur = pygame.mouse.get_pos()
                if eraser1:
                    pygame.draw.line(screen, RED, eraser1, eraser1_cur, 3)
                    eraser1 = eraser1_cur
            if event.type == pygame.MOUSEBUTTONUP:
                eraser1 = None
    pygame.draw.line(screen, BLACK, (0, 140), (1000, 140), 3)
    greeting = pygame.Surface((520, 50))
    greeting.fill(ORANGE)
    hello = font.render('Welcome to Paint of Vincent Van Gogh', True, BLACK)
    greeting.blit(hello, (10, 10))
    screen.blit(greeting, (10, 10))

    greeting2 = pygame.Surface((280, 50))
    greeting2.fill(ORANGE)
    hello2 = font.render('Manage and Create', True, BLACK)
    greeting2.blit(hello2, (10, 10))
    screen.blit(greeting2, (10, 70))

    rectangle = pygame.image.load('rectangle.png')
    circle = pygame.image.load('circle.png')
    eraser = pygame.image.load('eraser.png')

    rectangle2 = rectangle.get_rect(bottomright=(632, 52))
    circle2 = circle.get_rect(bottomright=(702, 52))
    eraser2 = eraser.get_rect(bottomright=(772, 52))
    screen.blit(rectangle, rectangle2)
    screen.blit(circle, circle2)
    screen.blit(eraser, eraser2)

    clock.tick(30)

    pygame.image.save(screen, 'surface.png')
    pygame.display.flip()
