try:
    # a = 10/0
    a = 12/2
except Exception as e:
    print(e)
else:
    print("value of a :",a)
finally:
    print('thankyou!')


#types of exception in python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

try:
    print(a)
except NameError as e:
    print(e)

try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)

try:
    print(int("dhilip"))
except ValueError as e:
    print("enter only numbers")
finally:
    print('I will always get execute')

try:
    a = [1,2,3]
    print(a[5])
except IndexError as e:
    print("invalid index")

try:
    f = open("text.txt")
except FileNotFoundError:
    print("file not found error")
else:
    print(f.read())