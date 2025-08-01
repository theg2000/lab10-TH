#https://github.com/theg2000/lab10-TH
#Partner 1: Trevor Hegarty

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)
    
def exp(a, b):
    return a ** b



