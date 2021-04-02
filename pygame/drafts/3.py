import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My First Game')

WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60
PI = 3.14

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # adding a text
    font = pygame.font.Font(None, 55)
    text = font.render("Nurlan", True, (255, 30, 70))
    screen.blit(text, (192, 192))

    
    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()









