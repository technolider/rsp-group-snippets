package controllers

import (
	"gateway/models"
	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
	"net/http"
)

func LoginJSON(c *gin.Context) {

	var json models.Login
	//user := DB.GetUsersFromDB()
	if err := c.ShouldBindJSON(&json); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	//TODO проверка пользователя
	if json.Login != "manu" || json.Password != "123" {
		c.JSON(http.StatusUnauthorized, gin.H{"status": "unauthorized"})
		return
	}

	session := sessions.Default(c)
	session.Set("id", "userid")
	session.Set("email", "test@gmail.com")
	session.Save()
	c.JSON(http.StatusOK, gin.H{
		"message": "User Sign In successfully",
	})
}

func Logout(c *gin.Context) {
	session := sessions.Default(c)
	session.Clear()
	session.Save()
	c.JSON(http.StatusOK, gin.H{
		"message": "User Sign out successfully",
	})
}
