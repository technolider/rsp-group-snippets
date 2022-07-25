package main

import (
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
	"github.com/joho/godotenv"
	"log"
	"os"
)

func init() {
	// loads values from .env into the system
	if err := godotenv.Load(); err != nil {
		log.Print("No .env file found")
	}
}

func ConnectDB() (db *sqlx.DB) {

	envvars := map[string]string{
		"username": os.Getenv("DB_USERNAME"),
		"password": os.Getenv("DB_PASSWORD"),
		"url":      os.Getenv("DB_URL"),
	}
	source := fmt.Sprintf("%v:%v@%v", envvars["username"], envvars["password"], envvars["url"])
	db, err := sqlx.Open("mysql", source)
	if err != nil {
		panic(err.Error())
	}
	return db
}
