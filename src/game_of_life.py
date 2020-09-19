import pygame
import sys
import os
from game_window_class import *

# Varibles for Game
width,height = 1000,900
background = (199,199,199)
FPS = 60

# Game Methods/Actions
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

def update():
   
    game_window.update()

def draw():
     window.fill(background)
     game_window.draw()
   
# Game intialization
pygame.init()
window = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()
game_window = Game_window(window, 250 , 180)

#Game Loop
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()

