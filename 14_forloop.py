
for i in range(10):
    print(i, end=" ")
print()

#printing even numbers
for i in range(0,21,2):
    print(i, end=" ")
print()

# nested for
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
print("--------------------")
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print("--------------------")
for i in range(26):
    print(chr(65+i),end="")
print()
for i in range(26):
    print(chr(97+i),end="")

print()
print("--------------------")


for i in range(5):
    for j in range(5):
        print(chr(65+j),end="")
    print()