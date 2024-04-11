from graphics import *

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_line = Line(Point(x1, y1), Point(x1, y2))
        top_line = Line(Point(x1, y1), Point(x2, y1))
        right_line = Line(Point(x2, y1), Point(x2, y2))
        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_left_wall:
            self._win.draw_line(left_line)
        else:
            self._win.draw_line(left_line,'white')
        if self.has_top_wall:
            self._win.draw_line(top_line)
        else:
            self._win.draw_line(top_line,'white')
        if self.has_right_wall:
            self._win.draw_line(right_line)
        else:
            self._win.draw_line(right_line,'white')
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line)
        else:
            self._win.draw_line(bottom_line,'white')

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        mid_to_mid_line = Line(Point(x_mid,y_mid),
                                Point(to_x_mid,to_y_mid))
        self._win.draw_line(mid_to_mid_line,fill_color)
