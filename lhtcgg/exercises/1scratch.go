package main

import (
	"fmt"
	"runtime"
)

var x uint8 = 255
var y float32 = 42.556

func main() {
	x := int(x)
	fmt.Println(x)
	fmt.Printf("%T ", x)
	fmt.Printf("%T\n", y)
	fmt.Println(runtime.GOOS)
	fmt.Println(runtime.GOARCH)

}
