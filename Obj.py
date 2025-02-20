import pygame
import random

class Obj():
    def __init__(self,pos,radius,color,charge):
        self.pos = pygame.Vector2(pos)
        self.color=color
        self.radius = radius
        self.charge = charge


    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
