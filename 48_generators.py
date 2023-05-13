'''
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

2. Memory Efficient
A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill, if the number of items in the sequence is very large.

Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.
'''

def my_generator(n):
    val = 0
    while val < n:
        yield val
        val += 1
for i in my_generator(4):
    print(i)