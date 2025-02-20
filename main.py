import pygame
import random
import math
from Obj import Obj
from Charge import Charge
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800,600
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("E field Simulation")


k_const = 90000 # test number, in real life this is 9 * 10^9
unit_charge = 2

FPS = 30

charge_list=[]
obj_list = []


def charges_init(d):
    for c in range(0,WIDTH, d):
        for r in range(0,HEIGHT, d):
            new_charge = Charge((c,r),(c,r))
            charge_list.append(new_charge)


# greater value - less density - less lag
charges_init(20)


obj_list.append(Obj(pygame.Vector2(WIDTH/2,HEIGHT/2), 50, "red", 2))
obj_list.append(Obj(pygame.Vector2(0,0), 50, "blue", -2))



def main():
    running=True
    clock = pygame.time.Clock()



    while running:
        delta = clock.tick(FPS)/1000

        mouse_pos = pygame.mouse.get_pos()
        
        

        for event in pygame.event.get():
            if event.type == QUIT:
                running=False
            if event.type == KEYDOWN:
                if event.key == K_w:
                    obj_list[0].pos.y-=10
                elif event.key == K_s:
                    obj_list[0].pos.y+=10
                elif event.key == K_a:
                    obj_list[0].pos.x-=10
                elif event.key == K_d:
                    obj_list[0].pos.x+=10



        obj_list[1].pos = pygame.Vector2(mouse_pos)
        for c in charge_list:

            #e_field = 0
            e_field = pygame.Vector2(0,0)
            
            
            for obj in obj_list:
                obj.draw(win)
                #obj.pos.x = obj.pos[0]
                #obj.pos.y = obj.pos[1]

                if not c.inside(obj):
                    dist = math.sqrt((c.pos.x-obj.pos.x)**2 + (c.pos.y-obj.pos.y)**2)
                    if dist==0:
                        continue
                    angle = math.atan2((obj.pos.y-c.pos.y), (obj.pos.x-c.pos.x)) 
                    # e-field as a vector2
                    e_field += k_const*obj.charge/(dist**2) * pygame.Vector2(math.cos(angle),math.sin(angle))
            c.line = (c.pos.x + e_field.x, c.pos.y+e_field.y)


            c.draw(win)

                
        

        pygame.display.update()
        win.fill("white")

    pygame.quit()

if __name__ =="__main__":
    main()
