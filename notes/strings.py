# String literals: 3 Forms

# 'Hello World!' == "Hello World!"

# Multi-line strings automatically insert new lines:
"""The Zen of Python
claims, Readability counts.
Read more: import this."""

# Strings are similar to lists
alphabet = 'abcde'
len(alphabet)   # == 5

initial = 'P'
initial[0] == initial       # True

 # 'in' operator matches substrings
 'W' in 'Where\'s Waldo'       # True

 # Split function:
 s = "This is a short sentence."
 words = s.split()  # ['This', 'is', 'a', 'short', 'sentence.']

 # Specify the character to spit on as an argument
 halfway = s.split(a)

 # Change the entire string to upercase or lowercases
 someString = "Title Case"
 someString.upper()
 someString.lower()

 # String interpolation combines string literals with the results of expressions
 # Put an 'f' in front of the quotes and then put any valid Python expression in curly brackets inside
 place = 10
 print(f"Landing at {place}")
 # Any valid python expression can go inside the parentheses
 greeting = 'Ahoy'
 noun = 'Jackson'
 print(f"{greeting.lower()}, {noun.upper()}!")

 # Slicing a list or string creates a new list with subsequence of the original lits
 letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        #    0    1    2    3    4    5    6    7    8    9
sublist1 = letters[1:]      # List includes all indexes of original list
sublist2 = letters[1:4]    # List includes indexes 1-3: ['a', 'b', 'c']

compound_word = "cortaunas"
word1 = compound_word[:5]   # "corta"
word2 = compound_word[5:]   # "unas"

# Copying a whole list via slicing - the two lists are independent and not linked
letters = letters1[:]
letters[0] = 0  #[0, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
letters[1] = 1  #['a', 1, 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# A range represents a sequence of integers - NOT A LIST
print(range(-2, 3))       # == -2, -1, 0, 1, 2
# if only one argument is included, it starts at 0
print(range(3))           # == 0, 1, 2
# range(<start>, <end>, <step>)
# <step> == interval









