import pygame
import random

charges_r = 2
charges_col = "black"

class Charge():
    def __init__(self,pos,line):
        #self.radius = radius
        #self.color = color
        self.pos = pygame.Vector2(pos)
        self.line = pygame.Vector2(line)


    def update(self,line):
        self.line = line
        

    def inside(self,other):
        """
            detect if it is inside the object.
        """
        dist_squared = (self.pos - other.pos).magnitude_squared()
        if 0 < dist_squared < (charges_r + other.radius)**2:
            return True
        else:
            return False

    def draw(self,screen):
        pygame.draw.circle(screen,charges_col,self.pos,charges_r)
        pygame.draw.line(screen,charges_col,self.pos,self.line,charges_r)
