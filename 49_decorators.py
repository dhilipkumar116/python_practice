def smart_div(func):
    def inner(a,b):
        print("i am going to divide ",a ," and ",b)
        if b == 0:
            print("cannot divide by 0")
            return
        else:
            func(a,b)
    return inner

@smart_div
def divide(a,b):
    return a/b

# decorated_func = smart_div(divide)
# decorated_func(2,0)

divide(2,0)

# --------------------------------------

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
