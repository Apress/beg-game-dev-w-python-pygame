#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)



while True:
        
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()            
    
    screen.fill((255, 255, 255))
    
    mouse_pos = pygame.mouse.get_pos()
    
    for x in xrange(0,640,20):
        pygame.draw.aaline(screen, (0, 0, 0), (x, 0), mouse_pos)
        pygame.draw.aaline(screen, (0, 0, 0), (x, 479), mouse_pos)
        
    for y in xrange(0,480,20):
        pygame.draw.line(screen, (0, 0, 0), (0, y), mouse_pos)
        pygame.draw.line(screen, (0, 0, 0), (639, y), mouse_pos)
        
    pygame.display.update()
    