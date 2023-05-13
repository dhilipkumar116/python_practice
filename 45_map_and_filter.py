def myfunc(a,b):
    return a+b

x = map(myfunc, (1,2,3),(1,2,3))
x = map(myfunc, [1,2,3],[1,2,3])

print(list(x))
print(type(x))


# filter  - return even numbers
def my_func(a):
    if a % 2 == 0:
        return True
    else:
        return False
lst = [1,2,3,4,5,6,7,8,9,10]
x = filter(my_func, lst)
print(list(x))
print(type(x))