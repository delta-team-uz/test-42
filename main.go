package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/videos/:id", func(c *gin.Context) {
		videoID := c.Param("id")
		videoPath := "videos/" + videoID + ".mp4"

		c.File(videoPath)
	})

	router.Run(":8080")
}
