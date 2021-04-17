import pygame
import random
import time
pygame.init()
# Capslock, constants are wrote by uppercase
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont('Arial', 30)

go = True

# we need classes when we need lots of objects (snakes, food and so on)
# it have some own methods
FPS = 30
clock = pygame.time.Clock()


class Snake:
    # init is constructor, we send self, so we can do not send any message to __init__ function
    def __init__(self):
        # when we write snake1 = Snake() we do __init__ function here
        self.size = 3
        self.radius = 10
        # for movement
        self.dx, self.dy = 5, 0
        # snake is a list of circles, so elements is for these circles
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False

    # for drawing it
    # all function in class is related to this class, because of that we need to send self by default
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False


    # for movement
    def move(self):
        if self.is_add:
            self.add_snake()
        # previous element takes the position of first
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        # adding a step for the head
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.image = pygame.image.load('apple.png')
        # self.position = [random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)]

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def show_score(x, y, score):
    show = font.render('Score: ' + str(score), True, (255, 0, 0))
    screen.blit(show, (x, y))

def collision():
    if(food.x in range(snake.elements[0][0]-20, snake.elements[0][0]) and food.y in range(snake.elements[0][1] - 20, snake.elements[0][1])):
        snake.is_add = True
        food.x = random.randint(50, WIDTH - 50)
        food.y = random.randint(50, HEIGHT - 50)

# checking the collision of snake with walls
def is_in_walls():
    return snake.elements[0][0] > WIDTH - 32 or snake.elements[0][0] < 32

def game_over():
    screen.fill((255, 0, 0))
    txt = font.render('GAME OVER', True, (255, 255, 255))
    my_score = font.render('Total score: ' + str(snake.score), True, (255, 255, 255))
    screen.blit(txt, (200, 200))
    screen.blit(my_score, (20, 20))
    pygame.display.flip()
    # to show only 3 seconds
    time.sleep(3)
    pygame.quit()



# drawing the walls
def show_walls():
    for i in range(0, WIDTH, 15):
        screen.blit(wall_image, (i, 0))
        screen.blit(wall_image, (i, HEIGHT - 32))
        screen.blit(wall_image, (1, i))
        screen.blit(wall_image, (WIDTH - 32, i))


# creating a object
snake = Snake()
food = Food()

wall_image = pygame.image.load('wall.png')



while go:
    mil = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        # key down means pressing a button
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
    if is_in_walls():
        game_over()
        go = False
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




