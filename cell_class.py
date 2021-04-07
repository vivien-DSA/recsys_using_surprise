
class Cell:
    rows = nb_cells
    cols = nb_cells

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, game_interface):
        #       if grid == grid_1:

        fnt = pygame.font.SysFont("comicsans", 40)

        cell_size = self.width / nb_cells
        x = self.col * cell_size
        y = self.row * cell_size

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            game_interface.blit(text, (x + 5 + start_x, y + 5 + start_y))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            game_interface.blit(text, (x + (cell_size / 2 - text.get_width() / 2) + start_x,
                                       y + start_y + (cell_size / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(game_interface, (200, 0, 0), (x + start_x, y + start_y, cell_size, cell_size), 8)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val

