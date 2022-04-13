package config

import (
	"github.com/gin-contrib/cors"
)

func SetupCORSConfig() cors.Config {
	return cors.Config{
		AllowMethods:     []string{"POST", "PUT", "PATCH", "GET", "DELETE", "HEAD", "OPTIONS"},
		AllowHeaders:     []string{"Origin", "Content-Length", "Content-Type", "Authorization"},
		ExposeHeaders:    []string{"Content-Length"},
		AllowAllOrigins:  true,
		AllowCredentials: true,
	}
}
