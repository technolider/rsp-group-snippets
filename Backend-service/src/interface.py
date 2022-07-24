import requests
import json
from flask import Flask, request, make_response
from configparser import ConfigParser


class Interface:
    def __init__(self) -> None:
        config = ConfigParser()  # создаём объекта парсера
        config.read("config.ini")  # читаем конфиг
        self.url = config['config']['SNS_URL']

        """Создание веб-сервера"""
        self.app = Flask(__name__)

        @self.app.route("/", methods=('GET', 'POST'))
        def get_data_json():
            """Получение данных от SNS"""
            self.data = request.get_json(force=True)
            self.last_target, self.pre_last_target = self.get_last_targets()
            self.pre_last_target['service_name'] = list(self.data['history'].keys())[-2]

            self.__update_status = {
                'to': self.pre_last_target['service_name'],
                'ray_id': int(self.data['ray_id']),
                'status_update': 'OK',
                'status_comment': 'something'
            }
            return make_response('Success')

        self.app.run(host='127.0.0.1', port=5000, debug=True)
        """"""

    def get_last_targets(self) -> list:
        """Получение двух последних действий"""
        return list(self.data['history'].values())[-2:]

    def send_update_status(self, update_status: dict) -> None:
        """Отправка данных к SNS"""
        requests.post(url=self.url, data=json.dumps(update_status))
