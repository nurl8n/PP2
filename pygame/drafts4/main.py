import pygame
import random

# initialization
pygame.init()

# screen size
screen = pygame.display.set_mode((800, 600))
# downloading an image
backImage = pygame.image.load("bg.png")
# ("./images/bg.png") we can do, ./ means that the same folder, but another path
# name of game
pygame.display.set_caption("GALAXY GAME")

fonts = pygame.font.SysFont('Times new roman', 40)

isDone = False
isBul = False

# downloading other images
bulletImage = pygame.image.load("bullet.png")
enemyImage = pygame.image.load("enemy.png")
playerImage = pygame.image.load("player.png")

score = 0

# starting position
bul_x, bul_y = 220, 460
# changing the position
bul_dx, bul_dy = 0, 0

# starting position
player_x, player_y = 200, 500
last_x = 0

# enemy position, randomly in x,y positions
enemy_x = random.randint(100, 700)
enemy_y = random.randint(20, 50)
# changing the position of enemy
enemy_dx, enemy_dy = 5, 60

def show_player(x, y):
    screen.blit(playerImage, (x, y))

def show_enemy(x, y):
    screen.blit(enemyImage, (x, y))

def show_bullet(x, y):
    screen.blit(bulletImage, (x, y))

# collision of enemy with enemy
def isCollision(enemy_x, enemy_y, bul_x, bul_y):
    if bul_x in range(enemy_x, enemy_x + 70) and bul_x in range(enemy_y, enemy_y + 70):
        return True
    return False

def show_score(x, y):
    sc = fonts.render("Score:" + str(score), True, (50, 100, 150))
    screen.blit(sc, (x, y))



while not isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = True
    # getting the pressed button
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player_x -= 5
        bul_x -= 5
    if pressed[pygame.K_RIGHT]:
        player_x += 5
        bul_x += 5

    if (player_x < 0 or player_x > 735) and (bul_x < 0 or bul_x > 735):
        player_x = player_x % 735
        bul_x = bul_x % 735

    enemy_x += enemy_dx

    # when enemy hits the wall, it goes another side
    if enemy_x < 0 or enemy_x > 735:
        enemy_dx = -enemy_dx
        enemy_y += enemy_y
    screen.blit(backImage, (0, 0))

    if bul_x == player_x + 20 and bul_y ==460:
        last_x = player_x
    if pressed[pygame.K_SPACE]:
        isBul = True
    if isBul:
        bul_y -= 5
        bul_x = last_x + 20
    if bul_y == 0:
        isBul = False
        bul_x = player_x + 20
        bul_y = 460

    isCol = isCollision(enemy_x, enemy_y, bul_x, bul_y)
    if isCol and bul_y < 460:
        enemy_x = random.randint(100, 700)
        enemy_y = random.randint(20, 50)
        bul_x = player_x + 20
        bul_y = 460
        score += 1
        isBul = False

    # showing the functions
    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)
    show_bullet(bul_x, bul_y)
    show_score(650, 60)
    pygame.display.update()
