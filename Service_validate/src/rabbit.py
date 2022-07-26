import json
import os
from time import sleep

from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.adapters.blocking_connection import BlockingChannel
from pika.exceptions import AMQPConnectionError

DEFAULT_TRIES = int(os.getenv('RABBIT_TRIES', 5))
DEFAULT_USER = os.getenv('RABBIT_USER')
DEFAULT_PASS = os.getenv('RABBIT_PASS')
DEFAULT_HOST = os.getenv('RABBIT_HOST')
DEFAULT_PORT = int(os.getenv('RABBIT_PORT'))
DEFAULT_VENV = '/'


def get_connection(venv: str = DEFAULT_VENV, user: str = DEFAULT_USER, password: str = DEFAULT_PASS,
                   host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> BlockingConnection:
    parameters = ConnectionParameters(host, port, venv, PlainCredentials(user, password))
    return BlockingConnection(parameters)


def get_channel(queue: str, connection: BlockingConnection) -> BlockingChannel:
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    return channel


def put_by_channel(body, queue: str, channel: BlockingChannel):
    channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(body))


def put(body, queue: str, venv: str = DEFAULT_VENV, user: str = DEFAULT_USER, password: str = DEFAULT_PASS,
        host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
    with get_connection(venv, user, password, host, port) as connection:
        channel = get_channel(queue, connection)
        put_by_channel(body, queue, channel)


def handle(callback: callable, queue: str, venv: str = DEFAULT_VENV, user: str = DEFAULT_USER,
           password: str = DEFAULT_PASS, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
    def _callback(ch, method, properties, body):
        try:
            callback(json.loads(body))
        except Exception as e:
            print(e)

    for _ in range(DEFAULT_TRIES):
        try:
            print('🟠🐰 > Пробуем подключиться!')
            with get_connection(venv, user, password, host, port) as connection:
                print('🟢🐰 > Кролик подключен!')
                channel = get_channel(queue, connection)
                channel.basic_consume(queue=queue, auto_ack=True, on_message_callback=_callback)
                try:
                    channel.start_consuming()
                except KeyboardInterrupt as ki:
                    print(ki)
                    channel.stop_consuming()
                break
        except AMQPConnectionError as ace:
            print('🔴🐰 > Кролик недоступен!', ace)
            sleep(10)
