from dotenv import load_dotenv

load_dotenv()

from worker_init import worker
from src.base_message import BaseMessage
from src.worker import ask


@worker.method
def validate_prof(msg: BaseMessage):
    """
        Данная функция будет обрабатывать услугу validate_prof сервиса validate
    """
    prof = ['разработчик', 'маркетолог', 'инженер', 'дизайнер']

    if 'type' in msg.ctx.keys():
        if msg.ctx['type'] in prof and 'persons' not in msg.ctx.keys():
            print('Введены корректные данные!')

            ask(BaseMessage(**dict(msg)), 'storage', 'search_person')
        else:
            ask(BaseMessage(**dict(msg)), 'tui', 'tui_print')
            return
    else:
        msg.ctx['question'] = 'Кто нужен?'
        ask(BaseMessage(**dict(msg)), 'tui', 'find')


if __name__ == '__main__':
    worker.run()
