from dotenv import load_dotenv

load_dotenv()

from worker_init import worker
from src.base_message import BaseMessage
from src.worker import ask
import threading
import os


questions = []


def print_menu() -> None:
    print("МЕНЮ")
    print("------------------------------------")
    print("1. Найти сотрудника")
    print("2. Добавить сотрудника в базу данных")
    print("3. Выйти из программы")
    print("------------------------------------")


def read_menu() -> int:
    while True:
        input_value = int(input())
        if 1 <= input_value <= 3:
            return input_value
        else:
            raise Exception("INVALID_INPUT")


def tui():
    while True:
        print('hfhjhfjfhjfhjfjhjfhi')
        try:
            msg = {"ray_id": 1, "previous": [], "service": "tui",
                   "method": "tui", "ctx": {}}
            print('hfghfgjfjfhjghjfi')
            print_menu()
            val = read_menu()
            if val == 1:
                ask(BaseMessage(dict(**msg)), 'validate', 'validate_prof')
                print(questions.pop(0))
                typ = input()
                msg['ctx']['type'] = typ
                ask(BaseMessage(dict(**msg)), 'validate', 'validate_prof')
            elif val == 2:
                pass
            else:
                os._exit(0)
        except Exception:
            print("Входные данные некорректны. Отправьте снова.")


@worker.method
def find(msg: BaseMessage):
    """
    Данная функция будет обрабатывать услугу find сервиса tui
    """
    question = msg.ctx['question']
    questions.append(question)
    del(msg.ctx['question'])


@worker.method
def tui_print(msg: BaseMessage):
    """
    Данная функция будет обрабатывать услугу tui_print сервиса tui
    """
    for person in msg.ctx['persons']:
        print(f'{person[0].capitalize()} {person[1]}, возраст - {person[2]}, опыт работы - {person[3]}')


if __name__ == '__main__':
    thread_tui = threading.Thread(target=tui)
    thread_worker = threading.Thread(target=worker.run())

    thread_tui.start()
    thread_worker.start()
