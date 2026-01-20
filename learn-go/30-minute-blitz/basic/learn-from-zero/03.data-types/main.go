package main

import "fmt"

func main() {
	// numeric non-decimal types
	var num1 uint8 = 255
	var num2 uint16 = 65535
	var num3 uint32 = 4294967295           // 4+ bilion,
	var num4 uint64 = 18446744073709551615 // 18+ bilion
	var uint = 4294967295                  // depending on the value
	var num5 int8 = -128
	var num6 int16 = -32768
	var num7 int32 = -2147483648          // -2+ bilion
	var num8 int64 = -9223372036854775808 // -9+ bilion
	var int = -2147483648                 // depending on the value
	var rune = 'a'                        // equal to int32,  'a' is a unicode code point (e.g. 97 for 'a')

	fmt.Println(num1, num2, num3, num4, uint, num5, num6, num7, num8, int, rune)

	// numeric decimal types
	var num9 float32 = 3.14
	var num10 float64 = 3.141592653589793
	fmt.Println(num9, num10)

	// boolean types
	var isOk bool = true
	fmt.Println(isOk)

	// string types
	var str1 string = "Hello World!"
	fmt.Println(str1)

	// zero value types
	var zeroNum uint8
	var zeroDecimal float64
	var zeroBool bool
	var zeroStr string
	fmt.Println(zeroNum, zeroDecimal, zeroBool, zeroStr)

	// nil zero value
	var pointer *int8
	var slice1 []int8
	var map1 map[string]string
	var channel1 chan int8
	var iface any          // equal to interface{}
	var fn func(int8) int8 // function that takes int8 and returns int8

	fmt.Println(slice1 == nil) // true
	fmt.Println(map1 == nil)   // true
	fmt.Println(fn == nil)     // true

	fmt.Println(pointer, slice1, map1, channel1, iface)
}
