package main

import "fmt"

func main() {
	var num1 int = 10

	// if-else statement
	fmt.Println("if-else statement")
	if num1 > 0 {
		fmt.Println("num1 is positive")
	} else if num1 < 0 {
		fmt.Println("num1 is negative")
	} else {
		fmt.Println("num1 is zero")
	}

	// switch statement
	fmt.Println("switch statement")
	switch num1 {
	case 1:
		fmt.Println("num1 is one")
	case 2:
		fmt.Println("num1 is two")
	default:
		fmt.Println("num1 is neither one nor two")
	}

	// for loop with range
	fmt.Println("for loop with range")
	for i := range 10 {
		if i%2 == 0 {
			fmt.Println(i)
		}
	}

	// for loop with condition
	fmt.Println("for loop with condition")
	for num1 > 1 {
		num1--
		fmt.Println(num1)
	}

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
	fmt.Println("for loop with break")
	for i := range 10 {
		if i == 5 {
			break
		}
		fmt.Println(i)
	}

	// for with continue
	fmt.Println("for loop with continue")
	for i := range 10 {
		if i%2 == 0 {
			continue
		}
		fmt.Println(i)
	}

	// switch statement with fallthrough: fallthrough is rarely used in Go
	fmt.Println("switch statement with fallthrough")
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
	fmt.Println("switch statement with goto")
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
	fmt.Println("if with goto")
	for i := range 10 {
		if i == 5 {
			goto end
		}
		fmt.Println(i)
	}

end:
	fmt.Println("end of switch statement")

	fmt.Println("outerloop:")
outerloop:
	for i := range 5 {
		for j := range 5 {
			if i == 3 {
				break outerloop
			}
			fmt.Print("matriks [", i, "][", j, "]", "\n")
		}
	}

	/* forever loop
	fmt.Println("forever loop")
	for {
		do stuff here
	}
	*/
}
