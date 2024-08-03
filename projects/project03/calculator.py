from pair import *
from operator import add, sub, mul, truediv

def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    # Write your code here
    token_list_rd = expression.split()
    token_list = []

    def is_num(character):  # Function takes a string of length 1 and checks to see if it could be part of a num
        assert len(character) == 1
        if character.isdigit():
            return True
        elif character == '.':
            return True
        else:
            return False

    def is_string_num(number):
        for character in number:
            if is_num(character):
                pass
            else:
                return False
        return True

    def find_num(string):   # Takes a string and returns a list that splits numbers from other characters
        string_list = []

        for i in string:
            if not is_num(i):   # Adds character if it is not a digit related character
                string_list.append(i)
            elif is_num(i) and len(string_list) == 0:
                string_list.append(i)
            elif is_num(i) and not is_num(string[string.index(i)-1]):
                string_list.append(i)
            else:   # If both the character and its previous character are digits, add together into 1 string
                string_list[-1] = string_list[-1] + i
        return string_list

    for token in token_list_rd:
        if len(token) == 1:
            token_list.append(token)
        elif is_string_num(token):
            token_list.append(token)
        else:
            temp_list = find_num(token)
            for element in temp_list:
                token_list.append(element)
    return token_list


# OPTIONAL
def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    # Write your code here
    token = tokens[index]
    if tokens[index] == '(':
        operator = tokens[index + 1]
        if index != 0:
            temp_return = parse_tokens(tokens, index + 2)
            index = temp_return[1]
            operator = Pair(operator, temp_return[0])
        elif index == 0:
            index += 2
        temp_return = parse_tokens(tokens, index)
        index = temp_return[1]
        return Pair(operator, temp_return[0]), index
    elif tokens[index] == ')':
        index += 1
        return nil, index
    else:
        try:
            if token.isdigit():
                converted_token = int(token)
            else:
                converted_token = float(token)
            temp_return = parse_tokens(tokens, index + 1)
            index = temp_return[1]
            temp_pair = temp_return[0]
            return Pair(converted_token, temp_pair), index
        except ValueError:
            raise TypeError("The function attempted to convert a string that was not a number.")


def parse(tokens):
    lst = parse_tokens(tokens, 0)
    return lst[0]


def reduce(func, operands, initial):
    num1 = initial
    num2 = operands.first
    next_num = operands.rest
    while next_num != nil:  # Ends loop 1 short
        num1 = func(num1, num2)
        num2 = next_num.first
        next_num = next_num.rest
    num1 = func(num1, num2)  # Evaluates the function of the value so far with last number
    return num1


def apply(operator, operands):
    if operator == '+':
        return reduce(add, operands, 0)
    elif operator == '*':
        return reduce(mul, operands, 1)
    elif operator == '-':
        initial = operands.first
        return reduce(sub, operands.rest, initial)
    elif operator == '/':
        initial = operands.first
        return reduce(truediv, operands.rest, initial)
    else:
        raise TypeError("Operator invalid: operator must be +, -, *, or /")


def eval(syntax_tree):
    if isinstance(syntax_tree, int) or isinstance(syntax_tree, float):
        return syntax_tree
    elif isinstance(syntax_tree, Pair):
        operator = syntax_tree.first
        current = syntax_tree.rest
        while current != nil:
            current.first = eval(current.first)
            current = current.rest
        num = apply(operator, syntax_tree.rest)
        return num
    else:
        raise TypeError("Input must be a primitive or a Pair object.")


# Interactive Session goes here
print('Welcome to the CS 111 Calculator Interpreter.')
# nsert main loop here
expression = input('calc >> ')
while expression != 'exit':
    exp_tokens = tokenize(expression)
    try:
        exp_parsed = parse(exp_tokens)
        value = eval(exp_parsed)
        print(value)
    except TypeError:
        print('TypeError: The expression is not valid.')

    expression = input('calc >> ')

print("Goodbye!")

if __name__ == "__main__":
    pass
