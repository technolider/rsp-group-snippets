package main

import (
	"fmt"
	"github.com/jmoiron/sqlx"
)

type User struct {
	Id             int    `json:"id" db:"id"`
	Login          string `json:"login" db:"login"`
	Password       string `json:"password" db:"password"`
	UserName       string `json:"user_name" db:"user_name"`
	UserSurname    string `json:"user_surname" db:"user_surname"`
	UserPatronymic string `json:"user_patronymic" db:"user_patronymic"`
}

func GetUserById(id int, db *sqlx.DB) User {
	resp := db.QueryRowx(`SELECT * FROM users WHERE id=?`, id)
	var user User
	err := resp.StructScan(&user)
	if err != nil {
		fmt.Println(err.Error())
	}
	return user
}

func GetUserByLogin(login string, db *sqlx.DB) User {
	resp := db.QueryRowx(`SELECT * FROM users WHERE login=?`, login)
	var user User
	err := resp.StructScan(&user)
	if err != nil {
		fmt.Println(err.Error())
	}
	return user
}

func GetAllUsers(db *sqlx.DB) []User {
	resp, err := db.Queryx("SELECT * FROM users")
	if err != nil {
		fmt.Println(err.Error())
	}
	var users []User

	for resp.Next() {
		var user User
		err := resp.StructScan(&user)
		if err != nil {
			fmt.Println(err.Error())
		} else {
			users = append(users, user)
		}
	}

	return users
}

func RemoveUserById(id int, db *sqlx.DB) string {
	resp := db.QueryRowx(`DELETE FROM users WHERE id=?`, id)
	var res string
	err := resp.Scan(&res)
	if err != nil {
		fmt.Println(err.Error())
	}
	return res
}

type UserRequest struct {
	Id            int    `json:"id" db:"id"`
	Login         string `json:"login" db:"login"`
	Position      string `json:"position" db:"position"`
	Qualification string `json:"qualification" db:"qualification"`
}

type ID struct {
	Id int `json:"id"`
}
type Login struct {
	Login string `json:"login"`
}
