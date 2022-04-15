from math_lib import math_functions
from math import e
import pytest

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
    assert math_functions.divide(10, 3) == 3.3333333333
    with pytest.raises(Exception):
        math_functions.divide(1,0)

def test_factorial():
    assert math_functions.factorial(0) == 1
    assert math_functions.factorial(1) == 1
    assert math_functions.factorial(2) == 2
    assert math_functions.factorial(5) == 120
    assert math_functions.factorial(10) == 3628800
    assert math_functions.factorial(52) ==  80658175170943878571660636856403766975289505440883277824000000000000
    with pytest.raises(Exception):
        math_functions.factorial(-1)
    with pytest.raises(Exception):
        math_functions.factorial(2.1)

def test_power():
    assert math_functions.power(0, 2) == 0
    assert math_functions.power(1, 0) == 1
    assert math_functions.power(2, 0) == 1
    assert math_functions.power(5, 2) == 25
    assert math_functions.power(-5, 2) == 25
    assert math_functions.power(10, 2) == 100
    assert math_functions.power(10 , 3) == 1000
    assert math_functions.power(2, 3) == 8
    assert math_functions.power(2.5, 3) == 15.625
    assert math_functions.power(-2, 3) == -8
    with pytest.raises(Exception):
        assert math_functions.power(2, 3.14)
    with pytest.raises(Exception):
        assert math_functions.power(2, -1)

def test_root():
    assert math_functions.root(25, 2) == 5
    assert math_functions.root(49, 2) == 7
    assert math_functions.root(27, 3) == 3
    assert math_functions.root(2, 2) == 1.4142135624
    with pytest.raises(Exception):
        math_functions.root(-1,2)
    with pytest.raises(Exception):
        math_functions.root(1,0)
    
def test_ln():
    assert math_functions.naturallog(1) == 0
    assert math_functions.naturallog(e) == 1
    assert math_functions.naturallog(e**2) == 2
    assert math_functions.naturallog(2) == 0.6931471806
    with pytest.raises(Exception):
        math_functions.naturallog(0)
    with pytest.raises(Exception):
        math_functions.naturallog(-1)