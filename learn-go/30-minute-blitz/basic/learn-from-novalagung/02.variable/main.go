package main

import "fmt"

func main() {
	// Declare multi variable with manifest typing
	var name string = "Muhammad Iqbal Ali"

	// Declare multi variable with type inference
	nickName := "Iqbal"
	nickName = "Zkh"

	// Print multi variable
	fmt.Printf("My name is %s, my nickname is %s\n", name, nickName)

	// Declare multi variable with manifest typing
	var one, two, three int = 1, 2, 3
	// Declare multi variable with type inference
	four, isOk, word := 4, true, "Go"
	// Print multi variable
	fmt.Printf("one: %d, two: %d, three: %d, four: %d, isOk: %t, word: %s\n", one, two, three, four, isOk, word)

	// _ (Underscore) variable -> Reserved variable for ignoring value
	_ = "Golang"
	tag, _ := "Go", 2023
	// Print tag
	fmt.Println(tag)

	// Declare pointer variable with `new` keyword
	myString := new(string)
	// Dereference pointer variable with `*` operator
	fmt.Println(*myString)
	// Print pointer address
	fmt.Println(myString)

	// Declare variable with `make` keyword
	mySlice := make([]int, 5)
	// Print slice
	fmt.Println(mySlice)

	myMap := make(map[string]string)
	// Print map
	fmt.Println(myMap)

	myChan := make(chan int)
	// Print channel address
	fmt.Println(myChan)
}
