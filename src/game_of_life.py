import pygame
import time
import sys
import os
from game_window_class import *
from cell_class import *
from button_class import *

# Varibles for Game
width,height = 800,800
background = (98,100,95)
FPS = 5


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
            else:
                for button in buttons:
                    button.click()
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'r':
                  game_window.random_grid()
                  game_window.update()
                  game_window.draw()

def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state = state)

def draw():
     window.fill(background)
     for button in buttons:
        button.draw()
     game_window.gen()
     game_window.draw()

def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < width - 100:
         if pos[1] > 180 and pos[1] < height - 20:
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

# Running
def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()
 
def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state = state)
    
    game_window.scan_self()

def running_draw():
     window.fill(background)
     for button in buttons:
        button.draw()
     game_window.gen()
     game_window.draw()

# Pause
def pause_get_events():
    global running
    for event in pygame.event.get():
        if state == 'paused':
            paused = False
        else:
            paused = True
        
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def pause_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state = state)

def pause_draw():
     window.fill(background)
     for button in buttons:
        button.draw()
     game_window.gen()
     game_window.draw()

                                             #Foward
def forward_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()
 
def forward_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state = state)
    
    game_window.scan_self()
def forward_draw():
     window.fill(background)
     for button in buttons:
        button.draw()
     if state == "forward":
        game_window.gen()
        game_window.draw()

#Random Color



#Pre Selected Grid
def selected_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()
 
def selected_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state = state)
    
    game_window.scan_self()

def selected_draw():
     window.fill(background)
     for button in buttons:
        button.draw()
     if state == "selected":
        game_window.gen()
        game_window.draw()

def make_button():
    buttons = []
    #Start Button
    buttons.append(Button(window, width//2 - 100,80, 150, 30, text ='Let us live!',color=(0, 212, 127),hover_color=(72, 250, 179), bold_text=True,function= run_game, state= "setting"))
    #Preset Grid Setting
    buttons.append(Button(window, width//2 - 100,20, 150, 30, text ='Chosen Life!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=pre_set_game, state = "setting"))
 
  # ---------------- RUNNING
    #Pause Running
    buttons.append(Button(window, width//2-220,80, 115, 30, text ='Pause life!',color=(18, 215, 255),hover_color=(163, 255, 250), bold_text=True,function=pause_game, state="running"))
    
    #Fast Forward running
    buttons.append(Button(window, width//5 + 330,80, 150, 30, text ='Speed up life!',color=(233, 245, 15),hover_color=(255, 251, 0), bold_text=True,function=fast_foward_game,state = "running"))
  
    #Reset Grid Running
    buttons.append(Button(window, width//2 - 85,80, 150, 30, text ='Restart life!',color=(197, 32, 17,),hover_color=(245, 39, 20), bold_text=True,function=reset_game, state = "running"))
    
    #Random Colors Running
    buttons.append(Button(window, width//5 - 100,40, 160, 30, text ='Random Colors!',color=(219, 168, 86),hover_color=(245, 197, 120), bold_text=True,function=random_color, state = "running"))
  
  # -------------- Pause   
 
   #Fast Forward Paused
    buttons.append(Button(window, width//5 + 330,80, 150, 30, text ='Speed up life!',color=(233, 245, 15),hover_color=(255, 251, 0), bold_text=True,function=fast_foward_game,state = "pause"))
 
   #Resume Paused
    buttons.append(Button(window, width//2- 290,80, 150, 30, text ='Resume life!',color=(72, 169, 20),hover_color=(80, 197, 17), bold_text=True,function=run_game, state = "pause"))
  
   #Reset Grid Paused
    buttons.append(Button(window, width//2 -100,80, 150, 30, text ='Restart life!',color=(197, 32, 17,),hover_color=(245, 39, 20), bold_text=True,function=reset_game, state = "pause"))  
   
  # -------------- Foward
    #Reset Grid Forward
    buttons.append(Button(window, width//2 + 120,80, 150, 30, text ='Restart life!',color=(197, 32, 17,),hover_color=(245, 39, 20), bold_text=True,function=reset_game, state = "forward"))  
  
    #Resume Forward
    buttons.append(Button(window, width//2-80,80, 150, 30, text ='Resume life!',color=(72, 169, 20),hover_color=(80, 197, 17), bold_text=True,function=run_game, state = "forward"))
    
    #Random Colors Forward
    buttons.append(Button(window, width//5 - 100,40, 160, 30, text ='Random Colors!',color=(219, 168, 86),hover_color=(245, 197, 120), bold_text=True,function=random_color, state = "forward"))
  
   #Paused Forward
    buttons.append(Button(window, width//2-250,80, 115, 30, text ='Pause life!',color=(14, 207, 197),hover_color=(163, 255, 250), bold_text=True,function=pause_game, state="forward"))
 
  # ------------ Selected

    #Reset Grid Selected
    buttons.append(Button(window, width//2 + 120,80, 150, 30, text ='Restart life!',color=(197, 32, 17,),hover_color=(245, 39, 20), bold_text=True,function=reset_game, state = "selected"))
   
    #Paused Selected
    buttons.append(Button(window, width//2-220,80, 115, 30, text ='Pause life!',color=(14, 207, 197),hover_color=(163, 255, 250), bold_text=True,function=pause_game, state="selected"))
    
    #Random Colors Selected
    buttons.append(Button(window, width//5 - 100,40, 160, 30, text ='Random Colors!',color=(219, 168, 86),hover_color=(245, 197, 120), bold_text=True,function=random_color, state = "selected"))
  
  #------------ Random Colors
     
    #Reset Grid Random Colors
    buttons.append(Button(window, width//2 -80,80, 150, 30, text ='Restart life!',color=(197, 32, 17,),hover_color=(245, 39, 20), bold_text=True,function=reset_game, state = "random_color"))  
   
    #Paused Random Colors
    buttons.append(Button(window, width//2-220,80, 115, 30, text ='Pause life!',color=(14, 207, 197),hover_color=(163, 255, 250), bold_text=True,function=pause_game, state="random_color"))
    
    #Forword Random Colors
    buttons.append(Button(window, width//5 + 330,80, 150, 30, text ='Speed up life!',color=(233, 245, 15),hover_color=(255, 251, 0), bold_text=True,function=fast_foward_game,state = "random_color"))
      
    return buttons



    #Button Funtionality 
def run_game():
    global state
    state = 'running'

def pause_game():
    global state
    state = 'pause'

def fast_foward_game():
    global state
    state = 'forward'
    
def reset_game():
    global state
    state = 'setting'
    game_window.clear()


def pre_set_game():
    global state
    state = 'selected'
    game_window.pre_set_grid()

def random_color():
    global state
    state = 'random_color'
    game_window.random_color()

# Game intialization
pygame.init() #stat game
window = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()
game_window = Game_window(window, 100 , 180)
buttons = make_button()
state = 'setting'

#Game Loop
while running:
    mouse_pos = pygame.mouse.get_pos()

    if state =='setting':
        get_events()
        update()
        draw()

    if state =='running':
        FPS = 8
        running_get_events()
        running_update()
        running_draw()

    if state =='pause':
        pause_get_events()
        pause_update()
        pause_draw()
    
    if state == 'random_color':
        running_get_events()
        running_update()
        running_draw()


    if  state == 'forward':
        FPS = 1000
        forward_events()
        forward_update()
        forward_draw()

    if state == "selected":
        selected_get_events()
        selected_update()
        selected_draw()


    pygame.display.update()
    clock.tick(FPS)
    print(state)
pygame.quit()
sys.exit()

