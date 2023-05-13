try:

    # writing existing file
    file = open("text.txt","w") # "a" - for append
    file.write("this is dhilip kumar!")
    file.close()


    file = open("text.txt","r")
    # print(file.readline())
    # print(file.readline(3))
    # print(file.readlines())
    for line in file:
        print(line)

except FileNotFoundError:
    print("exception:file not found")
else:
    file.close()