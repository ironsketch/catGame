import pygame, sys, items, blup
from pygame.locals import*

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()
surf = blup.Window()
player = items.Player(pygame.image.load("src/gifcat_small.png"), 50, 100)
ground = items.Ground(pygame.image.load("src/grass.jpg"), 0, surf.getHeight())
trees = items.Trees(pygame.image.load("src/Tree_Tall.png"), pygame.image.load("src/Tree_Short.png"), surf.getWidth(), surf.getHeight() - ground.img[0][0].get_height())

colItems = []
colItems.append(ground)

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
    player.move(key, surf.getWidth(), colItems, surf.getHeight(), ground, trees)

    # Update #
    surf.update()
    player.update(surf.getWin())
    ground.update(surf.getWin())
    trees.update(surf.getWin())

    # Quit Option #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
