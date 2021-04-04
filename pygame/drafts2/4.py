import pygame
import os

pygame.init()

# screen itself is surface
screen = pygame.display.set_mode((600, 600))

done = False

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# also instead of rectangle we can create a surface separately as an object
# we can send to it png image

_image_library = {}         # creating empty dictionary
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # only one file there
    print(_image_library)

    # for blit we send 1)surface, 2)position
    # file should be in one folder with py file
    screen.blit(get_image('jet.png'), (100, 100))

    # by .convert.alpha() function we can change the size of picture

    # after the logic we need to fill the screen with some color
    # screen.fill(WHITE)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
