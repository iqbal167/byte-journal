package main

import "fmt"

func main() {
	// Array
	// Array is a fixed-size collection of elements of the same type
	fmt.Println("Array")
	var arr1 [5]int = [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr1)
	// Array Length
	fmt.Println(len(arr1))

	// Array Element
	fmt.Println(arr1[2])

	// Array from Slice
	fmt.Println("Array from Slice")
	var num1 = [...]int{1, 2, 3, 4, 5}
	// Array Element with for loop
	for i := range num1 {
		fmt.Println(num1[i])
	}

	fmt.Println("Array Element with for loop")
	for _, num := range num1 {
		fmt.Println(num)
	}

	// Array from Matrix
	fmt.Println("Array from Matrix")
	var matrix [2][3]int = [2][3]int{
		{1, 2, 3},
		{4, 5, 6},
	}
	fmt.Println(matrix)

	// Slice
	// Slice is a reference to an array
	fmt.Println("Slice")
	var slice1 []int = []int{1, 2, 3, 4, 5}
	fmt.Println(slice1)
	// Slice Length
	fmt.Println(len(slice1))

	// Slice Element
	fmt.Println(slice1[2])

	// Slice from Array
	var slice2 []int = arr1[1:3]
	fmt.Println(slice2)
	// Slice from Array Length
	fmt.Println(len(slice2))
	// Slice from Array Element
	fmt.Println(slice2[0])

	// initialize slice with make
	// make function creates a slice of a given length and optional capacity
	var arr2 = make([]int, 5)
	fmt.Println(arr2)

	// Slicing operation
	// Slicing operation creates a new slice from an existing slice
	// The new slice is a reference to the same array as the existing slice
	// The new slice has a new length and capacity
	var sliceRef []int = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	var slice3 []int = sliceRef[0:0] // []
	fmt.Println(slice3)
	var slice4 []int = sliceRef[0:3] // [1, 2, 3]
	fmt.Println(slice4)
	var slice5 []int = sliceRef[3:6] // [4, 5, 6]
	fmt.Println(slice5)
	var slice6 []int = sliceRef[6:] // [7, 8, 9, 10]
	fmt.Println(slice6)
	var slice7 []int = sliceRef[:6] // [1, 2, 3, 4, 5, 6]
	fmt.Println(slice7)
	var slice8 []int = sliceRef[:] // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	fmt.Println(slice8)
	var slice9 []int = sliceRef[10:10] // [] -> because the start index is greater than the end index
	fmt.Println(slice9)
	// var slice10 []int = sliceRef[10:9] -> error: slice bounds out of range

}
