
def add(num1, num2):        # Function Signature
    return num1 + num2      # Function Body

def addition(x, y):
    sum = x + y             # Assigning variables in the Function body
    return sum

x = 3
add(x * x, x + x)          # Variables (num1, num2) can also instead be expressions

def calculate_dog_age(human_years, multiplier = 7): # Variables & their default value can be assigned in def
    return human_years * multiplier

calculate_dog_age(3)       # Function assumes the default of 7 if not otherwise (== 21)
calculate_dog_age(3, 7) # These two calls are equivalent (== 21)
calculate_dog_age(3, 6) # This call == 18

big_sum = add(200, 412) + add(312, 25)  #Functions can be called to define variables

def divide_exact(n, d):
    quotient = n // d
    remainder = n % d
    return quotient, remainder


q, r = divide_exact(618, 10)       # Two variables can be assigned at once b/c the function returns 2 numbers

def square_it(x):
    x * x           # Number is not returned

square_it(4)        # Function returns "None" - which is NOT a number
print(square_it(4))     # The result printed will be "None"

def passed_class(grade):
    return grade > 65

total = 0
counter = 0
while counter < 5:
    total += pow(2, 1)
    counter += 1

counter = 100
while counter < 200:
    if counter % 7 == 0:
        first_multiple = counter
        break       # Break statement ends the loop
    counter += 1

######### Lists #######################

members = []        # list is empty

members = ["Pamela", "Tinu", "Brenda", "Kaya"]

remixed = ["Pamela", 7, 79.99, 2*2*2]

len()           # Function to find the length of a list

print(len(members)) # == 3

# Each list item has an index, starting from 0
letters = ["A", "B", "C"]
# Index:    0    1    2
letters[0] # "A"

# Negative indices are also possible:
letters[-1]  # "C"
letters[-2]  # "B"
letters[-3]  # "A"

# The addition operator works on lists
boba_prices = [5.50, 6.50, 7.50]
smoothie_prices = [7.00, 7.50]
all_pricess = boba_prices + smoothie_prices  # The lists are combined together

# The multiplier operator repeats the list
more_boba = boba_prices * 2     # [5.50, 6.50, 7.50, 5.50, 6.50, 7.50]

# Appending lists using append()
new_price = 8.50
boba_prices.append(new_price)   # [5.50, 6.50, 7.50, 8.50]

# Inserting using insert()
boba_prices.insert(1, new_price)    # The first number chooses what index the number will have
# == [5.50, 850, 6.50, 7.50]

# nested items
gymnasts = [
    ["Brittany", 9.15, 9.4, 9.3, 9.2],
    ["Lea", 6, 6.5, 3, 4.5]
]

gymnasts[0] [1] # == 9.15

# The "in" operator tests if a value is inside a container
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
10 in digits        # False
1 in digits         # True

counter = 0
pairs = [1, 2], [2, 2], [3, 2], [4, 4]
for x, y in pairs:
    if x == y:
        counter += 1        # Counter will == 2











