import random
import sys
import pygame


class Game_Of_Life:

    def __init__(self, screen_width=800, screen_height=600, cell_size=10, alive_color=(0, 255, 255),
                 dead=(0, 0, 0), max_fps=10):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.alive_color = alive_color
        self.dead = dead

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clear_screen()
        pygame.display.flip()

        self.max_fps = max_fps

        self.alive = 0
        self.num_cols = int(self.screen_width / self.cell_size)
        self.num_rows = int(self.screen_height / self.cell_size)
        self.grids = []
        self.init_grids()
        self.update()

        self.paused = False
        self.game_over = False

    def init_grids(self):
        def create_grid():
            rows = []
            for row_num in range(self.num_rows):
                list_of_columns = [0] * self.num_cols
                rows.append(list_of_columns)
            return rows
        self.grids.append(create_grid())
        self.grids.append(create_grid())

    def update(self, value=None, grid=0):
        for f in range(self.num_rows):
            for l in range(self.num_cols):
                if value is None:
                    cell_value = random.randint(0, 1)
                else:
                    cell_value = value
                self.grids[grid][f][l] = cell_value

    def draw(self):
        self.clear_screen()
        for i in range(self.num_cols):
            for f in range(self.num_rows):
                if self.grids[self.alive][f][i] == 1:
                    color = self.alive_color
                else:
                    color = self.dead
                pygame.draw.circle(self.screen,
                                   color,
                                   (int(i * self.cell_size + (self.cell_size / 2)),
                                    int(f * self.cell_size + (self.cell_size / 2))),
                                   int(self.cell_size / 2),
                                   0)
        pygame.display.flip()

    def clear_screen(self):

        self.screen.fill(self.dead)

    def get_cell(self, row_num, col_num):

        try:
            cell_value = self.grids[self.alive][row_num][col_num]
        except:
            cell_value = 0
        return cell_value

    def get_neighbors(self, row, cols):
   
        neighbor_count = 0
        neighbor_count += self.get_cell(row - 1, cols - 1)
        neighbor_count += self.get_cell(row - 1, cols)
        neighbor_count += self.get_cell(row - 1, cols + 1)
        neighbor_count += self.get_cell(row, cols - 1)
        neighbor_count += self.get_cell(row, cols + 1)
        neighbor_count += self.get_cell(row + 1, cols - 1)
        neighbor_count += self.get_cell(row + 1, cols)
        neighbor_count += self.get_cell(row + 1, cols + 1)

      
        if self.grids[self.alive][row][cols] == 1:  # alive
            if neighbor_count > 3:  # Overpopulation
                return 0
            if neighbor_count < 2:  # Underpopulation
                return 0
            if neighbor_count == 2 or neighbor_count == 3:
                return 1
        elif self.grids[self.alive][row][cols] == 0:  # dead
            if neighbor_count == 3:
                return 1  # come to life

        return self.grids[self.alive][row][cols]

    def update_generation(self):
 
        self.update(0, self.not_alive())
        for r in range(self.num_rows - 1):
            for c in range(self.num_cols - 1):
                next_gen_state = self.get_neighbors(r, c)
                self.grids[self.not_alive()][r][c] = next_gen_state
        self.alive = self.not_alive()

    def not_alive(self):

        return (self.alive + 1) % 2

    def get_event(self):
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == 's':
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif event.unicode == 'r':
                
                    self.alive = 0
                    self.update(None, self.alive)  # randomize
                    self.update(0, self.not_alive())  # set to 0
                    self.draw()
                elif event.unicode == 'q':
                  
                    self.game_over = True
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):

        clock = pygame.time.Clock()

        while True:
            if self.game_over:
                return

            self.get_event()

            if not self.paused:
                self.update_generation()
                self.draw()

            clock.tick(self.max_fps)