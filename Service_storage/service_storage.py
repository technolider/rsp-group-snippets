from db.sql import DB
from dotenv import load_dotenv

load_dotenv()

from worker_init import worker
from src.base_message import BaseMessage
from src.worker import ask


@worker.method
def search_person(msg: BaseMessage):
    """
        Данная функция будет обрабатывать услугу search_person сервиса storage
    """
    typ = msg.ctx['type'].lower()
    print(f'Успешно отправили данные о сотруднике {typ}!')
    msg.ctx['persons'] = db.search_person(typ)
    return


@worker.method
def append_person(msg: BaseMessage):
    """
        Данная функция будет обрабатывать услугу append_person сервиса storage
    """
    person = msg.ctx['person']
    db.append_person(person)
    print(f'Успешно добавили сотрудника {person["type"]}')


if __name__ == '__main__':
    db = DB()
    worker.run()
