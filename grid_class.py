
from grid_class import *
import pygame
from Constraint import *

pygame.font.init()




class Grid:
    board = grid_1

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cells[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row,col)) and solve(self.model):
                return True
            else:
                self.cells[row][col].set(0)
                self.cells[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cells[row][col].set_temp(val)

    # put the color
    def draw_color_cell(self, color, start_x, start_y):
        corner_list = [(start_x, start_y), (start_x, start_y + cell_size),
                       (start_x + cell_size, cell_size + start_y), (cell_size + start_x, start_y)]
        pygame.draw.polygon(game_interface, color, corner_list)

    def draw(self, game_interface):
        # Draw Grid Lines
        cell_size = self.width / nb_cells
        for i in range(self.rows+1):
            thick = 3
            pygame.draw.line(game_interface, black, (start_x, int(i*cell_size)+ start_y), (self.width+ start_x, int(i*cell_size)+start_y), thick)
            pygame.draw.line(game_interface, black, (int(i * cell_size)+start_x, 0+start_y), (int(i * cell_size)+ start_x, self.height+start_y), thick)

        # Draw cells
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(game_interface)

    # Draw the area
    def draw_area(self, game_interface):
        thick = 8
        # Horizontal Line meaning rows
        pygame.draw.line(game_interface, black, (start_x, start_y),
                         ( self.width + start_x, start_y), thick)
        pygame.draw.line(game_interface, black, (start_x+4*cell_size, start_y+cell_size),
                         ( self.width + 2*cell_size, start_y+cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x, start_y+2*cell_size),
                         ( self.width - 2*cell_size, start_y+ 2*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+6*cell_size, start_y+2*cell_size),
                         ( self.width, start_y+ 2*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x, start_y+3*cell_size),
                         ( self.width - cell_size, start_y+ 3*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+7*cell_size, start_y+3*cell_size),
                         ( self.width +2*cell_size, start_y+ 3*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+3*cell_size, start_y+4*cell_size),
                         ( self.width - 3*cell_size, start_y+ 4*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+6*cell_size, start_y+4*cell_size),
                         ( self.width+cell_size , start_y+ 4*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+cell_size, start_y+5*cell_size),
                         ( self.width - cell_size, start_y+ 5*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x, start_y+6*cell_size),
                         ( self.width - 5*cell_size, start_y+ 6*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+5*cell_size, start_y+6*cell_size),
                         ( self.width + 2* cell_size, start_y+ 6*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+cell_size, start_y+7*cell_size),
                         ( self.width - 2*cell_size, start_y+ 7*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 3*cell_size, start_y+8*cell_size),
                         ( self.width + 2*cell_size, start_y+ 8*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x, start_y+9*cell_size),
                         ( self.width +2*cell_size, start_y+ 9*cell_size), thick)
        # Vertical Line meaning colums
        pygame.draw.line(game_interface, black, (start_x, start_y),
                         ( start_x, self.height + 2*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+cell_size, start_y+ 3*cell_size),
                         ( start_x+ cell_size, start_y+5*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+cell_size , start_y+7*cell_size),
                         ( start_x+cell_size, start_y+ 9*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+2*cell_size, start_y),
                         ( start_x+2*cell_size, start_y+ 2*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+2*cell_size, start_y+5*cell_size),
                         ( start_x+2*cell_size, start_y+ 7*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+3*cell_size, start_y+4*cell_size),
                         ( start_x +3*cell_size, start_y+ 5*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+3*cell_size, start_y+8*cell_size),
                         ( start_x + 3*cell_size, start_y+ 9*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+4*cell_size, start_y),
                         ( start_x+4*cell_size , start_y+ cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+4*cell_size, start_y+2*cell_size),
                         ( start_x+4*cell_size, start_y+ 4*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+4*cell_size, start_y+5*cell_size),
                         ( start_x + 4*cell_size, start_y+ 8*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+5*cell_size, start_y+cell_size),
                         ( start_x + 5*cell_size, start_y+ 2*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 5*cell_size, start_y+6*cell_size),
                         ( start_x + 5*cell_size, start_y+ 7*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 5*cell_size, start_y+8*cell_size),
                         ( start_x + 5*cell_size, start_y+ 9*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 6*cell_size, start_y+2*cell_size),
                         ( start_x + 6*cell_size, start_y+ 5*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 7*cell_size, start_y+cell_size),
                         ( start_x + 7*cell_size, start_y+ 3*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 7*cell_size, start_y+4*cell_size),
                         ( start_x + 7*cell_size, start_y+ 8*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 8*cell_size, start_y+3*cell_size),
                         ( start_x + 8*cell_size, start_y+ 4*cell_size), thick)
        pygame.draw.line(game_interface, black, (start_x+ 9*cell_size, start_y),
                         ( start_x + 9*cell_size, start_y+ 9*cell_size), thick)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].selected = False

        self.cells[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_temp(0)

    def click(self, pos):
        cell_size = self.width / nb_cells
        if start_x < pos[0] < self.width+start_x and start_y < pos[1] < self.height+start_y:
            x = pos[0] // cell_size
            y = pos[1] // cell_size
            return (int(y)-2,int(x)-2)
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value == 0:
                    return False
        return True
