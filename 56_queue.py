queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.pop(0))
print(queue)
# ----------------------------------
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())
print(queue)
# ----------------------------------
from queue import Queue
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())




