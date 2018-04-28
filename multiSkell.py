import pygame, sys, random
from pygame.locals import*

class MultiSkeleton:
    
    def __init__(self, image, x, y, vel):
        self.img = []
        self.rect = []
        self.speed = 5
        self.jumpSpeed = 5
        self.img.append(list((image, x, y, vel)))
        rectangle = pygame.Rect(x, y, image.get_width(), image.get_height() * .8)
        self.rect.append(rectangle)
        self.gravity = 7
        self.velocity = 0

    def add(self, image, x, y, vel):
        self.img.append(list((image, x, y, vel)))
        rectangle = pygame.Rect(x, y, image.get_width(), image.get_height() * .8)
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
                i[2] -= self.jumpSpeed
            for i in self.rect:
                i[1] -= self.jumpSpeed
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

    def gravity(self):
        if(self.velocity > 0):
            self.velocity = 0
        
        for i in self.img:
            i[2] += self.velocity
            i[2] += self.gravity
        for r in self.rect:
            r[1] += self.velocity
            r[1] += self.gravity
        self.velocity += 2

    def update(self, surf):
        for i in self.img:
            surf.blit(i[0], (i[1], i[2])) 
