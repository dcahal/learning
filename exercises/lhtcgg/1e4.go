package main

import "fmt"

type badbrains int

var x badbrains

func main() {

	fmt.Println(x)
	fmt.Printf("%T\n", x)
	x = 42
	fmt.Println(x)
}
