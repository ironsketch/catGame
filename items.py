import pygame, sys, random, skell
from skell import*
from pygame.locals import*

#####################
#      PLAYER       #
#####################
class Player(Skeleton):

    def __init__(self, image, x, y):
        Skeleton.__init__(self, image, x, y)
        self.flipped = False
        self.poopTimer = pygame.time.get_ticks()
        self.hairBallTimer = pygame.time.get_ticks()

    def move(self, key, WINW, colItems, WINH, ground, trees, poops, hairballs):
        # Forward
        if(key[K_d] and not self.collided('d', colItems, self.rect[0]) and not self.rect[0].x + self.rect[0].width >= WINW):
            if self.flipped:
                self.img[0][0] = pygame.transform.flip(self.img[0][0], True, False)
                self.flipped = False
            if(self.img[0][1] <= WINW * .6):
                super(Player, self).move('d')
            else:
                ground.move(WINW)
                trees.move(WINW)
                poops.move(WINW)
                hairballs.move(WINW)
        # Backward
        if(key[K_a] and not self.collided('a', colItems, self.rect[0]) and not self.rect[0].x <= 0):
            if not self.flipped:
                self.img[0][0] = pygame.transform.flip(self.img[0][0], True, False)
                self.flipped = True
            super(Player, self).move('a')

        # JUMP Yo'
        if(key[K_SPACE] and self.collided('s', colItems, self.rect[0]) and not self.collided('w', colItems, self.rect[0]) and not self.rect[0].y >= WINH):
            self.velocity = -20
            super(Player, self).move('w')

        # Gravity
        if(not self.collided('s', colItems, self.rect[0]) or self.rect[0].y + self.rect[0].height >= WINH):
            super(Player, self).gravity()

    def getRX(self):
        return self.img[0][1] + self.img[0][0].get_width()

#####################
#      GROUND       #
#####################
class Ground(Skeleton):
    
    def __init__(self, image, x, y):
        Skeleton.__init__(self, image, x, y - image.get_height())

    def move(self, WINW):
            if(self.img[len(self.img) - 1][1] + self.img[0][0].get_width() <= WINW):
                self.add(self.img[0][0], self.img[0][0].get_width(), self.img[0][2])
            super(Ground, self).move('a')

#####################
#       TREES       #
#####################
class Trees(Skeleton):
    
    def __init__(self, image, image2, thex, they):
        Skeleton.__init__(self, image, thex, they - image.get_height() * .8)
        self.treeTall = image
        self.treeSmall = image2
        self.x = thex
        self.y = they - image.get_height() * .8

    def move(self, WINW):
        if(not self.img or self.img[len(self.img) - 1][1] + self.img[len(self.img) - 1][0].get_width() < WINW):
            add = random.randint(0, 100)
            if(add == 1):
                self.add(self.treeTall, self.x, self.y)
            if(add == 0):
                self.add(self.treeSmall, self.x, self.y)
        super(Trees, self).move('a')

#####################
#      CLOUDS       #
#####################
class Clouds(Skeleton):

    def __init__(self, image, image2, x, y):
        Skeleton.__init__(self, image, x, y - image.get_height())
        self.cloudSmall = image
        self.cloudLarge = image2
        self.x = x
        self.y = y - image.get_height()
        self.speed = 2

    def move(self, WINW):
        if(not self.img or self.img[len(self.img) - 1][1] + self.img[len(self.img) - 1][0].get_width() < WINW):
            add = random.randint(0, 100)
            heightOfCloud = random.uniform(-.4, .4)
            if(add == 1):
                self.add(self.cloudSmall, self.x, self.y * heightOfCloud)
            if(add == 0):
                self.add(self.cloudLarge, self.x, self.y * heightOfCloud)
        super(Clouds, self).move('a')


#class hurtItems:

#class evilDoers:
