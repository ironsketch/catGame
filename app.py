import pygame, sys, items, multi, blup
from pygame.locals import*

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()
surf = blup.Window()
player = items.Player(pygame.image.load("src/gifcat_small.png"), 50, 100)
ground = items.Ground(pygame.image.load("src/grass.jpg"), 0, surf.getHeight())
trees = items.Trees(pygame.image.load("src/Tree_Tall.png"), pygame.image.load("src/Tree_Short.png"), surf.getWidth(), surf.getHeight() - ground.img[0][0].get_height())
clouds = items.Clouds(pygame.image.load("src/small_cloud.png"), pygame.image.load("src/large_cloud.png"), surf.getWidth(), pygame.image.load("src/small_cloud.png").get_height())
poops = multi.Poops(pygame.image.load("src/poo.png"), -30, -30, -7)
hairballs = multi.HairBalls(pygame.image.load("src/hairball.png"), -30, -30, -7)
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
    player.move(key, surf.getWidth(), colItems, surf.getHeight(), ground, trees, poops, hairballs)
    timeNow = pygame.time.get_ticks()
    
    if(key[K_e] or key[K_p]):
        if(timeNow - player.poopTimer >= poops.poopWait):
            if player.flipped:
                poops.add(pygame.image.load("src/poo.png"), player.rect[0].midright[0], player.rect[0].y - 20, -7)
            else:
                poops.add(pygame.image.load("src/poo.png"), player.rect[0].midleft[0] - 10, player.rect[0].y - 20, -7)
            player.poopTimer = pygame.time.get_ticks()
    
    if(key[K_r] or key[K_o]):
        if(timeNow - player.hairBallTimer >= hairballs.hairBallWait):
            if player.flipped:
                hairballs.add(pygame.image.load("src/hairball.png"), player.rect[0].midright[0], player.rect[0].y - 20, -7)
            else:
                hairballs.add(pygame.image.load("src/hairball.png"), player.rect[0].midleft[0] - 10, player.rect[0].y - 20, -7)
            player.hairBallTimer = pygame.time.get_ticks()
    
    clouds.move(surf.getWidth())

    # gravity #
    poops.gravity2(colItems)
    hairballs.gravity2(colItems)

    # Update #
    surf.update()
    clouds.update(surf.getWin())
    ground.update(surf.getWin())
    trees.update(surf.getWin())
    poops.update(surf.getWin())
    hairballs.update(surf.getWin())
    player.update(surf.getWin())

    # Quit Option #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
