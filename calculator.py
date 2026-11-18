import math
def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b


def logarithm(a, b): #loga(b)# use math library/raise ValueError
    try:
        return math.log(a, b)
    except:
        raise ValueError

def exponent(a, b): 
    return a**b



def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    try:
        return math.log(b, a)
    except:
        raise ValueError

def exp(a, b):
    return a ** b