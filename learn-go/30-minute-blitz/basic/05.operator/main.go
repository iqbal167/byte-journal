package main

import (
	"fmt"
)

func main() {
	num1 := 10
	num2 := 5

	// Arithmetic Operators
	fmt.Println(num1 + num2)
	fmt.Println(num1 - num2)
	fmt.Println((num1 * num2))
	fmt.Println(num1 / num2)
	fmt.Println(num1 % num2)

	// Comparison Operators
	fmt.Println(num1 == num2)
	fmt.Println(num1 != num2)
	fmt.Println(num1 > num2)
	fmt.Println(num1 < num2)
	fmt.Println(num1 >= num2)
	fmt.Println(num1 <= num2)

	// Assignment Operators
	num1 += 5
	fmt.Println(num1)
	num1 -= 5
	fmt.Println(num1)
	num1 *= 5
	fmt.Println(num1)
	num1 /= 5
	fmt.Println(num1)
	num1 %= 5
	fmt.Println(num1)

	// Logical Operators
	isTrue := true
	isFalse := false
	fmt.Println(isTrue && isFalse)
	fmt.Println(isTrue || isFalse)
	fmt.Println(!isTrue) // read as not isTrue

	/*
		Bitwise Operators
		 Bitwise Operators is used to perform bitwise operations on integer values
		 Bitwise Operators used when working with binary numbers, e.g. 1010 & 1100 = 1000, and with decimal numbers, e.g. 10 & 5 = 0
		 In real-world case, we use bitwise operators to manipulate binary data, e.g. to check if a number is even or odd
		 To check if a number is even, we use bitwise AND operator with 1, e.g. 1010 & 0001 = 0000, and if the result is 0, then the number is even
		 To check if a number is odd, we use bitwise AND operator with 1, e.g. 1010 & 0001 = 0001, and if the result is 1, then the number is odd
	*/
	num3 := 5
	num4 := 6
	
	fmt.Println(num3 & num4) // 4 (1010 & 1100 = 1000)
	fmt.Println(num3 | num4) // 7 (1010 | 1100 = 1111)
	fmt.Println(num3 ^ num4) // 3 (1010 ^ 1100 = 0110)
	fmt.Println(num3 << 1)   // 10 (1010 << 1 = 10100)
	fmt.Println(num3 >> 1)   // 2 (1010 >> 1 = 0101)
}
