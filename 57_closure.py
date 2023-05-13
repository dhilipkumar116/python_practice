#print odd number using closure
def calculate():
    num = -1
    def inner_function():
        nonlocal num
        num = num+2
        return num
    return inner_function


odd = calculate()
print(odd())
print(odd())
print(odd())

# -------------------------------