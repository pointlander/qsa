package main

import (
	"github.com/pointlander/qsa/liblsl"
)

func main() {
	inlet := liblsl.Start()
	liblsl.Sample(inlet)
	liblsl.Stop(inlet)
}
