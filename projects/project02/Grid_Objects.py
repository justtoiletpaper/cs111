from Grid import Grid
from Particle import Particlegit


class Sand(Particle):

    def is_move_ok(self, x, y):
        if self.grid.in_bounds(x, y):
            # checks to see if sand is traveling straight down and if that array is empty
            if x == self.x and y == self.y + 1 and self.grid.array[y][x] is None:
                return True
            # checks to see if sand is traveling diagonally down and if that array and its above array is empty
            elif (x == self.x - 1 or x == self.x + 1) and y == self.y + 1:
                if self.grid.array[y][x] is None and self.grid.array[self.y][x] is None:
                    return True
            else:
                return False
        else:
            return False

    def physics(self):
        if self.is_move_ok(self.x, self.y + 1) is True:
            new_position = (self.x, self.y + 1)
            return new_position
        elif self.is_move_ok(self.x - 1, self.y + 1) is True:
            new_position = (self.x - 1, self.y + 1)
            return new_position
        elif self.is_move_ok(self.x + 1, self.y + 1) is True:
            new_position = (self.x + 1, self.y + 1)
            return new_position
        else:
            return None


class Rock(Particle):

    def physics(self):
        return None

class Bubble(Particle):

    def is_move_ok(self, x, y):
        if self.grid.in_bounds(x, y):
            # checks to see if sand is traveling straight down and if that array is empty
            if x == self.x and y == self.y - 1 and self.grid.array[y][x] is None:
                return True
            # checks to see if sand is traveling diagonally down and if that array and its above array is empty
            elif (x == self.x - 1 or x == self.x + 1) and y == self.y - 1:
                if self.grid.array[y][x] is None and self.grid.array[self.y][x] is None:
                    return True
            else:
                return False
        else:
            return False

    def physics(self):
        if self.is_move_ok(self.x, self.y - 1) is True:
            new_position = (self.x, self.y - 1)
            return new_position
        elif self.is_move_ok(self.x + 1, self.y - 1) is True:
            new_position = (self.x + 1, self.y - 1)
            return new_position
        elif self.is_move_ok(self.x - 1, self.y - 1) is True:
            new_position = (self.x - 1, self.y - 1)
            return new_position
        else:
            return None
