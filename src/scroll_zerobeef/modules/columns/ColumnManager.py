from modules import terminal_size, config, ScrollManager, set_preferred, test_column_size
from menu_zerobeef.data import ItemSingleSelection
from curses.textpad import rectangle
from curses import newwin


class ColumnManager(object):
    def __init__(self, stdscr, columns, viewable_lines, data, **kwargs):
        self.terminal_rows, self.terminal_columns = list(map(lambda item: int(item), terminal_size()))
        self.columns = columns
        self.viewable_lines = viewable_lines
        self.position = 0
        self.focused_column = 0
        self.columns_data = map(lambda objects: ScrollManager(data=objects), data)
        self.stdscr = stdscr
        self.kwargs = kwargs
        self.windows = None

    def draw(self):
        set_preferred(self.columns, columns=True)
        if not test_column_size():
            raise ValueError("Column size is not supported")
        self.split_terminal()

    def split_terminal(self):
        self.windows = []
        column_width = self.terminal_columns // self.columns
        for i in range(0, self.columns):
            win = newwin(self.terminal_rows, column_width, 0, (0+(i*column_width)))
            self.windows.append(win)
            rectangle(win, 0, 0, self.terminal_rows - 1, column_width - 1)

    def __action__(self):
        column_data = self.get_column_data(self.focused_column)
        position = self.position
        item = column_data[position]
        if type(item) is ItemSingleSelection:
            item.take_action()

    def get_positions(self):
        # Pack variables together for easier handling later.
        return self.position, self.focused_column, map(lambda items: items.get_viewable_lines(), self.columns_data)

    def __setstate__(self, state):
        if state is None or state == "":
            raise ValueError("state is incorrectly set!")
        if state in ("UP", "DOWN"):
            change_position = lambda current_position: current_position + self.position if state == "UP" \
                else current_position - 1
            self.position = change_position(1)

    def get_column_data(self, focused_column):
        return self.columns_data[focused_column]
