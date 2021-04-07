import pygame

# Define size of the interface of the game and the grid
nb_cells = 9
cell_size = 40
width_grid = nb_cells * cell_size
height_grid = nb_cells * cell_size
width = width_grid + 4*cell_size
height = height_grid + 5*cell_size
start_x = 2*cell_size
start_y = 2*cell_size
game_interface = pygame.display.set_mode((width, height))


red = (255, 0, 0)
cream = (250, 210, 188)  # cream color
light_gray = (211,211,211)
white = (255,255,255)
black = (0,0,0)
blue = (0, 0, 255)  # blue color
light_blue = (12, 50, 200)  # light blue color