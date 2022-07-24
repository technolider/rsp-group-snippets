package DB

import (
	"encoding/json"
	"fmt"
	"gateway/models"
	"net/http"
)

func getJson(url string, target interface{}) error {
	r, err := http.Get(url)
	fmt.Println(r)
	if err != nil {
		return err
	}
	defer r.Body.Close()

	return json.NewDecoder(r.Body).Decode(target)
}

func GetUsersFromDB() (users []models.User) {
	getJson("url", users)
	return
}
