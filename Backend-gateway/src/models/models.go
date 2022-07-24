package models

type Login struct {
	Login    string `json:"login"`
	Password string `json:"password"`
}

type User struct {
	Login
	Name       string `json:"name"`
	Surname    string `json:"surname"`
	Patronymic string `json:"patronymic"`
	Email      string `json:"email"`
	PhoneNum   string `json:"phone_num"`
}
