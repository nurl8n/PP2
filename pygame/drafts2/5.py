import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 600))

done = False

# loading music
# it should be outside the while loop
# convert mp3 to ogg format, in that case it would work
# file also should be in one folder with py file
pygame.mixer.music.load('music.ogg')

# for playing infinitely
pygame.mixer.music.play(-1)

# we can also to stop the sound in some cases

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pygame.USEREVENT
# in that way, we can create our own events, for example QUIT is also some kind of event

_image_library = {}
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
        # if event.type == EVENT_OWN:
            # pass

    # print(_image_library)

    screen.fill(WHITE)

    screen.blit(get_image('jet.png'), (100, 100))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
