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
            print("The given coordinates are not in bounds.")

    def set(self, x, y, val):
        if self.in_bounds(x, y) is True:
            self.array[y][x] = val
        else:
            print("The given coordinates are not inbounds.")

    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __eq__(self, other):
        if isinstance(other, Grid) is False:
            return False
        else:
            return self.array == other.array
