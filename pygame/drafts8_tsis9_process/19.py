import pygame
import random
import time
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AppleGrub')
font1 = pygame.font.SysFont('Times New Roman', 60)
font2 = pygame.font.SysFont('dejavuserif', 30)
font3 = pygame.font.SysFont('arial', 20)
font4 = pygame.font.SysFont('Arial', 30)
font = pygame.font.SysFont('Arial', 30)
mainCycle, mainCycle2, mainCycleLevelTwo, twoPlayerCycle = False, False, False, False
menuCycle, menuCycle2, menuCycle3, menuCycleLevel1, menuCycleLevel2 = True, False, False, False, False
screen.fill((102, 0, 102))
FPS, FPS2 = 30, 60
incSpeed = 5
clock = pygame.time.Clock()

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
                twoPlayerCycle = True
            if 160 < prev[0] < 340 and 700 < prev[1] < 750:
                menuCycle = False
                menuCycleLevel1 = True
            if 460 < prev[0] < 640 and 700 < prev[1] < 750:
                menuCycle = False
                menuCycleLevel2 = True

    greeting = font1.render('Hello to AppleGrub Game', True, (255, 255, 0))
    n_players = font2.render('Choose number of players', True, (153, 204, 0))
    screen.blit(greeting, (95, 150))
    screen.blit(n_players, (200, 320))

    lvlOne = pygame.Surface((180, 50))
    lvlOne.fill((255, 0, 0))
    bir = font3.render('Scores in Level 1', True, (0, 0, 0))
    lvlOne.blit(bir, (15, 11))
    screen.blit(lvlOne, (160, 700))

    lvlTwo = pygame.Surface((180, 50))
    lvlTwo.fill((255, 0, 0))
    eki = font3.render('Scores in Level 2', True, (0, 0, 0))
    lvlTwo.blit(eki, (15, 11))
    screen.blit(lvlTwo, (460, 700))

    one_p = pygame.image.load('one_p.png')
    one_p_rect = one_p.get_rect(bottomright=(330, 600))
    screen.blit(one_p, one_p_rect)
    two_p = pygame.image.load('two_p.png')
    two_p_rect = two_p.get_rect(bottomright=(600, 600))
    screen.blit(two_p, two_p_rect)

    bandersnatch = font3.render('Брандашмыг', True, (0, 0, 255))
    screen.blit(bandersnatch, (345, 870))
    pygame.display.flip()

screen.fill((255, 204, 153))
record1 = ''
with open('record_lvl1.txt', 'r') as reader:
    xax = (reader.read())
    record1 += xax
s = record1.split('\n')
while menuCycleLevel1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuCycleLevel1 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            if 50 < prev[0] < 130 and 50 < prev[1] < 100:
                menuCycleLevel1 = False
                menuCycle = True
    for i in range(len(s)):
        showRecordOne = font2.render(s[i], True, (0, 0, 0))
        screen.blit(showRecordOne, (380, i*60 + 200))
    button1 = pygame.Surface((80, 50))
    button1.fill((0, 255, 0))
    but = font3.render('Back', True, (0, 0, 0))
    button1.blit(but, (15, 11))
    screen.blit(button1, (50, 50))
    pygame.display.flip()

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
                twoPlayerCycle = True
            if 160 < prev[0] < 340 and 700 < prev[1] < 750:
                menuCycle = False
                menuCycleLevel1 = True
            if 460 < prev[0] < 640 and 700 < prev[1] < 750:
                menuCycle = False
                menuCycleLevel2 = True

    greeting = font1.render('Hello to AppleGrub Game', True, (255, 255, 0))
    n_players = font2.render('Choose number of players', True, (153, 204, 0))
    screen.blit(greeting, (95, 150))
    screen.blit(n_players, (200, 320))

    lvlOne = pygame.Surface((180, 50))
    lvlOne.fill((255, 0, 0))
    bir = font3.render('Scores in Level 1', True, (0, 0, 0))
    lvlOne.blit(bir, (15, 11))
    screen.blit(lvlOne, (160, 700))

    lvlTwo = pygame.Surface((180, 50))
    lvlTwo.fill((255, 0, 0))
    eki = font3.render('Scores in Level 2', True, (0, 0, 0))
    lvlTwo.blit(eki, (15, 11))
    screen.blit(lvlTwo, (460, 700))

    one_p = pygame.image.load('one_p.png')
    one_p_rect = one_p.get_rect(bottomright=(330, 600))
    screen.blit(one_p, one_p_rect)
    two_p = pygame.image.load('two_p.png')
    two_p_rect = two_p.get_rect(bottomright=(600, 600))
    screen.blit(two_p, two_p_rect)

    bandersnatch = font3.render('Брандашмыг', True, (0, 0, 255))
    screen.blit(bandersnatch, (345, 870))
    pygame.display.flip()

screen.fill((255, 204, 153))
record2 = ''
with open('record_lvl2.txt', 'r') as reader:
    xax2 = (reader.read())
    record2 += xax2
