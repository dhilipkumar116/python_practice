'''

The reduce(fun,seq) function is used to apply a
particular function passed in its argument to all
of the list elements mentioned in the sequence
passed along.This function is defined in “functools” module.

'''

import functools
import itertools


lst = [1,2,3,4,5]
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a,b : a+b, lst))

# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lst, lambda x, y: x + y)))

'''
Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.  

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a iterator containing the intermediate results. The last number of the iterator returned is summation value of the list.
reduce(fun, seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.

'''