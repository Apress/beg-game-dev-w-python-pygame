background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# The X coordinate of our sprite
x = 0.

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(sprite, (x, 100))
    x+= 10.
    
    # If the image goes off the end of the screen, move it back
    if x > 640.:
        x = 0.    
    
    pygame.display.update()
