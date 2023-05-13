import threading
import time

def count(n):
    for i in range(1,n+1):
        print(i, end='\n')
        time.sleep(0.2)

def count2(n):
    for i in range(1,n+1):
        print(i, end='\n')
        time.sleep(0.2)

x = threading.Thread(target=count, args=(5,))
x.start()

y = threading.Thread(target=count2, args=(5,))
y.start()

# to wait until 1st thread completes its execution, use join
x.join()
y.join()
print('done')