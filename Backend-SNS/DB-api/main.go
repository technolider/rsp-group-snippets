package main

import "fmt"

func main() {
	db := ConnectDB()
	defer db.Close()
	row := db.QueryRow(`SELECT * FROM abc`)
	var id, a, b, c int
	row.Scan(&id, &a, &b, &c)
	fmt.Println(id, a, b, c)
}
