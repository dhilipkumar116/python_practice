'''
it is immutable
sorrounded by a round brackets
'''

a = (3.4,1,"ram",False)
print(a)
print(type(a))
print(a[0])
print(a[2])
print(a[-1])
print(a[0:2])

# to add values to tuples
b = list(a)
b.append("sam")
a = tuple(b)
print(a)

if "ram" in a:
    print("found")
else:
    print("not found")

# single element in tuple

b = (1,) # comma is necessary if tuple as single element
print(b)
del b # deletes tuple, we cannot use them in future

print("merge tuple")
a = (1,2,3,4)
b = (4,5,6,7)
c = a+b
print(c)
print(c.count(4))

# nested tuples
print("nested tuple")
c = (a,b)
print(c)
print(c[0])
print(c[1])
print(c[1][0])

x = ('dhilip',)*4
print(x)

temp = tuple('dhilip')
print(temp)