package models

type Login struct {
	Login    string `json:"login"`
	Password string `json:"password"`
}

type User struct {
	Id             int    `json:"id" db:"id"`
	Login          string `json:"login"`
	Password       string `json:"password"`
	UserName       string `json:"user_name" db:"user_name"`
	UserSurname    string `json:"user_surname" db:"user_surname"`
	UserPatronymic string `json:"user_patronymic" db:"user_patronymic"`
}
