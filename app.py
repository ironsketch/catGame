import pygame, sys, items
from pygame.locals import*

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

player = items.Player(pygame.image.load("src/gifcat_small.png"), 50, 100)

## ======== ## ======== ##
    ### MAIN LOOP ###
## ======== ## ======== ##
while True:
    pygame.event.pump()

    # Get the key pressed #
    key = pygame.key.get_pressed()
    if(key[K_ESCAPE]):
        pygame.quit()
        sys.exit()
    player.move(key)

    # Quit Option #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    fpsClock.tick(FPS)
