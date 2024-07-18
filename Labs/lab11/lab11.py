from Grid import Grid
import random

def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def random_rocks(grid, chance_of_rock):
    '''Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    # assert 0 <= chance_of_rock <= 1
    # copied_grid = grid.copy()
    # for y in range(copied_grid.height):
    #     for x in range(copied_grid.width):
    #         rock_roll = random.random()
    #         if copied_grid.array[y][x] is None and rock_roll <= chance_of_rock:
    #             copied_grid.array[y][x] = 'r'
    # return copied_grid
    copied_grid = grid.copy()
    rocks = lambda x, y: copied_grid.set(x, y, 'r')
    return modify_grid(copied_grid, rocks, chance_of_rock)


def random_bubbles(grid, chance_of_bubbles):
    '''Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    # assert 0 <= chance_of_bubbles <= 1
    # copied_grid = grid.copy()
    # for y in range(copied_grid.height):
    #     for x in range(copied_grid.width):
    #         rock_roll = random.random() -- ERROR: rolling even if array is not empty creates inconsistency with test
    #         if copied_grid.array[y][x] is None and rock_roll <= chance_of_bubbles:
    #             copied_grid.array[y][x] = 'b'
    # return copied_grid
    copied_grid = grid.copy()
    bubbles = lambda x, y: copied_grid.set(x, y, 'b')
    return modify_grid(copied_grid, bubbles, chance_of_bubbles)


def modify_grid(grid, func, prob):
    """Write a function which can take in a grid, a function
    and a probablily as parameters and updates the grid using
    the function passed in."""
    "*** YOUR CODE HERE ***"
    assert 0 <= prob <= 1
    for y in range(grid.height):
        for x in range(grid.width):
            # rock_roll = random.random()
            # if grid.array[y][x] is None and rock_roll <= prob:
            #     func(x, y)
            if grid.array[y][x] is None:
                rock_roll = random.random()
                if rock_roll <= prob:
                    func(x, y)
    return grid


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    "*** YOUR CODE HERE ***"
    assert grid.array[y][x] == 'b'
    assert y > 0, "Bubble is already at the top of the grid"
    assert grid.get(x, y - 1) is None, "The array above the bubble is taken"
    copied_grid = grid.copy()
    copied_grid.set(x, y, None)
    copied_grid.set(x, y - 1, 'b')
    return copied_grid


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    copied_grid = grid.copy()
    for y in range(copied_grid.height):
        for x in range(copied_grid.width):
            if copied_grid.array[y][x] == 'b' and y > 0 and copied_grid.get(x, y-1) is None:
                copied_grid = bubble_up(copied_grid, x, y)
    return copied_grid



def animate_grid(grid, delay):
    """Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1
