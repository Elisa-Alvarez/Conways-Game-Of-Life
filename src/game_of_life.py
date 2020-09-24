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
     if state == "running":
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

#Clear
def clear_get_events():
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

def clear_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state = state)

def clear_draw():
     window.fill(background)
     for button in buttons:
        button.draw()
     game_window.gen()
     game_window.draw()

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
    buttons.append(Button(window, width//2 - 100,80, 150, 30, text ='Let us live!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function= run_game, state= "setting"))
    #Pause
    buttons.append(Button(window, width//2-220,80, 115, 30, text ='Pause life!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=pause_game, state="running"))
    #Fast Forward
    buttons.append(Button(window, width//5 + 330,80, 150, 30, text ='Speed up life!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=fast_foward_game,state = "running"))
    #Resume
    buttons.append(Button(window, width//2- 200,80, 150, 30, text ='Resume life!',color=(72, 169, 20),hover_color=(80, 197, 17), bold_text=True,function=run_game, state = "forward"))
    #Reset Grid
    buttons.append(Button(window, width//2 + 20,80, 150, 30, text ='Restart life!',color=(197, 32, 17,),hover_color=(245, 39, 20), bold_text=True,function=reset_game, state = "pause"))
    #Preset Grid
    buttons.append(Button(window, width//2 - 100,20, 150, 30, text ='Chosen Life!',color=(50, 137, 168),hover_color=(174, 217, 232), bold_text=True,function=pre_set_game, state = "setting"))
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


    if  state == 'forward':
        FPS = 1000
        forward_events()
        forward_update()
        forward_draw()

    if state == "selected":
        selected_get_events()
        selected_update()
        selected_draw()

    if state =='clear':
        clear_get_events()
        clear_update()
        clear_draw()

    pygame.display.update()
    clock.tick(FPS)
    print(state)
pygame.quit()
sys.exit()

