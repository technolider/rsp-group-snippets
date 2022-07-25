package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	db := ConnectDB()
	defer db.Close()
	row := db.QueryRow(`SELECT * FROM abc`)
	var id, a, b, c int
	row.Scan(&id, &a, &b, &c)
	fmt.Println(id, a, b, c)
	r := gin.Default()
	r.GET("/DB/getUserById", func(c *gin.Context) {
		var id ID
		if err := c.ShouldBindJSON(&id); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		usr := GetUserById(id.Id, db)

		c.JSON(http.StatusOK, usr)
	})

	r.GET("/DB/getUserByLogin", func(c *gin.Context) {
		var login Login
		if err := c.ShouldBindJSON(&login); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		usr := GetUserByLogin(login.Login, db)

		c.JSON(http.StatusOK, usr)
	})

	r.GET("/DB/getAllUsers", func(c *gin.Context) {
		usrs := GetAllUsers(db)

		c.JSON(http.StatusOK, usrs)
	})

	r.DELETE("/DB/deleteUserById", func(context *gin.Context) {
		var id ID
		if err := context.ShouldBindJSON(&id); err != nil {
			context.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		res := RemoveUserById(id.Id, db)

		context.JSON(http.StatusOK, res)
	})
	r.Run(":2000") // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
