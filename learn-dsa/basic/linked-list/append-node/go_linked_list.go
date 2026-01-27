// Singly Linked List

package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

type LinkedList struct {
	head *Node
}

func NewLinkedList() *LinkedList {
	return &LinkedList{}
}

func (lln *LinkedList) Append(newValue int) {
	newNode := &Node{
		value: newValue,
		next:  nil,
	}

	if lln.head == nil {
		lln.head = newNode
		return
	}

	current := lln.head
	// Traverse to the end of the list
	for current.next != nil {
		current = current.next
	}

	current.next = newNode
}

func (lln *LinkedList) Display() {
	temp := lln.head
	for temp != nil {
		fmt.Println(temp.value)
		temp = temp.next
	}
	// To ensure the end of the list is marked by a newline
	fmt.Println()
}

func main() {
	lln := NewLinkedList()
	lln.Append(1)
	lln.Append(2)
	lln.Append(3)
	lln.Display()
}
