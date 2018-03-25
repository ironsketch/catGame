import pygame, sys, random
from pygame.locals import*

class Skeleton:
    
    def __init__(self, image, x, y):
        self.img = []
        self.rect = []
        self.speed = 5
        self.img.append(list((image, x, y)))
        rectangle = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.rect.append(rectangle)
        self.gravity = 5
        self.velocity = 7

    def add(self, image, x, y):
        self.img.append(list((image, x, y)))
        rectangle = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.rect.append(rectangle)

    def changeSpeed(newSpeed):
        self.speed = newSpeed

    def changeVelocity(newSpeed):
        self.velocity = newSpeed
    
    def collided(self, letter, colItems, rec):
        for item in colItems:
            for i in item.rect:

                if(i.collidepoint(rec.midright) and letter == 'd'):
                    return True
                elif(i.collidepoint(rec.midleft) and letter == 'a'):
                    return True
                # Up
                elif(i.collidepoint(rec.midtop) and letter == 'w'):
                    return True
                # Down
                elif(i.collidepoint(rec.midbottom) and letter == 's'):
                    return True
        return False

    def move(self, DIR):
        if(DIR == 'd'):
            for i in self.img:
                i[1] += self.speed
            for i in self.rect:
                i[0] += self.speed
        if(DIR == 'a'):
            for i in self.img:
                i[1] -= self.speed
            for i in self.rect:
                i[0] -= self.speed
        if(DIR == 'w'):
            for i in self.img:
                i[2] -= self.speed
            for i in self.rect:
                i[1] -= self.speed
        if(DIR == 's'):
            for i in self.img:
                i[2] += self.speed
            for i in self.rect:
                i[1] += self.speed

        # Clean up #
        c = 0
        for i in range(0, len(self.img)):
            if(self.img[c][1] + self.img[c][0].get_width() < 0):
                self.img.pop(c)
                self.rect.pop(c)
                c -= 1
            c += 1

    def gravity(self, vel):
        for i in self.img:
            i[1] += self.velocity
            i[2] += self.gravity
        for r in self.rect:
            r[0] += self.velocity
            r[1] += self.gravity
        self.velocity += vel

    def update(self, surf):
        for i in self.img:
            surf.blit(i[0], (i[1], i[2])) 
