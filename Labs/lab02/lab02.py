
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    factorial = 1
    if k > 0:
        while k > 0 and n > 1:
            factorial = factorial * n
            k -= 1
            n -= 1
        return factorial
    elif k == 0:
        return 1



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    length = len(str(y))
    sum = 0
    while length > 0:
        digit = str(y)[length - 1]
        sum += int(digit)
        length -= 1
    return sum





###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    a = 0
    b = 1
    string = str(n)
    counter = len(string) - 1
    while counter > 0:
        if string[a] == string[b] and string[a] == "8":
            counter = 0
            return True
        else:
            counter -= 1
            a += 1
            b += 1
    return False

