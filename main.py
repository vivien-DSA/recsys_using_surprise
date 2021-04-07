
from function_other import *
from grid_class import *
import time
pygame.font.init()


def one_level():
    pygame.display.set_caption("Kemaru Game")

    board = Grid(nb_cells, nb_cells, width_grid, height_grid)

    key = None
    run = True
    start = time.time()
    errors = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cells[i][j].temp != 0:
                        if board.place(board.cells[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            errors += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    print(clicked)
                    key = None

        if board.selected and key != None:
            board.sketch(key)
        redraw_window(game_interface, board, play_time, errors)
        button("Help", 2*cell_size,12*cell_size,2*cell_size,cell_size,light_blue,blue,None)
        button("Quit", 5*cell_size,12*cell_size,2*cell_size,cell_size,light_blue,blue,game_intro)
        button("Read me", 8*cell_size,12*cell_size,3*cell_size,cell_size,light_blue,blue,None)
        pygame.display.update()


game_intro()
#game_intro()
pygame.quit()
