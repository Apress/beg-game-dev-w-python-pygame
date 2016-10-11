GRID_SIZE = (160, 120)
GRID_SQUARE_SIZE = (4, 4)
ant_image_filename = "ant.png"
ITERATIONS = 10

import pygame
from pygame.locals import *

class AntGrid(object):
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height        
        self.clear()
    
    def clear(self):
        
        self.rows = []
        for col_no in xrange(self.height):
            new_row = []
            self.rows.append(new_row)
            for row_no in xrange(self.width):
                new_row.append(False)
    
    def swap(self, x, y):        
        self.rows[y][x] = not self.rows[y][x]
    
    def get(self, x, y):
        return self.rows[y][x]
    
    def render(self, surface, colors, square_size):
        
        w, h = square_size        
        surface.fill(colors[0])
        
        for y, row in enumerate(self.rows):
            rect_y = y * h    
            for x, state in enumerate(row):
                if state:                    
                    surface.fill(colors[1], (x * w, rect_y, w, h))                
                

class Ant(object):
    
    directions = ( (0,-1), (+1,0), (0,+1), (-1,0) )
    
    def __init__(self, grid, x, y, image, direction=1):
        
        self.grid = grid
        self.x = x
        self.y = y
        self.image = image
        self.direction = direction
        
        
    def move(self):
                
        self.grid.swap(self.x, self.y)
                
        self.x = ( self.x + Ant.directions[self.direction][0] ) % self.grid.width
        self.y = ( self.y + Ant.directions[self.direction][1] ) % self.grid.height        
                        
        if self.grid.get(self.x, self.y):
            self.direction = (self.direction-1) % 4
        else:
            self.direction = (self.direction+1) % 4                
        
        
    def render(self, surface, grid_size):
        
        grid_w, grid_h = grid_size
        ant_w, ant_h = self.image.get_size()
        render_x = self.x * grid_w - ant_w / 2
        render_y = self.y * grid_h - ant_h / 2
        surface.blit(self.image, (render_x, render_y))
        
        
def run():
    
    pygame.init()
    w = GRID_SIZE[0] * GRID_SQUARE_SIZE[0]
    h = GRID_SIZE[1] * GRID_SQUARE_SIZE[1]
    screen = pygame.display.set_mode((w, h), 0, 32)
    
    ant_image = pygame.image.load(ant_image_filename).convert_alpha()    
    
    default_font = pygame.font.get_default_font()
    font = pygame.font.SysFont(default_font, 22)    
    
    ants = []
    grid = AntGrid(*GRID_SIZE)
    running = False
    
    total_iterations = 0
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                return
            
            if event.type == MOUSEBUTTONDOWN:
                
                x, y = event.pos
                x /= GRID_SQUARE_SIZE[0]
                y /= GRID_SQUARE_SIZE[1]                
                
                ant = Ant(grid, int(x), int(y), ant_image)
                ants.append(ant)
                    
                    
            if event.type == KEYDOWN:
                
                if event.key == K_SPACE:                
                    running = not running
                    
                if event.key == K_c:
                    grid.clear()
                    total_iterations = 0
                    del ants[:]
                
    
        grid.render(screen, ((255, 255, 255), (0, 128, 0)), GRID_SQUARE_SIZE)
    
        if running:
            for iteration_no in xrange(ITERATIONS):        
                for ant in ants:
                    ant.move()
            total_iterations += ITERATIONS
            
        txt = "%i iterations"%total_iterations
        txt_surface = font.render(txt, True, (0, 0, 0))
        screen.blit(txt_surface, (0, 0))

        for ant in ants:
            ant.render(screen, GRID_SQUARE_SIZE)
            
    
        pygame.display.update()
    
    
if __name__ == "__main__":
    run()
            