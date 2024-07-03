def digit_counter(func, num):
    """Return the number of digits when func(num) is true"""
    counter = 0

    while num > 0:
        if func(num):
            counter += 1
            num = num // 10
            print("DEBUG: num = " + str(num))
            print("DEBUG: counter = " + str(counter))
        else:
            num = num // 10

    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


"""ADD_TESTING_CODE"""
print(digit_counter(is_even, 10))
print(digit_counter(is_even, 20))
print(digit_counter(is_even, 112))
print(digit_counter(is_even, 8574))