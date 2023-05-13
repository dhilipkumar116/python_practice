'''

Identity operators are used to compare the objects,
not if they are equal, but if they are actually the same object,
with the same memory location:

is
is not

'''

d = 3
e = 3
print(id(d),id(e))

f = []
g = []
print(id(f),id(g))

a = [1,2]
b = [1,2]
c = a
print(id(a))
print(id(b))
print(id(c))

print(a is c)
print(a == b)

print(a is not c) # opposite to "is"