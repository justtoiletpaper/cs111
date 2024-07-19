from Grid import Grid


class Particle:

    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        return f'{type(self).__name__}({self.x},{self.y})'

    def move(self):
        new_position = self.physics()
        if new_position is None:
            pass
        else:
            self.grid.array[self.y][self.x] = None
            self.x = new_position[0]
            self.y = new_position[1]
            self.grid.array[self.y][self.x] = self



