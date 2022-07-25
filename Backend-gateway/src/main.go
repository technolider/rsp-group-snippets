package main

import (
	"gateway/controllers"
	"gateway/middleware"
	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/memstore"
	"github.com/gin-gonic/gin"
)

var Router = gin.Default()

func main() {

	store := memstore.NewStore([]byte("secret"))
	Router.Use(sessions.Sessions("mysession", store))

	Router.POST("/login", controllers.LoginJSON)
	Router.GET("/logout", controllers.Logout)
	auth := Router.Group("/auth")
	auth.Use(middleware.Authentication())
	{
		auth.GET("/test", func(c *gin.Context) {
			c.JSON(200, gin.H{
				"message": "Everything is ok",
			})
		})
	}
	// Listen and serve on 0.0.0.0:8080
	Router.Run(":3000")
}
