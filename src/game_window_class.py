import pygame
import copy
import random
from cell_class import *
vec = pygame.math.Vector2

class Game_window:
    def __init__(self, screen, x,y,):
        self.screen = screen
        self.pos = vec(x,y)
        self.width, self.height = 600, 600
        self.image = pygame.Surface((self.width,self.height))
        self.rect = self.image.get_rect()
        self.rows = 30
        self.cols = 30
        self.gen = gen
        self.grid = [[Cell(self.image, x , y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in  row:
                cell.get_neighbors(self.grid)
        
    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
              cell.update()
              
    def draw(self):
       self.image.fill((102,102,102))
       for row in self.grid:
            for cell in row:
                cell.draw()
       self.screen.blit(self.image, (self.pos.x,self.pos.y))
    
    def clear(self):
        self.grid = [[Cell(self.image, x , y) for x in range(self.cols)] for y in range(self.rows)]
    
    

    # Generation counter
    def gen(self):
        for row in self.grid:
            for cell in row:
                if cell.alive == True:
                    self.gen += 1
                    
        font = pygame.font.SysFont('arial',25)
        text = font.render("Generation:" + str(self.gen), True )
        self.screen.blit(text,(0,0))
    

    def scan_self(self):

                        # Need to increment every time a cell is changed
        new_grid = copy.copy(self.grid)
        for row in self.grid:
            for cell in row:
                cell.live_neighbors()
      
        for yindex, row in enumerate(self.grid):
            for xindex, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbor == 2 or cell.alive_neighbor == 3:
                        new_grid[yindex][xindex].alive = True
                    if cell.alive_neighbor < 2 :
                        new_grid[yindex][xindex].alive = False
                    if cell.alive_neighbor > 3:
                        new_grid[yindex][xindex].alive = False
                else:
                    if cell.alive_neighbor == 3:
                        new_grid[yindex][xindex].alive = True
                        

        self.grid = new_grid
    
    # def random_grid(self):
    #                             # Need to increment every time a cell is changed
    #     random_grids = copy.copy(self.grid)
    #     for row in self.grid:
    #         for cell in row:
    #            if cell.live_neighbors() == 0 or cell.alive == False:
    #                cel.l = random(True,False)
    #     # for r in range(self.num_rows):
    #     #     for c in range(self.num_cols):
    #     #         if value is None:
    #     #             cell_value = random.randint(0, 1)
    #     #         else:
    #     #             cell_value = value
    #     #         self.grids[grid][r][c] = cell_value
    #     self.grid = random_grids
