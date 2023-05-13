
def welcome():
    print("welcome")

welcome()

def welcome_1():
    return "welcome!!!"

print(welcome_1())

'''
types of functions:
# no return type without argument 
# no return with argument   
# return type without argument
# return type with argument
# arbitary argument function
# keyword argument function
'''


# arbitary argument function(*)
# we can pass n number of arguments, in
# this arguments is passed in form of list to the function
def friend(*frd):
    print(frd)
friend("ram","krish","dhilip")


#keyword argument function
def message(name,age):
    print(name,"age is",age)

message(22,"ram") # argument is changing
# ,in order to restict that
message(age=23, name="ram")



#arbitrary keyword argument functions -  it gives keyvalue pair
def personalDetails(**kwargs):
    print(kwargs)
personalDetails(name="dhilip",age=22,color="white")

#default parameter function
def user(name, city="chennai"):
    print(name,"is from",city)

user("dhilip","chengalpat")
user("dhilip")


#passing list as an argument in function
def average(marks):
    print("average:",sum(marks)/len(marks))
average([76,34,67,93,89])


#recursive func
# eg: factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print("factorial:",fact(5))

#lambda function
#it is a anonymous function
c = lambda a : a+100
print("lambda:", c(2))

c = lambda a, b: a*b
print("lambda:", c(2, 3))

