package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	amqp "github.com/rabbitmq/amqp091-go"
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

type RequestJSON struct {
	RayID        int               `json:"ray_id"`
	UserID       int               `json:"user_id"`
	Root         string            `json:"root"`
	RootCallBack string            `json:"root_call_back"`
	History      map[string]string `json:"history"`
	Data         any               `json:"data"`
}

func failOnError(err error, msg string) {
	if err != nil {
		log.Panicf("%s: %s", msg, err)
	}
}

func main() {
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	q, err := ch.QueueDeclare(
		"RequestQueue", // name
		false,          // durable
		false,          // delete when unused
		false,          // exclusive
		false,          // no-wait
		nil,            // arguments
	)
	failOnError(err, "Failed to declare a queue")

	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		true,   // auto-ack
		false,  // exclusive
		false,  // no-local
		false,  // no-wait
		nil,    // args
	)
	failOnError(err, "Failed to register a consumer")

	var forever chan struct{}

	go func() {
		for d := range msgs {

			var req RequestJSON
			err := json.Unmarshal([]byte(d.Body), &req)
			failOnError(err, "Failed to unmarshal json")

			if len(req.History) == 0 {
				jsonReq, err := json.Marshal(req)

				request, err := http.NewRequest("POST", "http://192.168.141.139:5000", bytes.NewBuffer(jsonReq))
				request.Header.Set("Content-Type", "application/json; charset=UTF-8")

				client := &http.Client{Timeout: 30 * time.Second}
				response, err := client.Do(request)
				if err != nil {
					panic(err)
				}
				defer response.Body.Close()

				fmt.Println("response Status:", response.Status)
				fmt.Println("response Headers:", response.Header)
				body, _ := ioutil.ReadAll(response.Body)
				fmt.Println("response Body:", string(body))
			}
		}
	}()

	log.Printf(" [*] Waiting for messages. To exit press CTRL+C")
	<-forever
}
