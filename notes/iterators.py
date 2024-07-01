# An iterator is an object that provides sequential access to values, one by one.
inter(iterable) # Returns an iterator over the elements of an iterable.
next(iterator)  # Returns the next element in an iterator

toppings = ["pineapple", "pepper", "mushroom", "red pepper"]
topperator = iter(toppings)
next(topperator) # "pineapple"
next(topperator) # "pepper"

# Calling iter() on an interator just returns the iterator:
numbers = [1, 2, 3, 4, 5]
num_iter = iter(numbers)
num_iter2 = iter(num_iter)

num_iter is num_iter2   # True, both will always be pointed at the same iterator object

#  When used in a for loop, Python will call next() on the iterator in each iteration
nums = range(1, 4)
num_iter = iter(nums)
for num in num_iter:
    print(num)      #  1, 2, 3

# Lists, tuples, dictionaries, strings, and ranges are all iterable objects
best_topping = "pineapple"
# iter() can return an iterator for any iterable object
topping_iter = iter(best_topping)
next(topping_iter)      # "p"

# In Python 3.6+, items in a dict are ordered according to when they were added.
prices = {"pineapple": 9.99, "pen": 2.99, "pineapple-pen": 19.99}
# An iterator for the keys
price_iter = iter(prices.keys())
#  An iterator for the values
price_iter2 = iter(prices.values())

# Iterators are mutable! Once the iterator moves forward, it won't return the value that came before.
nums = range(1, 4)
num_iter = iter(nums)
first = next(num_iter) # 1

for num in num_iter:
    print(num)      # 2, 3           The 1st value is skipped because it was iterated earlier

"""Iterators will not react retrospectively to changes in an object. Changes must be made before using the next() 
function in order for the iter to reflect the change in the list."""

# Code that processes an iterator using iter() or next() makes few assumptions about the data itself.
# An iterator bundles together a sequence and a position with the sequence in a single object.

# Passing the iterator to another function always retains its position.
# Ensures that each element of the sequence is only processed once.

"""Useful built in functions"""
list(iterable)  # Returns a list containing all items in an iterable
tuple(iterable)     # Returns a tuple containing all items in iterable
sorted(iterable)    # Returns a sorted list containing all items in iterable: < operator by default
reversed(sequence)      # Iterate over item in sequence in reversed order
zip(*iterables)  # Iterate over co-indexed tuples with elements from each of the iterables
map(func, iterables, ....)  # Iteration over func(x) for x in iterable
        """Same as [func(x) for x in iterable]"""
filter (func, iterable)     # Iterate over x in iterable if func(x)
        """Same as list comprehension [x for x in iterable if func(x)]"""


"""Generators"""
# A generator function uses yield instead of return:
def evens():
    num = 0
    while num < 10:
        yield num
        num += 2
# A generator is a type of iterator that yields results from a generator function
# Just call the generator function to get back a generator:
even_gen = evens()
next(even_gen)  # 0
next(even_gen)  # 2
next(even_gen)  # 4
next(even_gen)  # 6
next(even_gen)  # 8
next(even_gen)  # Iterator Error is given

# Looping over generators
def evens(start, end):
    num = start + (start % 2)
    while num < end:
        yield num
        num += 2
for num in evens (12, 60):
    print(num)
# Looks a lot like:
evens = [num for num in range(12, 60) if num % 2 == 0]
for num in evens:
    print(num)

# Generators are lazy, they only generate the next item when needed.
# Why generate the whole sequence, if you only want some elements?
"""A large list can cause your program to run out of memory.
A generator can be a lot more efficient."""

# A "yield from" statement can be used to yield the values from an iterable one at a time:
def a_then_b(a, b):
    yield from a
    yield from b
list(a_then_b(range(10), range(10, 20))

# A "yield from" can also yield the results of another generator function (which could be itself)

# When a generator function executes a return statement, it exits and cannot yield more values.
def g(x):
    yield x
    yield x + 1
    return x + 2
    yield x + 3     # does not work, code will not be read past "return" on a generator.








