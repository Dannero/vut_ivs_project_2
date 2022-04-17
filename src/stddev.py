# Standard Deviation Calculator
from math_lib import math_functions

int_lst = list(map(int, input().split()))

mean = float(0)
for i in range(len(int_lst)):
    mean = plus(mean, int_lst[i])   
mean = divide(mean, len(int_lst)) 

sample = float(0)
for i in range(len(int_lst)):
    sample = plus(sample, power(minus(int_lst[i], mean), 2))
sample = root(divide(sample, minus(mean, 1)), 2)

print(round(sample,10))
