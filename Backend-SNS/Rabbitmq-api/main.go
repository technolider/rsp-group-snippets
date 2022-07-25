package main

import (
	"encoding/json"
	"github.com/gin-gonic/gin"
	amqp "github.com/rabbitmq/amqp091-go"
	"log"
	"net/http"
)

type RequestJSON struct {
	RayID        int    `json:"ray_id"`
	UserID       int    `json:"user_id"`
	Root         string `json:"root"`
	RootCallBack string `json:"root_call_back"`
	History      any    `json:"history"`
	Data         any    `json:"data"`
}

func failOnError(err error, msg string) {
	if err != nil {
		log.Panicf("%s: %s", msg, err)
	}
}

func newRequest(ch *amqp.Channel, q amqp.Queue, body RequestJSON) {
	b, err := json.Marshal(body)
	failOnError(err, "Failed to marshal a message")
	err = ch.Publish(
		"",     // exchange
		q.Name, // routing key
		false,  // mandatory
		false,  // immediate
		amqp.Publishing{
			ContentType: "text/plain",
			Body:        []byte(b),
		})
	failOnError(err, "Failed to publish a message")
	log.Printf(" [x] Sent %s\n", body)
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

	r := gin.Default()
	r.GET("/RBMQ/newRequest", func(c *gin.Context) {
		//newRequest(ch, q)
		var req RequestJSON
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		} else {
			newRequest(ch, q, req)
			c.JSON(http.StatusOK, "msg addet to queue")
		}
	})
	r.Run(":4000")

}
