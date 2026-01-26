package main

import "fmt"

func main() {
	// Fixed-size array
	arr := [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr)

	// Slice (dynamic array)
	arr2 := []int{1, 2, 3, 4, 5}
	fmt.Println(arr2)
}
