# Singly Linked List

class Node:
    def __init__(self, value):
        # Assign value to the node
        self.value = value
        # Initialize next as null
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize head as null
        self.head = None

    def append(self, new_value):
        # Create a new node with the given value
        new_node = Node(new_value)

        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        # Traverse to the end of the list
        while current.next:
            current = current.next

        current.next = new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        # To ensure the end of the list is marked by a newline
        print()


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.display()
