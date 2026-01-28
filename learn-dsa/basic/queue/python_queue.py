# Basic Queue
# Queue is a linear data structure that follows the First In First Out (FIFO) principle.
# The operations are:
# - enqueue: Add an element to the end of the queue.
# - dequeue: Remove the element from the front of the queue.
# - is_empty: Check if the queue is empty.
# - peak: Get the element at the front of the queue without removing it.
# - size: Get the number of elements in the queue.

# Big O Notation:
# - enqueue: O(1)
# - dequeue: O(n)
# - is_empty: O(1)
# - peak: O(1)
# - size: O(1)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

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