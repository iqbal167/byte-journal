package main

import "fmt"

func main() {
	var num1 int = 10

	// if-else statement
	if num1 > 0 {
		fmt.Println("num1 is positive")
	} else if num1 < 0 {
		fmt.Println("num1 is negative")
	} else {
		fmt.Println("num1 is zero")
	}

	// switch statement
	switch num1 {
	case 1:
		fmt.Println("num1 is one")
	case 2:
		fmt.Println("num1 is two")
	default:
		fmt.Println("num1 is neither one nor two")
	}

	for i := range 10 {
		if i%2 == 0 {
			fmt.Println(i)
		}
	}

	// for with struct
	fmt.Println("MyStruct")
	type MyStruct struct {
		Field1 *MyStruct
	}

	myStruct := &MyStruct{
		Field1: nil,
	}

	for myStruct.Field1 != nil {
		fmt.Println("My Field")
		fmt.Println(myStruct.Field1)
	}

	// for with braak
	for i := range 10 {
		if i == 5 {
			break
		}
		fmt.Println(i)
	}

	// for with continue
	for i := range 10 {
		if i%2 == 0 {
			continue
		}
		fmt.Println(i)
	}

	// switch statement with fallthrough: fallthrough is rarely used in Go
	switch num1 {
	case 1:
		fmt.Println("num1 is one")
		// fallthrough to the next case
		fallthrough
	case 2:
		fmt.Println("num1 is two")
	default:
		fmt.Println("num1 is neither one nor two")
	}

	// switch with goto: goto is rarely used in Go
	switch num1 {
	case 1:
		fmt.Println("num1 is one")
		goto end
	case 2:
		fmt.Println("num1 is two")
	default:
		fmt.Println("num1 is neither one nor two")
	}

	// if with goto
	for i := range 10 {
		if i == 5 {
			goto end
		}
		fmt.Println(i)
	}

end:
	fmt.Println("end of switch statement")
}
