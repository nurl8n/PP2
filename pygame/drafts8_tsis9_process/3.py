import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AppleGrub')
font1 = pygame.font.SysFont('Times New Roman', 60)
font2 = pygame.font.SysFont('dejavuserif', 30)
font3 = pygame.font.SysFont('arial', 20)
mainCycle = False
menuCycle, menuCycle2, menuCycle3 = True, False, False
screen.fill((102, 0, 102))


while menuCycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuCycle = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            # one player mode
            if 202 < prev[0] < 330 and 472 < prev[1] < 600:
                menuCycle = False
                menuCycle2 = True
            # two player mode
            if 472 < prev[0] < 600 and 472 < prev[1] < 600:
                menuCycle = False

    greeting = font1.render('Hello to AppleGrub Game', True, (255, 255, 0))
    n_players = font2.render('Choose number of players', True, (153, 204, 0))
    screen.blit(greeting, (95, 150))
    screen.blit(n_players, (200, 320))

    one_p = pygame.image.load('one_p.png')
    one_p_rect = one_p.get_rect(bottomright=(330, 600))
    screen.blit(one_p, one_p_rect)
    two_p = pygame.image.load('two_p.png')
    two_p_rect = two_p.get_rect(bottomright=(600, 600))
    screen.blit(two_p, two_p_rect)

    bandersnatch = font3.render('Брандашмыг', True, (0, 0, 255))
    screen.blit(bandersnatch, (345, 870))
    pygame.display.flip()

screen.fill((102, 0, 102))

while menuCycle2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuCycle2 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clr = pygame.mouse.get_pos()
            if 150 < clr[0] < 250 and 400 < clr[1] < 500:
                menuCycle2 = False
                menuCycle3 = True
                colorRgb = (255, 0, 0)
            if 350 < clr[0] < 450 and 400 < clr[1] < 500:
                menuCycle2 = False
                menuCycle3 = True
                colorRgb = (0, 255, 0)
            if 550 < clr[0] < 650 and 400 < clr[1] < 500:
                menuCycle2 = False
                menuCycle3 = True
                colorRgb = (0, 0, 255)
            if 150 < clr[0] < 250 and 600 < clr[1] < 700:
                menuCycle2 = False
                menuCycle3 = True
                colorRgb = (255, 255, 0)
            if 350 < clr[0] < 450 and 600 < clr[1] < 700:
                menuCycle2 = False
                menuCycle3 = True
                colorRgb = (255, 102, 255)
            if 550 < clr[0] < 650 and 600 < clr[1] < 700:
                menuCycle2 = False
                menuCycle3 = True
                colorRgb = (255, 153, 0)

    choosingColor = font2.render('Choose color of your AppleGrub', True, (153, 204, 0))
    screen.blit(choosingColor, (157, 200))
    one_p1 = pygame.Surface((100, 100))
    one_p1.fill((255, 0, 0))
    one_p2 = pygame.Surface((100, 100))
    one_p2.fill((0, 255, 0))
    one_p3 = pygame.Surface((100, 100))
    one_p3.fill((0, 0, 255))
    one_p4 = pygame.Surface((100, 100))
    one_p4.fill((255, 255, 0))
    one_p5 = pygame.Surface((100, 100))
    one_p5.fill((255, 102, 255))
    one_p6 = pygame.Surface((100, 100))
    one_p6.fill((255, 153, 0))
    screen.blit(one_p1, (150, 400))
    screen.blit(one_p2, (350, 400))
    screen.blit(one_p3, (550, 400))
    screen.blit(one_p4, (150, 600))
    screen.blit(one_p5, (350, 600))
    screen.blit(one_p6, (550, 600))

    pygame.display.flip()

screen.fill((102, 0, 102))

while menuCycle3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuCycle3 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            level = pygame.mouse.get_pos()
            if 150 < level[0] < 350 and 400 < level[1] < 500:
                menuCycle3 = False
            if 450 < level[0] < 650 and 400 < level[1] < 500:
                menuCycle3 = False
                
    lvl = font2.render('Choose level', True, (153, 204, 0))
    screen.blit(lvl, (300, 250))

    lvl1 = pygame.Surface((200, 100))
    lvl1.fill((255, 0, 0))
    lol = font1.render('Level 1', True, (0, 0, 0))
    lvl1.blit(lol, (10, 10))
    screen.blit(lvl1, (150, 400))

    lvl2 = pygame.Surface((200, 100))
    lvl2.fill((255, 0, 0))
    lol2 = font1.render('Level 2', True, (0, 0, 0))
    lvl2.blit(lol2, (10, 10))
    screen.blit(lvl2, (450, 400))


    pygame.display.flip()


while mainCycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainCycle = False

    screen.fill((255, 255, 255))
    pygame.display.flip()
