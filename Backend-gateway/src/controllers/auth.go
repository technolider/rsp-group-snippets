package controllers

import (
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"gateway/models"
	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
	"io/ioutil"
	"net/http"
)

func toHash(str string) string {
	data := []byte(str)
	hash := sha256.Sum256(data)
	return fmt.Sprintf("%x", hash[:])

}

func check() {

}

func LoginJSON(c *gin.Context) {

	var req models.Login
	//user := DB.GetUsersFromDB()
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	var user []models.User
	resp, err := http.Get("http://localhost:2000/DB/getAllUsers")
	if err != nil {
		fmt.Println(err.Error())
	}
	defer resp.Body.Close()
	jsonDataFromHttp, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err.Error())
	}

	err = json.Unmarshal([]byte(jsonDataFromHttp), &user)
	//fmt.Println(reflect.TypeOf(user))
	data := []byte("password")
	hash := sha256.Sum256(data)
	//fmt.Printf("%x", hash[:])
	h := fmt.Sprintf("%x", hash[:])
	fmt.Println(h)
	for i := 0; i < len(user); i++ {
		if user[i].Login == req.Login && user[i].Password == toHash(req.Password) {
			c.JSON(http.StatusOK, "ok")
			break
		}
	}
	//for i, var := range user {
	//	if var.Login == req.Login && var.Password == req.Password {
	//		c.JSON(http.StatusOK, "ok")
	//		return
	//	}
	//}

	session := sessions.Default(c)
	session.Set("id", "userid")
	session.Set("email", "test@gmail.com")
	session.Save()

}

func Logout(c *gin.Context) {
	session := sessions.Default(c)
	session.Clear()
	session.Save()
	c.JSON(http.StatusOK, gin.H{
		"message": "User Sign out successfully",
	})
}
