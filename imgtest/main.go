package main

import (
	//"image"
	//"image/color"
	"log"

	"github.com/disintegration/imaging"
)

func main() {
	// Open a test image.
	src, err := imaging.Open("melon.jpg")
	if err != nil {
		log.Fatalf("failed to open image: %v", err)
	}
	// Resize the cropped image to width = 300px preserving the aspect ratio.
	dst_1 := imaging.Resize(src, 1200, 0, imaging.CatmullRom)

	dst_2 := imaging.Resize(src, 300, 0, imaging.CatmullRom)

	// Scale down srcImage to fit the 800x600px bounding box.
	//dst := imaging.Fit(src, 800, 600, imaging.Lanczos)

	// Scale down srcImage to fit the 800x600px bounding box.
	// dst := imaging.Fit(src, 800, 600, imaging.Lanczos)

	// Resize and crop the srcImage to fill the 100x100px area.
	//dst := imaging.Fill(src, 100, 100, imaging.Center, imaging.Lanczos)

	// Save the resulting image as JPEG.
	err = imaging.Save(dst_1, "output_1.jpg")
	if err != nil {
		log.Fatalf("failed to save image: %v", err)
	}
	err = imaging.Save(dst_2, "output_2.jpg")
	if err != nil {
		log.Fatalf("failed to save image: %v", err)
	}
}