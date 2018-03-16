import pygame, sys, random
from pygame.locals import*

class Skeleton:
    img = []
    rect = []
    
    def __init__(self, image, x, y):
        self.img.append(list((image, x, y)))
        rectangle = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.rect.append(rectangle)

    def add(self, image, x, y):
        self.img.append(list((image, x, y)))
        rectangle = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.rect.append(rectangle)

    def move(self, speed):
        for i in self.img:
            i[1] -= speed
        for r in self.rect:
            r[0] -= speed

    def gravity(self, gravity, velocity):
        for i in self.img:
            i[1] += velocity
            i[2] += gravity
        for r in rect:
            r[0] += velocity
            r[1] += gravity

    def update(self, surf):
        for i in self.img:
            surf.blit(i[0], i[1], i[2]) 
