from random import randint


def randNumUpTo(n):
    return lambda: randint(1,n)


oneToHundred = randNumUpTo(100)