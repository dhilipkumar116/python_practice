import threading

x = 0
def increment():
    global x
    x += 1
    print(x)

def thread_task(lock):
    for _ in range(100):
        lock.acquire()
        increment()
        lock.release()

def main_task():

    # to avoid race condition we need to add lock
    lock = threading.Lock()
    x = threading.Thread(target=thread_task, args=(lock,))
    y = threading.Thread(target=thread_task, args=(lock,))
    x.start()
    y.start()

    x.join()
    y.join()
    print('done')
main_task()
