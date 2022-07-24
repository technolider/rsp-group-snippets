import requests


class Interface:
    def __init__(self, url: str) -> None:
        self.url = url
        self.data = self.get_data()
        self.last_target, self.pre_last_target = self.get_last_targets()
        self.pre_last_target['service_name'] = list(self.data['history'].keys())[-2]

    def get_data(self) -> dict:
        """Получение данных с SNS"""
        response = requests.get(url=self.url)
        data = response.json()
        return data

    def get_last_targets(self) -> list:
        """Получение двух последних действий"""
        return list(self.data['history'].values())[-2:]

    def send_update_status(self, update_status: dict) -> None:
        """Отправка данных к SNS"""
        requests.post(url=self.url, data=update_status)
