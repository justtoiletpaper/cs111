import random


def in_range1(n):
    """Write a function that checks to see if n is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    "*** YOUR CODE HERE ***"
    if n >= 1 and n <= 100:
        return True
    else:
        return False


def in_range2(num):
    """Redo in_range1, but throw an exception instead of
    throwing false
    """
    "*** YOUR CODE HERE ***"
    if num < 1 or num > 100:
        raise ValueError("Number must be between 1 and 100")
    return None


def main():
    """Write code in the main function that generates 1000 
    random numbers between 1 and 101 and calls the generated 
    function to validate the number generated."""
    "*** YOUR CODE HERE ***"
    counter = 0
    while counter < 1000:
        result = random.randint(1, 101)
        try:
            in_range2(result)
            counter += 1
        except ValueError as e:
            print(f"An error occurred: {type(e)}. Error Information: {e}")



