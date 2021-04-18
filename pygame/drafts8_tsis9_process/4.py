import pygame
import random
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AppleGrub')
font1 = pygame.font.SysFont('Times New Roman', 60)
font2 = pygame.font.SysFont('dejavuserif', 30)
font3 = pygame.font.SysFont('arial', 20)
font4 = pygame.font.SysFont('Arial', 30)
mainCycle, mainCycle2 = False, False
menuCycle, menuCycle2, menuCycle3 = True, False, False
screen.fill((102, 0, 102))
FPS = 30
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
                mainCycle = True
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

class Snake:
    # my constructor for snake
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx, self.dy = 5, 0
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False
    # drawing the snake
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, colorRgb, element, self.radius)
    # adding parts of snake and increasing the score
    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        # after adding it becomes False again
        self.is_add = False

    # for movement
    def move(self):
        if self.is_add:
            self.add_snake()
        # getting the position of subsequent element
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        # adding a step for movement
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


# radius of snake is 10
# radius of food is 16
# radius of wall is 16

class Food:
    # my constructor for food
    def __init__(self):
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(150, SCREEN_HEIGHT - 50)
        self.image = pygame.image.load('apple.png')
    # drawing an apple
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# showing score
def show_score(x, y, score):
    show = font4.render('Score: ' + str(score), True, (0, 153, 0))
    screen.blit(show, (x, y))
# detecting the collision of snake with apple
def collision():
    if (food.x in range(snake.elements[0][0] - 26, snake.elements[0][0]) and food.y in range(snake.elements[0][1] - 26, snake.elements[0][1])):
        # adding one to score and increasing the size of snake for one
        snake.is_add = True
        food.x = random.randint(50, SCREEN_WIDTH - 50)
        food.y = random.randint(150, SCREEN_HEIGHT - 50)
# checking the collision of snake with walls
def is_in_walls():
    LeftRight =  snake.elements[0][0] > SCREEN_WIDTH - 32 or snake.elements[0][0] - 32
    TopBottom = snake.elements[0][1] > SCREEN_HEIGHT - 50 or snake.elements[0][1] - 150
    BothOfThem = LeftRight or TopBottom
    return BothOfThem
# showing the walls
def show_walls():
    for i in range(0, SCREEN_WIDTH, 16):
        screen.blit(wall_image, (i, 100))
        screen.blit(wall_image, (i, SCREEN_HEIGHT - 32))
        screen.blit(wall_image, (1, 100))
        screen.blit(wall_image, (SCREEN_WIDTH - 32, i))

# initializing our classes
snake = Snake()
food = Food()
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
    collision()
    screen.fill((255, 255, 255))
    # moving our snake
    snake.move()
    snake.draw()
    food.draw()
    show_score(40, 35, snake.score)
    show_walls()
    # updating the screen
    pygame.display.flip()

