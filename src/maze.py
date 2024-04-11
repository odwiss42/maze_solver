from cell import *
from time import sleep
import random

class Maze:
    def __init__(
        self,
        x,
        y,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = self._x + self._cell_size_x * i
        cell_x2 = self._x + self._cell_size_x * (i + 1)
        cell_y1 = self._y + self._cell_size_y * j
        cell_y2 = self._y + self._cell_size_y * (j + 1)
        self._cells[i][j].draw(cell_x1,cell_y1,
                               cell_x2,cell_y2)
        self._animate(0.01)
    
    def _animate(self,tick):
        if self._win is None:
            return
        self._win.redraw()
        sleep(tick)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _get_adjacent_cells(self,i,j):
        #determine which directions a cell is present relative to current position
        adjacent_cells = []
        if j > 0:
            adjacent_cells.append((i,j-1))
        if i < self._num_cols - 1:
            adjacent_cells.append((i+1,j))
        if j < self._num_rows - 1:
            adjacent_cells.append((i,j+1))
        if i > 0:
            adjacent_cells.append((i-1,j))
        return adjacent_cells

    def _get_adj_to_visit(self, adjacent_cells):
        return [c for c in adjacent_cells if self._cells[c[0]][c[1]]._visited == False]
    
    def _break_walls_r(self,i,j):
        current = self._cells[i][j]
        current._visited = True

        while True:
            #Get adjacent cells
            adjacent = self._get_adjacent_cells(i,j)

            #add those who haven't been visited yet to a list
            to_visit = self._get_adj_to_visit(adjacent)

            #draw result and break out if there aren't any
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            # choose direction to go at random
            dir = to_visit[random.randrange(0,len(to_visit))]
            target = self._cells[dir[0]][dir[1]]

            #break walls
            #north
            if dir[1] < j:
                current.has_top_wall = False
                target.has_bottom_wall = False
            #east
            if dir[0] > i:
                current.has_right_wall = False
                target.has_left_wall = False
            #south
            if dir[1] > j:
                current.has_bottom_wall = False
                target.has_top_wall = False
            #west
            if dir[0] < i:
                current.has_left_wall = False
                target.has_right_wall = False

            #call break walls on the next cell
            self._break_walls_r(dir[0],dir[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False
    
    def solve(self) -> bool:
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        current = self._cells[i][j]
        #draw
        self._animate(0.1)

        #mark passage
        current._visited = True

        #goal check
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        #Get adjacent cells
        adjacent = self._get_adjacent_cells(i,j)

        #add those who haven't been visited yet to a list
        to_visit = self._get_adj_to_visit(adjacent)

        for dir in to_visit:
            target = self._cells[dir[0]][dir[1]]
            #check walls and move
            #north
            if dir[1] < j and current.has_top_wall == False:
                current.draw_move(target)
                if self._solve_r(dir[0],dir[1]):
                    return True
                current.draw_move(target, undo=True)
            #east
            if dir[0] > i and current.has_right_wall == False:
                current.draw_move(target)
                if self._solve_r(dir[0],dir[1]):
                    return True
                current.draw_move(target, undo=True)
            #south
            if dir[1] > j and current.has_bottom_wall == False:
                current.draw_move(target)
                if self._solve_r(dir[0],dir[1]):
                    return True
                current.draw_move(target, undo=True)
            #west
            if dir[0] < i and current.has_left_wall == False:
                current.draw_move(target)
                if self._solve_r(dir[0],dir[1]):
                    return True
                current.draw_move(target, undo=True)
            
            #if all failed
                return False

        