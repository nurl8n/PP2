import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball:
    def __init__(self, *args, **kwargs):
        # properties of ball
        self.radius = 10
        # position
        self.x = 150
        self.y = 100
        self.dx = random.randint(1, 5)      # random between 1 and 5
        self.dy = random.randint(1, 5)
        self.color = RED

    # actions that can be done with the ball
    def move(self, screen):
        self.x += self.dx
        self.y += self.dy

        # to not disappear from the screen
        if self.x > 600 or self.x < 0:
            self.dx *= -1
        if self.y > 600 or self.y < 0:
            self.dy *= -1


    def draw(self, screen):
        # depending on the selected color
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


# empty list
# Ball() means one object from the class Ball
# we are getting only one object
balls = [
    Ball()
]


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

    for ball in balls:
        # moving the ball in some direction
        ball.move(screen)

    screen.fill(WHITE)

    for ball in balls:
        # draw() means we want to draw each ball on the screen
        # it should be done before the refreshing the screen
        # calling the function
        ball.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
