import sqlite3 as sql


class DB:
    def __init__(self) -> None:
        """
            Подключение в таблице
        """
        self.db = sql.connect('db/type.db')
        self.cur = self.db.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS types(type TEXT, fio TEXT, age INT, exp INT)')
        self.db.commit()

    def append_person(self, person: dict) -> None:
        """
            Добавление нового работника в БД
        """
        self.cur.execute('INSERT INTO types VALUES(:type, :fio, :age, :exp)',
                         {'type': person['type'].lower(), 'fio': person['fio'], 'age': person['age'], 'exp': person['exp']})
        self.db.commit()

    def search_person(self, typ):
        """
            Вытаскивание сотрудника
        """
        person = self.cur.execute('SELECT * from types WHERE type == ?', (typ, )).fetchall()
        return person
