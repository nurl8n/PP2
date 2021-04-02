import pygame

# Initializing pygame module
pygame.init()


# will be referred Surface Object
screen = pygame.display.set_mode((500, 500))            # screen size of game
pygame.display.set_caption('My First Game')             # name of the window

running = True

# Main program loop
while running:                     # to keep the screen from closing
    # Event Loop
    for event in pygame.event.get():                # for all events
        if event.type == pygame.QUIT:               # each event has own type
            running = False                 # will be closed, because we are out of loop

    # Game logic





    # Drawing object




    # Apply changes on the window (Change the frame)
    pygame.display.flip()
    # it will not be closed by clicking on X

# Exitting from the pygame program
pygame.quit()









