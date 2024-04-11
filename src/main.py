from graphics import *
from cell import *
from maze import *


def main():
    window_width = 600
    window_height = 450
    win = Window(window_width, window_height)

    maze_root_x = 50
    maze_root_y = 50
    num_rows = 8
    num_cols = 12
    cell_size_x = 42
    cell_size_y = 42
    maze = Maze(maze_root_x,maze_root_y,
                num_rows,num_cols,
                cell_size_x,cell_size_y,
                win,
                seed=None)
    
    if maze.solve():
        print('tadaaa')
    else:
        print('debug to do')
    
    win.wait_for_close()

main()