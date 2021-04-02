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
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background-color
    screen.fill(WHITE)

    # adding different type of items
    # counting starts from the top left in x and y, like on the fourth quarter of the graph
    # arguments are provided like a tuple
    # surface, color, starting position, ending position, width
    pygame.draw.line(screen, (0, 255, 0), (10, 10), (200, 10), 5)

    # drawing multiple-lines
    for step in range(20, 50, 10):
        pygame.draw.line(screen, (0, 0, 255), (10, step), (200, step), 4)

    # colored circle
    pygame.draw.circle(screen, (255, 0, 0), (250, 50), 40)

    # not colored circle
    pygame.draw.circle(screen, (255, 0, 0), (350, 50), 40, 3)

    # rectangle
    pygame.draw.rect(screen, (0, 255, 0), (20, 60, 100, 50))

    # rectangle empty one
    pygame.draw.rect(screen, (0, 255, 0), (20, 120, 100, 50), 3)

    # ellipse
    #ellipse is drawn inside a rectangle
    pygame.draw.ellipse(screen, (100, 100, 100), (50, 200, 100, 100), 3)
    pygame.draw.rect(screen, (30, 60, 90), (50, 200, 100, 100), 3)

    # polygon is a line, which connects points
    pygame.draw.polygon(screen, (255, 30, 155), ((450, 170), (400, 250), (500, 250)))
    pygame.draw.polygon(screen, (255, 55, 180), ((300, 170), (200, 250), (350, 250)), 3)

    # arc is one part of a circle
    pygame.draw.arc(screen, (230, 15, 60), (20, 330, 100, 100), 0, 90*PI/180, 5)
    pygame.draw.arc(screen, (80, 255, 30), (20, 330, 100, 100), 90*PI/180, PI, 5)
    pygame.draw.arc(screen, (30, 55, 180), (20, 330, 100, 100), PI, 270*PI/180, 5)
    pygame.draw.arc(screen, (33, 233, 133), (20, 330, 100, 100), 270*PI/180, 0, 5)


    pygame.display.flip()

    # clock class, it can be used setting frames per second
    # FPS
    clock.tick(FPS)

pygame.quit()









