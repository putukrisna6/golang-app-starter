package main

import (
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/putukrisna6/golang-app-starter/config"
	"gorm.io/gorm"
)

var (
	db *gorm.DB = config.SetupDatabaseConnection()
)

func main() {
	defer config.CloseDatabaseConnection(db)

	// Prepare Routing
	r := gin.Default()
	r.Use(cors.New(config.SetupCORSConfig()))

	// Route List
	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "Hello, World",
		})
	})

	r.Run()
}
