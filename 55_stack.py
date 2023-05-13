stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
print(stack)
# ---------------------------------
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
print(stack)
# ---------------------------------
from queue import LifoQueue
stack = LifoQueue(maxsize=10)
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.get())
'''
maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue.
'''
# ---------------------------------

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack():
    def __init__(self):
        self.head = Node('head')
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        remove = self.head.next.value
        self.head.next = self.head.next.next
        self.size -= 1
        return remove
    def peek(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.head.next.value
    def __str__(self):
        cur = self.head.next
        out = ''
        while cur:
            out += str(cur.value)+"->"
            cur = cur.next
        return out[:-2]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print('size : ',stack.get_size())
print(stack)

