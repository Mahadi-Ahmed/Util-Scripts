package main

import (
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	desktopDir := "/Users/mahadiahmed/Desktop"
	screenShotsDir := "/Users/mahadiahmed/Documents/screenshots"
	// screenShotsDir := "/Users/mahadiahmed/Documents/goMoverTest"

	dir, err := os.ReadDir(desktopDir)
	check(err)
  var movedPngs []string
	for _, file := range dir {
		fileName := file.Name()
		if strings.Contains(fileName, "png") {
			sourceFullPath := desktopDir + "/" + fileName
			destinationFullPath := screenShotsDir + "/" + fileName
      movedPngs = append(movedPngs, fileName)
			os.Rename(sourceFullPath, destinationFullPath)
		}
	}
  fmt.Print("moved files: ")
  fmt.Println(movedPngs)
  fmt.Print("to ~/Documents/screenshots")
}