s2 = record2.split('\n')
while menuCycleLevel2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuCycleLevel2 = False
    for j in range(len(s2)):
        showRecordTwo = font2.render(s2[j], True, (0, 0, 0))
        screen.blit(showRecordTwo, (380, j*60 + 200))
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
                mainCycle = True
            if 450 < level[0] < 650 and 400 < level[1] < 500:
                menuCycle3 = False
                mainCycleLevelTwo = True

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

class Snake:
    # my constructor for snake
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx, self.dy = 5, 0
        self.elements = [[100, 300], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)
    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x = random.randint(100, SCREEN_WIDTH - 100)
        self.y = random.randint(200, SCREEN_HEIGHT - 100)
        self.image = pygame.image.load('apple.png')
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def show_score(x, y, score):
    show = font4.render('Score: ' + str(score), True, (0, 153, 0))
    screen.blit(show, (x, y))

def collision():
    if (food.x in range(snake.elements[0][0] - 26, snake.elements[0][0]) and food.y in range(snake.elements[0][1] - 26, snake.elements[0][1])):
        snake.is_add = True
        food.x = random.randint(100, SCREEN_WIDTH - 100)
        food.y = random.randint(200, SCREEN_HEIGHT - 100)
        a = random.randint(32, 732)
        b = random.randint(182, 768)
        levelTwo.x, levelTwo.y = a, b


def is_in_walls_first():
    return snake.elements[0][0] > SCREEN_WIDTH - 42 or snake.elements[0][0] < 42

def random_walls():
    if (snake.elements[0][0] in range(levelTwo.x, levelTwo.x + 25) and snake.elements[0][1] in range(levelTwo.y, levelTwo.y + 105)):
        return True
    if (snake.elements[0][0] in range(levelTwo.x - 10, levelTwo.x) and snake.elements[0][1] in range(levelTwo.y - 10, levelTwo.y)):
        return True

def is_in_walls_second():
    return snake.elements[0][1] > SCREEN_HEIGHT - 42 or snake.elements[0][1] < 142

def show_walls():
    for i in range(0, SCREEN_WIDTH, 16):
        screen.blit(wall_image, (i, 100))
        screen.blit(wall_image, (i, SCREEN_HEIGHT - 32))
        screen.blit(wall_image, (0, i + 100))
        screen.blit(wall_image, (SCREEN_WIDTH - 32, i + 100))

def game_over():
    screen.fill((255, 0, 0))
    txt = font.render('GAME OVER', True, (255, 255, 255))
    my_score = font.render('Total score: ' + str(snake.score), True, (255, 255, 255))
    screen.blit(txt, (310, 400))
    screen.blit(my_score, (20, 20))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

class LevelTwoWalls:
    def __init__(self):
        a = random.randint(32, 732)
        b = random.randint(182, 768)
        self.x, self.y = a, b
        self.image = pygame.image.load('wall.png')

    def draw(self):
        screen.blit(self.image, (self.x, self.y + 32))
        screen.blit(self.image, (self.x, self.y + 64))
        screen.blit(self.image, (self.x, self.y + 96))

snake = Snake()
food = Food()
levelTwo = LevelTwoWalls()
wall_image = pygame.image.load('wall.png')

while mainCycle:
    mil = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainCycle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 5
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -5
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dy = -5
                snake.dx = 0
            if event.key == pygame.K_DOWN:
                snake.dy = 5
                snake.dx = 0

    head_x = snake.elements[0][0]
    head_y = snake.elements[0][1]
    for i in range(len(snake.elements)):
        if i > 0:
            body_x = snake.elements[i][0]
            body_y = snake.elements[i][1]
            if (body_x == head_x and body_y == head_y):
                with open('record_lvl1.txt', 'a', encoding='utf-8') as file:
                    file.write(f'{snake.score}' + '\n')
                game_over()

    if is_in_walls_first():
        with open('record_lvl1.txt', 'a', encoding='utf-8') as file:
            file.write(f'{snake.score}' + '\n')
        game_over()
        mainCycle = False
    if is_in_walls_second():
        with open('record_lvl1.txt', 'a', encoding='utf-8') as file:
            file.write(f'{snake.score}' + '\n')
        game_over()
        mainCycle = False
    collision()
    screen.fill((255, 255, 255))
    snake.move()
    snake.draw()
    food.draw()
    show_score(40, 35, snake.score)
    show_walls()
    pygame.display.flip()

