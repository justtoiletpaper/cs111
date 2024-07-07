#In Cs, we often "abstract away the details."


"""Abstraction by Parameterization"""
interest = 1 + 0.6 * 2
interest 2 = 1 + 0.9 * 4
# Let's make a parameter:
def interest(rate, years):
    return 1 + rate * years

