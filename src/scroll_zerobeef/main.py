import curses

from icecream import ic
from modules import (ColumnManager, ScrollManager, terminal_size,
                     test_column_size)


def main(stdscr):
    with open("./modules/scroll/lipsum.txt", "r") as f:
        t = f.read()
    x = list(map(lambda x, y: "{x}={y}", t, [i for i in range(0, len(t))]))
    Columns = ColumnManager(stdscr, 2, 3, x)
    Columns.draw()
    stdscr.getch()


if __name__ == "__main__":
    ic(terminal_size())
    test_column_size()
    with open("./modules/scroll/lipsum.txt", "r") as f:
        t = f.read()
    t = t.split(".")
    scrolling_text = ScrollManager(data=t, viewable_lines=5)
    for _, _ in enumerate(t):
        print(str(scrolling_text))
        print()
        if not scrolling_text.scroll("UP"):
            break
    curses.wrapper(main)
