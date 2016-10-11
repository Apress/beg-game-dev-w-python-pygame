import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

all_colors = pygame.Surface((4096,4096), depth=24)

for r in xrange(256):
    print r+1, "out of 256"
    x = (r&15)*256    
    y = (r>>4)*256
    for g in xrange(256):
        for b in xrange(256):
            all_colors.set_at((x+g, y+b), (r, g, b))

pygame.image.save(all_colors, "allcolors.bmp")