# Tuples
empty = ()
# or
# empty = tuple()

# Make a tuple from an iterable (modifiable) sequence
digit_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_tuple = tuple(digit_list)

# Many of a list's read only operations work on tuples
    # Combining tuples:
("come", "rain") + ("or", "shine")
    # Checking containment
"wally" in ("wally", "wall-e", "wallace", "waldo")
    # Acessing elements
conditions = ("rain", "shine")
conditions[1] # "shine"
    # Slicing
numbers = digit_tuple[:2]   # (1, 2, 3)


### Dictionaries ###
states = {
    "CA": "California",
    "AZ": "Arizona",
    "UT": "Utah",
    "ID": "Idaho"
}
# Select a value
states["AZ"]    # "Arizona"

best_state = "AZ"
states[best_state]  # "Arizona"

"""
a KEY cannot be a list or a dictionary (or any mutable type)
The VALUES, however, can be any type
"""
random = {
    "colors": ["Blue", "Green", "Orange"],
    "length": (5, 7),
    "color meaning": {"red": "angry", "blue": "sad"}
}

# Keys are iterated over in the order they are first added
insects = {"spiders": 8, "centipedes": 100, "bees": 6}
for name in insects:
    print(insects[name])        # 8 100 6

# Dictionary Comprehensions
# {key: value for <name> in <iter exp>}
{x: x*x for x in range(3, 6)}   # {3: 9, 4: 16, 5: 25}

# Going through each key in a dictionary
for somekey in insects:
    <SOMECODE>

# Checking for a code:
my_dictionary = {1: 1, 2: 4, 3: 9}
key = "a"
if key in my_dictionary:
    value = my_dictionary[key]
else:
    value = 0
