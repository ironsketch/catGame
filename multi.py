import pygame, sys, random, multiSkell
from multiSkell import*
from pygame.locals import*

#####################
#       POOPS       #
#####################
class Poops(MultiSkeleton):
    
    def __init__(self, image, x, y, vel):
        MultiSkeleton.__init__(self, image, x, y, vel)
        self.poopWait = 300

    def move(self, WINH):
        super(Poops, self).move('a')

    def gravity2(self, colItems):
        count = 0
        for poo in self.rect:
            if(not self.collided('s', colItems, poo)):
                self.img[count][2] += self.gravity
                self.rect[count][1] += self.gravity
            count += 1

#####################
#     HAIRBALLS     #
#####################
class HairBalls(MultiSkeleton):
    
    def __init__(self, image, x, y, vel):
        MultiSkeleton.__init__(self, image, x, y, vel)
        self.hairBallWait = 300

    def move(self, WINH):
        super(HairBalls, self).move('a')

    def gravity2(self, colItems):
        count = 0
        for hairball in self.rect:
            if(not self.collided('s', colItems, hairball)):
                self.img[count][2] += self.gravity
                self.rect[count][1] += self.gravity
            count += 1

#class hurtItems:

#class evilDoers:
