from copy import deepcopy


class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.array = [[None for x in range(self.width)] for y in range(self.height)]
        # templist = []
        # self.array = []
        #
        # for i in range(self.width):
        #     templist.append(None)
        # for j in range(self.height):
        #     self.array.append(list(templist))

    def in_bounds(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        else:
            return True

    def get(self, x, y):
        if self.in_bounds(x, y) is True:
            return self.array[y][x]
        else:
            raise IndexError("The given coordinates are not inbounds.")

    def set(self, x, y, val):
        if self.in_bounds(x, y) is True:
            self.array[y][x] = val
        else:
            raise IndexError("The given coordinates are not inbounds.")

    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __repr__(self):
        grid_list = []
        for y in range(self.height):
            grid_list.append(self.array[y])
        return f'Grid.build({grid_list})'

    def __eq__(self, other):
        if isinstance(other, Grid) is True:
            return self.array == other.array
        elif isinstance(other, list) is True:
            return self.array == other
        else:
            return False

    @staticmethod
    def check_list_malformed(lst):
        if isinstance(lst, list) is False:
            raise ValueError("The object is not a list.")
        if len(lst) == 0:
            raise ValueError("The object is empty.")
        for x in range(len(lst)):
            if isinstance(lst[x], list) is False:
                raise ValueError(f"The element with index {x} is not a list.")
        for x in range(1, len(lst)):
            if len(lst[x]) != len(lst[0]):
                raise ValueError(f"Not all elements have the same length.")

    @staticmethod
    def build(lst):
        if Grid.check_list_malformed(lst) is None:
            grid = Grid(len(lst[0]), len(lst))
            for y in range(grid.height):
                for x in range(grid.width):
                    value = deepcopy(lst[y][x])
                    grid.set(x, y, value)
            return grid

    def copy(self):
        new_grid = deepcopy(self)
        return new_grid










