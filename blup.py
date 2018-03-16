import pygame, sys
from pygame.locals import*

class Window:
    
    def __init__(self):
        self.WINH = 400
        self.WINW = 600
        self.surf = pygame.display.set_mode((self.WINW, self.WINH), 0, 32)
        pygame.display.set_caption("Kitty Poops the Game")
        self.bck = pygame.image.load("src/sky.jpg").convert()

    def getWin(self):
        return self.surf
