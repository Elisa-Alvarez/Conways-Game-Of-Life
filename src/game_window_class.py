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
        self.generation = 0
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
        self.generation = 0
    
    

    # Generation counter
    def gen(self): 
        font = pygame.font.SysFont('arial',25)
        text = font.render(f"Generation:" + str(self.generation), True, (0,0,0))
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
                        self.generation += 1
                        

        self.grid = new_grid
  
    def pre_set_grid(self):
        set_grid = copy.copy(self.grid)
        for yindex, row in enumerate(self.grid):
            for xindex, cell in enumerate(row):
                #object 1 IDK how to loop without breaking! *crying on the inside*
                 set_grid[5][0].alive = True
                 set_grid[5][1].alive = True
                 set_grid[5][2].alive = True
                 set_grid[5][3].alive = True
                 set_grid[5][4].alive = True  
                 set_grid[5][5].alive = True  
                 set_grid[4][0].alive = True
                 set_grid[4][5].alive = True
                 set_grid[3][0].alive = True
                 set_grid[3][1].alive = True
                 set_grid[3][2].alive = True
                 set_grid[3][3].alive = True
                 set_grid[3][4].alive = True
                 set_grid[3][5].alive = True 
                 set_grid[2][5].alive = True
                 set_grid[2][6].alive = True
                
                 set_grid[7][0].alive = True
                 set_grid[7][1].alive = True
                 set_grid[8][2].alive = True
                 set_grid[7][3].alive = True
                 set_grid[8][4].alive = True  
                 set_grid[7][5].alive = True  
                 set_grid[8][0].alive = True
                 set_grid[8][5].alive = True
                 set_grid[11][0].alive = True
                 set_grid[11][1].alive = True
                 set_grid[11][2].alive = True
                 set_grid[11][3].alive = True
                 set_grid[11][4].alive = True
                 set_grid[11][5].alive = True 
                 set_grid[10][5].alive = True
                 set_grid[10][6].alive = True

                 set_grid[20][0].alive = True
                 set_grid[20][1].alive = True
                 set_grid[20][2].alive = True
                 set_grid[20][3].alive = True
                 set_grid[20][5].alive = True  
                 set_grid[25][5].alive = True  
                 set_grid[25][0].alive = True
                 set_grid[0][5].alive = True
                 set_grid[18][0].alive = True
                 set_grid[20][10].alive = True
                 set_grid[9][14].alive = True
                 set_grid[9][12].alive = True
                 set_grid[13][10].alive = True
                 set_grid[13][21].alive = True 
                 set_grid[14][10].alive = True
                 set_grid[14][11].alive = True
                
                
        self.grid = set_grid

    def random_grid(self):
                                # Need to increment every time a cell is changed
        random_grids = copy.copy(self.grid)
        for yindex, row in enumerate(self.grid):
            for xindex, cell in enumerate(row):
                if cell.alive is not True:
                    yindex = random.randint(0,29)
                    xindex = random.randint(0,29)
                    random_grids[yindex][xindex].alive = True
        self.grid = random_grids
