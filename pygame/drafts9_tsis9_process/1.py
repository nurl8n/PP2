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
font = pygame.font.SysFont('Arial', 30)

screen.fill(WHITE)

while overall:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            overall = False
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

    pygame.display.flip()
