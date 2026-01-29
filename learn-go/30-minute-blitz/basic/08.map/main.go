package main

import "fmt"

func main() {
	// Initialize a map
	var map1 map[string]string = map[string]string{
		"id":   "1",
		"name": "John Doe",
	}

	fmt.Println(map1)

	// Initialize an empty map
	map3 := map[string]string{}
	map3["id"] = "3"
	fmt.Println(map3)

	// Initilize with make function
	var map2 map[string]string = make(map[string]string)
	fmt.Println(map2)

	// Add a key-value pair
	map2["id"] = "2"
	fmt.Println(map2)

	// Add another key-value pair
	map2["name"] = "Jane Doe"
	fmt.Println(map2)

	// Get a value by key
	fmt.Println(map2["id"])

	// Iterate over key-value pairs
	fmt.Println("Iterate over key-value pairs")
	for key, value := range map2 {
		fmt.Println(key, " \t:", value)
	}

	type User struct {
		ID   string
		Name string
	}

	// Initialize a map with struct
	map4 := map[int]User{
		1: {
			ID:   "1",
			Name: "John Doe",
		},
	}

	fmt.Println(map4)

	// Add another key-value pair
	map4[2] = User{
		ID:   "2",
		Name: "Jane Doe",
	}

	fmt.Println(map4)

	map5 := map[string]int{
		"1": 1,
		"2": 2,
	}

	fmt.Println(map5["3"]) // 0 -> Zero value

	// Check if a key exists
	if v, ok := map5["3"]; ok {
		fmt.Println(v)
	} else {
		fmt.Println("Key not found")
	}

	// Update a value by key
	map5["2"] = 3
	fmt.Println(map5["2"]) // 2

	// Delete a key-value pair
	delete(map5, "2")
	fmt.Println(map5) // map[1:1]

	// Initialize a map with struct array
	map6 := []map[string]User{
		{
			"1": {
				ID:   "1",
				Name: "John Doe",
			},
		},
		{
			"2": {
				ID:   "2",
				Name: "Jane Doe",
			},
		},
		{
			"3": {
				ID:   "3",
				Name: "John Doe",
			},
		},
	}

	fmt.Println("Iterate over struct array")
	for _, userMap := range map6 {
		for _, user := range userMap {
			fmt.Println(user)
		}
	}

	// Initialize a map with string array with different keys
	map7 := []map[string]string{
		{
			"id":   "1",
			"name": "John Doe",
		},
		{
			"name":    "Jane Doe",
			"address": "123 Main St",
		},
	}

	fmt.Println("Iterate over string array with different keys")
	for _, userMap := range map7 {
		for key, value := range userMap {
			fmt.Println(key, " \t:", value)
		}
	}
}
