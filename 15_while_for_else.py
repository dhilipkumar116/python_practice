
# while else
# else will be executed after completion of while loop
# if while is not completed else will also not executed

i=1
while i<=5:
    #if i==3:
    #    break
    print(i,end=" ")
    i+=1
else:
    print("")
    print("while loop competed successfully")

print("-----------------------------------------")

for i in range(5):
    print(i,end=" ")
else:
    print("")
    print("for loop completed successfully")