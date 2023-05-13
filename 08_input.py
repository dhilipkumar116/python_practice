"""
name = input("enter input : ")
print(name)
print(type(name))
"""


# input is a string type
"""
#getting int value
a =  int(input("enter value of A: "))
b =  int(input("enter value of B: "))
c =  a+b;
print(c)
print(type(c))
"""

"""
#getting int value
a =  float(input("enter value of A: "))
b =  float(input("enter value of B: "))
c =  a+b;
print(c)
print(type(c))
"""

"""
#multiple input in single line
name1,name2,name3 = input("enter 3 name : ").split() # or split(',')
print("name1 : ",name1);
print("name2 : ",name2);
print("name3 : ",name3);
"""

"""
#list input
number = [12,3,54,23]
print(type(number))
print(number)
"""


#getting multiple line as a input

paragraph = []
print("enter a paragraph : ")
while True:
    line = input()
    if line: 
        paragraph.append(line)
    else:
        break
print(paragraph)
print('\n'.join(paragraph))




























