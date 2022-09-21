import requests
import json
from flask import Flask, request, make_response
from configparser import ConfigParser


class Interface:
    def __init__(self) -> None:
        """Читаем конфиг"""
        config = ConfigParser()
        config.read("../../config.ini")
        self.url = config['config']['SNS_URL']

    def create_web_server(self) -> None:
        """Создание веб-сервера"""
        self.app = Flask(__name__)

        @self.app.route("/", methods=('GET', 'POST'))
        def get_data_json():
            """Получение данных от SNS"""
            self.data = request.get_json(force=True)
            self.get_last_targets()
            return make_response('Success')

        self.app.run(host='127.0.0.1', port=5000, debug=True)

    def send_update_status(self, update_status: dict) -> None:
        """Отправка данных к SNS"""
        requests.post(url=self.url, data=json.dumps(update_status))
