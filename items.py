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
    
    def move(self, key, WINW, colItems, WINH):
        if(key[K_d] and not self.collided('d', colItems, self.rect[0], WINW, WINH)):
            if self.flipped:
                self.img[0][0] = pygame.transform.flip(self.img[0][0], True, False)
                self.flipped = False
            if(self.img[0][1] <= WINW * .6):
                super(Player, self).move('d')
        if(key[K_a] and not self.collided('a', colItems, self.rect[0], WINW, WINH)):
            if not self.flipped:
                self.img[0][0] = pygame.transform.flip(self.img[0][0], True, False)
                self.flipped = True
            super(Player, self).move('a')
        if(not self.collided('s', colItems, self.rect[0], WINW, WINH)):
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

#class hurtItems:

#class Clouds:
 
#class evilDoers:
