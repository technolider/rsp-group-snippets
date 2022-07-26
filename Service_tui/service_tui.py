from dotenv import load_dotenv

load_dotenv()

from worker_init import worker
from src.base_message import BaseMessage
from src.worker import ask, abort
import threading
import os
import time


messages: list[BaseMessage] = []


def print_menu() -> None:
    print(
        'МЕНЮ'
        '\n------------------------------------\n'
        '1. Найти сотрудника\n'
        '2. Добавить сотрудника в базу данных\n'
        '3. Выйти из программы'
        '\n------------------------------------\n'
    )


def read_menu() -> int:
    while True:
        input_value = int(input())
        if 1 <= input_value <= 3:
            return input_value
        else:
            raise Exception("INVALID_INPUT")


def tui():
    while True:
        # try:
        print_menu()
        val = int(read_menu())
        msg = {"ray_id": 1, "previous": [], "service": "tui", "method": "tui", "ctx": {}}
        if val == 1:
            def a():
                if messages:
                    msg: BaseMessage = messages.pop(0)
                    print(msg.ctx['question'])
                    typ = input()
                    msg.ctx['type'] = typ
                    ask(BaseMessage(**msg.dict()), 'validate', 'validate_prof')
            t = threading.Timer(3, a)
            t.start()
            ask(BaseMessage(**msg), 'validate', 'validate_prof')
            time.sleep(12)
        elif val == 2:
            questions_list = ['Профессия: ', 'ФИО: ', 'Возраст: ', 'Опыт работы: ']
            portrait = []
            for question in questions_list:
                answer = input(question)
                portrait.append(answer)
        else:
            os._exit(0)
        # except Exception as e:
        #     print(e)
        #     print("Входные данные некорректны. Отправьте снова.")


@worker.method
def find(msg: BaseMessage):
    """
    Данная функция будет обрабатывать услугу find сервиса tui
    """
    messages.append(BaseMessage(**msg.dict()))
    abort(msg)


@worker.method
def tui_print(msg: BaseMessage):
    """
    Данная функция будет обрабатывать услугу tui_print сервиса tui
    """
    for person in msg.ctx['persons']:
        print(f'{person[0].capitalize()} {person[1]}, возраст - {person[2]}, опыт работы - {person[3]}')
    abort(msg)


if __name__ == '__main__':
    thread_tui = threading.Thread(target=tui)
    thread_worker = threading.Thread(target=worker.run)

    thread_tui.start()
    thread_worker.start()
