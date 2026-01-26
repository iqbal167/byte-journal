package main

import "fmt"

func main() {
	// use PascalCase for exported constants
	const HTTPTimeout = 30

	// use cameCase for unexported constants
	const httpTimeout = 30

	// multi-constant declaration
	const num1, num2 = 1, 2

	fmt.Println(HTTPTimeout, httpTimeout, num1, num2)

	// use const block for multiple constants
	const (
		MaxBufferSize  = 1024
		MaxConcurrency = 100
	)

	fmt.Println(MaxBufferSize, MaxConcurrency)

	// use const block for constants of same kind
	const (
		// manifest typing
		Error      string = "General Error"
		GeneralErr        // same as Error
		// inference typing
		Success = "Success"
	)

	fmt.Println(Error, GeneralErr, Success)

}
