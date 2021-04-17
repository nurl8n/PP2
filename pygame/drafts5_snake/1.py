import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()


# we can also create our own surfaces
# a = pygame.Surface((20, 20))

radius = 10
# initial position of our object
# list of points

body = [[100, 100], [0, 0], [0, 0], [0, 0]]

# 1) [100, 100], [0, 0], [0, 0]
# 2) [100, 100], [100, 100], [0, 0]
# 3) [100, 115], [100, 100], [0, 0]
# 4) [100, 130], [100, 115], [100, 100]
# 5) [100, 145], [100, 130], [100, 115]
# 6) [100, 160], [100, 145], [100, 130]
# 7) [115, 160], [100, 160], [100, 145]
# 8) [130, 160], [115, 160], [100, 160]

# changing of position
block = 15
dx, dy = block, 0

food_x, food_y = 0, 0

# in order to be able to eat food
def own_round(value, base=10):
    return base * round(value / 10)

def set_random_position():
    return own_round(random.randint(0, WINDOW_WIDTH)), own_round(random.randint(0, WINDOW_HEIGHT))

food_x, food_y = set_random_position()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = block
                dy = 0
            if event.key == pygame.K_LEFT:
                dx = -block
                dy = 0
            if event.key == pygame.K_UP:
                dx = 0
                dy = -block
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = block
            if event.key == pygame.K_SPACE:
                # adding one more element
                body.append([0, 0])
                # new food
                food_x, food_y = set_random_position()
    for i in range(len(body)-1, 0, -1):
        body[i][0] = body[i-1][0]
        body[i][1] = body[i-1][1]
    body[0][0] += dx
    body[0][1] += dy

    screen.fill(WHITE)

    # Drawing Food
    pygame.draw.circle(screen, BLUE, (food_x, food_y), radius)

    # Drawing Snake
    for i, (x, y) in enumerate(body):
        color = RED if i ==0 else GREEN
        pygame.draw.circle(screen, color, (x, y), radius)



    # screen frames
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
