package main

import (
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/putukrisna6/golang-app-starter/config"
)

func main() {
	r := gin.Default()

	r.Use(cors.New(config.SetupCORSConfig()))

	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "Hello, World",
		})
	})

	r.Run()
}
