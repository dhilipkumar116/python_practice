try:
    file = open("text.txt",'r')
    print(file.read())
except FileNotFoundError:
    print("exception: file not found")
else:
    file.close()