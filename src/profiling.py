##
# @file profiling.py
#
# @brief Standard Deviation Calculator

from math_lib import math_functions

int_lst = list(map(float, input().split()))

##
# @brief Mean Evaluation
#
# Calculates the mean value (sum of input values divided by the count of the input values)
mean = float(0)
for i in range(len(int_lst)):
    mean = math_functions.plus(mean, int_lst[i])   
mean = math_functions.divide(mean, len(int_lst)) 

##
# @bried Sample evaluation
#
# Calculates the sample value( sqrt( (1/n-1)*(sum(val^2) - n*mean^2 ) ) )
sample = float(0)
for i in range(len(int_lst)):
    sample = math_functions.plus(sample, math_functions.power(int_lst[i],2))
sample = math_functions.minus(sample, math_functions.multiply(len(int_lst), math_functions.power(mean, 2)))
sample = math_functions.root(math_functions.divide(sample, math_functions.minus(len(int_lst), 1)), 2)

print(round(sample,10))