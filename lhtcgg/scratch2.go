package main

import (
	"fmt"
)

var x int = 2 

func main() {
	s := "世界"
	fmt.Println(s)
	fmt.Printf("%T\n", s)

	bs := []byte(s)
	fmt.Println(bs)
	fmt.Printf("%T\n", bs)

	for i := 0; i < len(s); i++ {
		fmt.Printf("%#U ", s[i])
	}

	fmt.Println("")

	for i, v := range s {
        fmt.Println(i, v)
		fmt.Printf("at index position %d we have hex %#x\n", i, v)
        fmt.Printf("%T\n", v)
	}
}