while mainCycleLevelTwo:
    mil = clock.tick(FPS2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainCycleLevelTwo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = incSpeed
                snake.dy = 0
                incSpeed += 1
            if event.key == pygame.K_LEFT:
                snake.dx = -incSpeed
                snake.dy = 0
                incSpeed += 1
            if event.key == pygame.K_UP:
                snake.dy = -incSpeed
                snake.dx = 0
                incSpeed += 1
            if event.key == pygame.K_DOWN:
                snake.dy = incSpeed
                snake.dx = 0
                incSpeed += 1
    head_x = snake.elements[0][0]
    head_y = snake.elements[0][1]
    for i in range(len(snake.elements)):
        if i > 0:
            body_x = snake.elements[i][0]
            body_y = snake.elements[i][1]
            if (body_x == head_x and body_y == head_y):
                with open('record_lvl2.txt', 'a', encoding='utf-8') as file:
                    file.write(f'{snake.score}' + '\n')
                game_over()
    if is_in_walls_first():
        with open('record_lvl2.txt', 'a', encoding='utf-8') as file:
            file.write(f'{snake.score}' + '\n')
        game_over()
        mainCycleLevelTwo = False
    if is_in_walls_second():
        with open('record_lvl2.txt', 'a', encoding='utf-8') as file:
            file.write(f'{snake.score}' + '\n')
        game_over()
        mainCycleLevelTwo = False
    if random_walls():
        with open('record_lvl2.txt', 'a', encoding='utf-8') as file:
            file.write(f'{snake.score}' + '\n')
        game_over()
        mainCycleLevelTwo = False

    collision()
    screen.fill((255, 255, 255))
    snake.move()
    snake.draw()
    food.draw()
    show_score(40, 35, snake.score)
    show_walls()
    levelTwo.draw()
    pygame.display.flip()

class Snake2:
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx, self.dy = 5, 0
        self.elements = [[200, 300], [220, 100], [240, 100]]
        self.score = 0
        self.is_add = False
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (0, 0, 255), element, self.radius)
    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

snake2 = Snake2()

def collision2():
    if (food.x in range(snake2.elements[0][0] - 26, snake2.elements[0][0]) and food.y in range(snake2.elements[0][1] - 26, snake2.elements[0][1])):
        snake2.is_add = True
        food.x = random.randint(100, SCREEN_WIDTH - 100)
        food.y = random.randint(200, SCREEN_HEIGHT - 100)

def show_score2(x, y, score2):
    show = font4.render('Score: ' + str(score2), True, (0, 153, 0))
    screen.blit(show, (x, y))

def is_in_walls_first2():
    return snake2.elements[0][0] > SCREEN_WIDTH - 42 or snake2.elements[0][0] < 42

def is_in_walls_second2():
    return snake2.elements[0][1] > SCREEN_HEIGHT - 42 or snake2.elements[0][1] < 142

def game_over2():
    screen.fill((255, 0, 0))
    txt = font.render('GAME OVER', True, (255, 255, 255))
    my_score = font.render('Player 1: ' + str(snake.score), True, (255, 255, 255))
    screen.blit(txt, (310, 400))
    screen.blit(my_score, (20, 20))
    my_score2 = font.render('Player 2: ' + str(snake2.score), True, (255, 255, 255))
    screen.blit(my_score2, (630, 20))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

def collision3():
    if (snake2.elements[0][0] in range(snake.elements[0][0] - 20, snake.elements[0][0]) and snake2.elements[0][0] in range(snake.elements[0][1] - 20, snake.elements[0][1])):
        return True
    if (snake.elements[0][0] in range(snake2.elements[0][0] - 20, snake2.elements[0][0]) and snake.elements[0][0] in range(snake2.elements[0][1] - 20, snake2.elements[0][1])):
        return True

while twoPlayerCycle:
    mil = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            twoPlayerCycle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 5
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -5
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dy = -5
                snake.dx = 0
            if event.key == pygame.K_DOWN:
                snake.dy = 5
                snake.dx = 0
            if event.key == pygame.K_a:
                snake2.dx = -5
                snake2.dy = 0
            if event.key == pygame.K_d:
                snake2.dx = 5
                snake2.dy = 0
            if event.key == pygame.K_w:
                snake2.dy = -5
                snake2.dx = 0
            if event.key == pygame.K_s:
                snake2.dy = 5
                snake2.dx = 0
    head_x = snake.elements[0][0]
    head_y = snake.elements[0][1]
    for i in range(len(snake.elements)):
        if i > 0:
            body_x = snake.elements[i][0]
            body_y = snake.elements[i][1]
            if (body_x == head_x and body_y == head_y):
                game_over2()

    head2_x = snake2.elements[0][0]
    head2_y = snake2.elements[0][1]
    for i in range(len(snake2.elements)):
        if i > 0:
            body2_x = snake2.elements[i][0]
            body2_y = snake2.elements[i][1]
            if (body2_x == head2_x and body2_y == head2_y):
                game_over2()

    if is_in_walls_first():
        game_over2()
        twoPlayerCycle = False
    if is_in_walls_second():
        game_over2()
        twoPlayerCycle = False
    if is_in_walls_first2():
        game_over2()
        twoPlayerCycle = False
    if is_in_walls_second2():
        game_over2()
        twoPlayerCycle = False

    collision()
    collision2()
    if collision3():
        game_over2()
    screen.fill((255, 255, 255))
    snake.move()
    snake.draw()
    snake2.move()
    snake2.draw()
    food.draw()
    show_score(40, 35, snake.score)
    show_score2(600, 35, snake2.score)
    show_walls()
    pygame.display.flip()

