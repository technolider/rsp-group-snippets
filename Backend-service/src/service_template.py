from interface import Interface


class Service:
    def __init__(self) -> None:
        """Получение данных с SNS (data, last_target, pre_last_target) и функции send_update_status"""
        Interface.__init__(self)
        Interface.create_web_server(self)

    def get_last_targets(self) -> None:
        """Получение двух последних действий и создание статуса"""
        self.last_target, self.pre_last_target = list(self.data['history'].values())[-2:]
        self.pre_last_target['service_name'] = list(self.data['history'].keys())[-2]

        self.__update_status = {
            'to': self.pre_last_target['service_name'],
            'ray_id': int(self.data['ray_id']),
            'status_update': 'OK',
            'status_comment': 'something'
        }

    def is_callback_needed(self) -> bool:
        """Нужны ли данные предыдущему сервису"""
        return self.pre_last_target['is_callback_needed']

    def give_data_last_service(self) -> None:
        """Отправка данных о статусе"""
        if self.is_callback_needed():
            self.send_update_status(self.__update_status)

    def set_status_update(self, status: str) -> None:
        self.__update_status['status_update'] = status

    def set_status_comment(self, comment: str) -> None:
        self.__update_status['status_comment'] = comment


serv = Service()
while True:
    if serv.data:
        print(serv.data)

