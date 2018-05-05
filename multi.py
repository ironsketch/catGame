import pygame, sys, random, multiSkell
from multiSkell import*
from pygame.locals import*

#####################
#       POOPS       #
#####################
class Poops(MultiSkeleton):
    
    def __init__(self, image, x, y, vel, flip):
        MultiSkeleton.__init__(self, image, x, y, vel, flip)
        self.poopWait = 300

    def move(self, WINH):
        super(Poops, self).move('a')

#####################
#     HAIRBALLS     #
#####################
class HairBalls(MultiSkeleton):
    
    def __init__(self, image, x, y, vel, flip):
        MultiSkeleton.__init__(self, image, x, y, vel, flip)
        self.hairBallWait = 300

    def move(self, WINH):
        super(HairBalls, self).move('a')

#class hurtItems:

#class evilDoers:
