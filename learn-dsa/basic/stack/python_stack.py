# Basic Stack Implementation
# LIFO (Last In First Out)
# Operations: push, pop, peak, size, is_empty, clear

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peak(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def get_items(self):
        return self.items

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Peak:", stack.peak())
print("Get Items",stack.get_items())
stack.pop()
print("Get Items",stack.get_items())

print("Size:", stack.size())
