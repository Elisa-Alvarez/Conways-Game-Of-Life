import pygame
import sys
import os
from game_window_class import *
from button_class import *

# Varibles for Game
width,height = 800,800
background = (199,199,199)
FPS = 60

# Game Methods/Actions
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)


def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)

def draw():
     window.fill(background)
     for button in buttons:
        button.draw()

     game_window.draw()

def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < width - 100:
         if pos[1] > 100 and pos[1] < height - 20:
                return True
    return False   

def click_cell(pos):
    grid_pos= [pos[0]-100, pos[1] - 180]
    grid_pos[0]=grid_pos[0]//20
    grid_pos[1]=grid_pos[1]//20
    if  game_window.grid[grid_pos[1]][grid_pos[0]].alive:
         game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive =True

def make_button():
    buttons = []
    #Start Button
    buttons.append(Button(window, width//5 - 100,80, 150, 30, text ='Let us live!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=run_game))
    #Pause
    buttons.append(Button(window, width//2-150,80, 110, 30, text ='Pause life!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=pause_game))
    #Rewind
    buttons.append(Button(window, width//5 +250,80, 170, 30, text ='Go back in time!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=rewind_game))
    #Fast Foward
    buttons.append(Button(window, width//2+220,80, 100, 30, text ='Skip life!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=fast_foward_game))
    
    return buttons
 
    #Button Funtionality 
def run_game(self):
    pass

def pause_game(self):
    pass

def rewind_game(self):
    pass

def fast_foward_game(self):
    pass

# Game intialization
pygame.init()
window = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()
game_window = Game_window(window, 100 , 180)
buttons = make_button()
#Game Loop
while running:
    mouse_pos = pygame.mouse.get_pos()
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()

