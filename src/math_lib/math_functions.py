##
# @file math_functions.py
# @brief Library of math functions for our calculator
#
# This library contains all arithmetic functions necessary for our calculator.
from math import log

##
# @brief Addition
# @param a First number for addition
# @param b Second number for addition
# @return Sum of a and b
def plus(a: float, b: float) -> float:
    return(a + b)

##
# @brief Subtraction
# @param a Number to subtract from
# @param b Number to subtract
# @return Difference of b from a
def minus(a: float, b: float) -> float:
    return(a - b)

##
# @brief Multiplication
# @param a First number for multiplication
# @param b Second number for multiplication
# @return Product of a and b
def multiply(a: float, b: float) -> float:
    return(a * b)

##
# @brief Division
# @param a Number to divide (dividend)
# @param b Number to divide by (divisor)
# @return Fraction of a over b
def divide(a: float, b: float) -> float:
    if b == 0:
        raise Exception("Undefined operation: Division by zero")
    return round((a / b),10)

##
# @brief Factorial
# @param a Number for factorial
# @return Factorial of a
def factorial(a: int):
    if a < 0:
        raise Exception("Factorial is undefined for negative numbers")
    else:
        res = 1
        for i in range(1,a+1):
            res = res*i
        return res

##
# @brief Exponentation
# @param a Base to raise
# @param b Exponent for base to raise to
# @return Power of a raised to b
def power(a: float, exponent):
    if isinstance(exponent,float):
        raise Exception("Only natural number exponents are allowed")
    if exponent < 0:
        raise Exception("Only natural number exponents are allowed") 
    return(a**exponent)

##
# @brief Root
# @param a Number to find root of
# @param b Number specifying n-th root
# @return b-th root of a
def root(a: float, root: int) -> float:
    return round((a**(1/root)),10)

##
# @brief Natural logarithm
# @param a Number for logarithm
# @return Natural logarithm of a
def naturallog(a: float) -> float:
    return round(log(a),10)