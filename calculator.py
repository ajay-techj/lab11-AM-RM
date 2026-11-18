"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def square_root(a):
    if a<0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a, b)
def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a, b): #b / a   # raise ZeroDivisionError if a == 0 
    if a == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a, b): #loga(b)# use math library/raise ValueError
    try:
        return math.log(a, b)
    except:
        raise ValueError

def exponent(a, b): 
    return a**b



