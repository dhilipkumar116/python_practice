'''
Function composition is the way of combining two or more functions in such
a way that the output of one function becomes the input of the second function and so on.
For example, let there be two functions “F” and “G” and their composition can be
represented as F(G(x)) where “x” is the argument and output of G(x) function will
become the input of F() function.
'''


def add(x):
    return 2+x
def multiply(x):
    return 2*x
print(multiply(add(5)))

# ------------------------------

def composition_func(f, g):
    return lambda x: f(g(x))

add_multiply = composition_func(add,multiply)
print(add_multiply(5))

