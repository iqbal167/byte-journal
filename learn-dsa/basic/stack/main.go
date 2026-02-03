package main

import "fmt"

type Stack struct {
	items []int
}

func NewStack() *Stack {
	return &Stack{}
}

func (s *Stack) IsEmpty() bool {
	return len(s.items) == 0
}

func (s *Stack) Push(item int) {
	s.items = append(s.items, item)
}

func (s *Stack) Pop() int {
	if s.IsEmpty() {
		return -1
	}
	item := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return item
}

func (s *Stack) Peak() int {
	if s.IsEmpty() {
		return -1
	}
	return s.items[len(s.items)-1]
}

func (s *Stack) Size() int {
	return len(s.items)
}

func (s *Stack) Clear() {
	s.items = []int{}
}

func (s *Stack) GetItems() []int {
	return s.items
}

func main() {

	stack := NewStack()
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)

	fmt.Println("Peak:", stack.Peak())
	fmt.Println("Get Items:", stack.GetItems())
	stack.Pop()
	fmt.Println("Get Items:", stack.GetItems())

	fmt.Println("Size:", stack.Size())
}
