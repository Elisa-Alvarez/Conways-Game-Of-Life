# Conways-Game-Of-Life


## Rules for Conway's Game of Life

1. Cells that are alive must have 2-3 neighbors to stay alive

2. Cells that have less than 2 neighbors dies

3. Cells with more than 3 neighbors dies


True = live cell (Black)

Fals = dead cell (White)

----

## Installing Pygame

Pygame is a game library made for pyhton. To install you must have python and pip installed and used the command `pip install pygame`

----

## To Start Game

In the command line use python game_of_life.py and the pygame window will pop up. 

### Playing the game

To exit press `X` on the top right of the screen, in future updates will inculed the ability to change the game window size and allow it to minimize. When user press `r` a random grid will appear and will run when `Let's Us Live` button.

`Let us live` = Start game
`Chosen Life` = Pre-set grid will run
`Random Color` = Will change the color randomly
`Speed Up Life` =  Changes the frames per second from 5 to 1000 miliseconds
`Resume Life` = Will continue the fps at 5 miliseconds and continued when paused.
`Restart Life` = Resets the grid to the begining
`Pause Life` = Will stop the game loop until you reset or resume game.

----

## Making Changes and File Structure

The game is ran in the file `game_of_life.py`. This file contains the game loop and to eddit the buttons and their fucnctionality, grid position, and sets the state.

**The state of the buttons:**
Buttons will apear in specific state which is passed in when the Button class is made on game_of_life.py 
   -Setting: The pre game grid and akkiws the user the to click the grid and create shapes.
   -Running: When  game is started the state is changed to running.
   -Forward: Speed will increase until the resume or rest is clicked
   -Random_Color: Will generate random colors and when another button is pushed the state will refresh to running and the colors will continue until reset
   -Pause: Game play will stop 
   -Selected: Will generate a grid created on `game_window_class.py` file
  
  ----
  
  ### The Grid

**The grid:** This is a python class on `game_window_class.py` you can add rows and change the height and width here. Before the game loop the varible game_window is created. This allows you to set where in the pygame window you would lik the grid to be set.

<br>
<br>

**Grid Cells:** The individual alive "cells" in the game are individual boxes that are set into the grind in `game_window_class.py` as the self.grid. If you would like to change the cells the `cell_class.py` has the sized of the cell so it can be adujusted as long as the  grid and the functions `mouse_on_grid` and `click_cell` are adjusted to the new dimentions.
 
