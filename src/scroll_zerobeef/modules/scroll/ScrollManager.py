from modules import terminal_size
from icecream import ic


class ScrollManager(object):
    def __init__(self, *args, **kwargs):
        """
        __init__(self, *args, **kwargs) -> None
            The class constructor for the ScrollManager class.

        :param args:
            No args should be passed to the constructor
        :param kwargs:
            Arguments such as lines, columns, etc. should be passed to
            the constructor inorder to avoid unexpected behaviour. Data
            is a required argument to the constructor which without it
            gives you no lines when scrolling
        """
        self.lines = kwargs.pop('lines', int(terminal_size()[0]) - 1)
        self.columns = kwargs.pop('columns', int(terminal_size()[1]))
        self.viewable_lines = kwargs.pop('viewable_lines', self.lines)
        self.data = kwargs.pop('data', None)
        self.offset = 0
        if self.viewable_lines > self.lines:
            self.viewable_lines = self.lines - 1

    def __getattr__(self, name):
        ic(self)

    def get_viewable_lines(self):
        start_line = self.offset
        end_line = self.offset + self.viewable_lines
        return "" if len(self.data) == 0 else self.data[start_line:end_line]

    def scroll(self, direction):
        if self.offset + 1 < len(self.data) - self.viewable_lines \
                and direction == "UP":
            self.offset = self.offset + 1
            return True
        elif self.offset + self.viewable_lines >= self.viewable_lines \
                and direction == "DOWN":
            self.offset = self.offset - 1
            return True
        elif direction not in ("UP", "DOWN"):
            raise EnvironmentError("direction is incorrect it has to be UP or DOWN")
        return False

    def __str__(self):
        return str(''.join(map(lambda item: f"{item}.\r\n", self.get_viewable_lines())))
