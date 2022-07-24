package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Login struct {
	User     string `json:"user"`
	Password string `json:"password"`
}

func getJson(url string, target interface{}) error {
	r, err := http.Get(url)
	fmt.Println(r)
	if err != nil {
		return err
	}
	defer r.Body.Close()

	return json.NewDecoder(r.Body).Decode(target)
}

func main() {

	login := &Login{}
	getJson("http:///localhost:3000/", login)
	fmt.Println(login)
}
