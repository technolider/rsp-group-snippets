"""
Пример команды:
export PYTHONPATH=/путь/до/корня/проекта
python scripts/ask.py -sf из-какого-сервиса -mf из-какого-метода -st в-какой-сервис -mt в-какой-метод -c 'json-с-данными'
python scripts/ask.py -sf another-fine-service -mf another_fine_method -st rsp-backend-service-template -mt some_method -c '{"ray_id": null, "previous": [{"service": "another-fine-service", "method": "another_fine_method"}], "service": "another-fine-service", "method": "another_fine_method", "ctx": {"someData": "asd"}}'
"""

import json

import click
from dotenv import load_dotenv

load_dotenv()

from worker_init import QUEUE_NAME
from src.base_message import BaseMessage
from src.worker import ask


@click.command()
@click.option('-sf', '--service_from', default=QUEUE_NAME, required=True, help='Название сервиса от которого отправляем реквест.')
@click.option('-mf', '--method_from', required=True, help='Название метода от которого отправляем реквест.')
@click.option('-st', '--service_to', required=True, help='Название сервиса к которому отправляем реквест.')
@click.option('-mt', '--method_to', required=True, help='Название метода к которому отправляем реквест.')
@click.option('-c', '--ctx', required=True, help='Контекст, который засылаем в сервис.')
def put(service_from, method_from, service_to, method_to, ctx):
    ctx = json.loads(ctx)
    ask(BaseMessage(previous=[], service=service_from, method=method_from, ctx=ctx),
        service_to, method_to)


if __name__ == '__main__':
    put()
