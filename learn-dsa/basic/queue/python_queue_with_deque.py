# Queue with Deque

# Big O Notation:
# - enqueue: O(1)
# - dequeue: O(1)
# - is_empty: O(1)
# - peak: O(1)
# - size: O(1)

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def peak(self):
        if self.is_empty():
            return None
        return self.items[0]

    def display(self):
        print(self.items)

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(1)   
q.enqueue(2)   
q.enqueue(3)
q.display()
print("Peak before dequeue:",q.peak())
print("Size before dequeue:",q.size())
q.dequeue()
q.display()
print("Peak after dequeue:",q.peak())
print("Size after dequeue:",q.size())