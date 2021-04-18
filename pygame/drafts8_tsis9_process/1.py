import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AppleGrub')
font1 = pygame.font.SysFont('Times New Roman', 60)
font2 = pygame.font.SysFont('dejavuserif', 30)
mainCycle = False
menuCycle = True
screen.fill((102, 0, 102))

while menuCycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuCycle = False
    greeting = font1.render('Hello to AppleGrub Game', True, (255, 255, 0))
    n_players = font2.render('Choose number of players', True, (153, 204, 0))
    screen.blit(greeting, (95, 150))
    screen.blit(n_players, (200, 300))
    one_p = pygame.image.load('one_p.png')
    one_p_rect = one_p.get_rect(bottomright=(330, 600))
    screen.blit(one_p, one_p_rect)
    two_p = pygame.image.load('two_p.png')
    two_p_rect = two_p.get_rect(bottomright=(600, 600))
    screen.blit(two_p, two_p_rect)
    pygame.display.flip()


while mainCycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainCycle = False

    screen.fill((255, 255, 255))
    pygame.display.flip()
