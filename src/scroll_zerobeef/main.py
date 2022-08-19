from icecream import ic
from modules import terminal_size, test_column_size
from modules import ScrollManager

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
