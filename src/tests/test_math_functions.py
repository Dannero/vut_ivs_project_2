from math_lib import math_functions

def test_plus():
    assert math_functions.plus(10, 20) == 30
    assert math_functions.plus(-10, 20) == 10
    assert math_functions.plus(-10, -20) == -30
    assert math_functions.plus(10.3, 20.3) == 30.6

def test_minus():
    assert math_functions.minus(10, 20) == -10
    assert math_functions.minus(-10, 20) == -30
    assert math_functions.minus(-10, -20) == 10
    assert math_functions.minus(10.3, 20.3) == -10

def test_multiply():
    assert math_functions.multiply(10, 20) == 200
    assert math_functions.multiply(-10, 20) == -200
    assert math_functions.multiply(-10, -20) == 200
    assert math_functions.multiply(0.5, 0.5) == 0.25

def test_divide():
    assert math_functions.divide(10, 20) == 0.5
    assert math_functions.divide(-10, 20) == -0.5
    assert math_functions.divide(-10, -20) == 0.5
    assert math_functions.divide(0.5, 0.5) == 1

# def test_factorial():
#     assert math_functions.factorial(5) == 120
#     assert math_functions.factorial(-5) == -120
#     assert math_functions.factorial(10) == 3628800

# def test_power():
#     assert math_functions.power(5, 2) == 25
#     assert math_functions.power(-5, 2) == 25
#     assert math_functions.power(10, 2) == 100
#     assert math_functions.power(10 , 3) == 10000
#     assert math_functions.power(2, 3) == 8
#     assert math_functions.power(2.5, 3) == 15.625
#     assert math_functions.power(-2, 3) == -8

# def test_square():
#     assert math_functions.square(25, 2) == 5
#     assert math_functions.square(49, 2) == 7
#     assert math_functions.square(27, 3) == 3

