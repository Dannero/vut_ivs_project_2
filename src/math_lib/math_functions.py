from math import log

def plus(a: float, b: float) -> float:
    return(a + b)

def minus(a: float, b: float) -> float:
    return(a - b)

def multiply(a: float, b: float) -> float:
    return(a * b)

def divide(a: float, b: float) -> float:
    if b == 0:
        raise Exception("Undefined operation: Division by zero")
    return round((a / b),10)

def factorial(a: int):
    if a < 0:
        raise Exception("Factorial is undefined for negative and floating numbers") 
    res = 1
    for i in range(1,a+1):
        res = res*i
    return res

def power(a: float, exponent):
    if isinstance(exponent,float):
        raise Exception("Only natural number exponents are allowed")
    if exponent < 0:
        raise Exception("Only natural number exponents are allowed") 
    return(a**exponent)

def root(a: float, root: int) -> float:
    return round((a**(1/root)),10)

def naturallog(a: float) -> float:
    return round(log(a),10)