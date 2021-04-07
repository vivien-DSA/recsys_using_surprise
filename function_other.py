from function_other import *
from grid_class import *

pygame.font.init()


def redraw_window(game_interface, board, time, errors):
    game_interface.fill(light_gray)
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time =" + format_time(time), 1, (0,0,0))
    game_interface.blit(text, (cell_size, 0.5*cell_size))
    # Draw errors
    text = fnt.render("Errors = "+str(1 * errors), 1, red)
    game_interface.blit(text, (width_grid, 0.5* cell_size))
    # Draw grid and board
    board.draw(game_interface)
    board.draw_area(game_interface)


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

# Quit the game
def game_quit():
    pygame.quit()
    quit()
# Game introduction
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        game_interface.fill(light_gray)
        font_obj = pygame.font.Font('freesansbold.ttf', 25)
        text_surface_obj = font_obj.render('WELCOME TO KEMARU GAME', True, black, light_gray)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = ( 7*cell_size,4*cell_size)
        game_interface.blit(text_surface_obj, text_rect_obj)

        button("play", 2*cell_size,12*cell_size,2*cell_size,cell_size,light_blue,blue,one_level)
        button("Quit", 5*cell_size,12*cell_size,2*cell_size,cell_size,light_blue,blue,game_quit)
        button("Read me", 8*cell_size,12*cell_size,3*cell_size,cell_size,light_blue,blue,None)
        pygame.display.update()

# Create a Button
def button( msg, x, y, w, h, active_color, inactive_color, action=None):
    # Location of the mouse
    mouse = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_interface, active_color, (x, y, w, h))
        if press[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(game_interface, inactive_color, (x, y, w, h))

    font_obj = pygame.font.Font('freesansbold.ttf', 15)
    text_surface_obj = font_obj.render(msg, True, white, inactive_color)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (x + int(w / 2), y + int(h / 2))
    game_interface.blit(text_surface_obj, text_rect_obj)
