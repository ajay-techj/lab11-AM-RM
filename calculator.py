# https://github.com/ajay-techj/lab11-AM-RM.git
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

def logarithm(a, b): #loga(b)# use math library/raise ValueError
    try:
        return math.log(b, a)
    except:
        raise ValueError

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a ** b