from interface import Interface


class Service:
    def __init__(self) -> None:
        """Создание веб-сервера"""
        Interface.__init__(self)
        Interface.create_web_server(self)

    def get_last_targets(self) -> None:
        """Получение двух последних действий и создание статуса"""
        self.last_target = list(self.data['history'].values())[-2:-1][0]
        self.last_target['service_name'] = list(self.data['history'].keys())[-2]

        # Отправка статуса предыдущему сервису, если это нужно
        if self.last_target['is_callback_needed']:
            self.__update_status = {
                'to': self.last_target['service_name'],
                'ray_id': int(self.data['ray_id']),
                'status_update': 'OK',
                'status_comment': 'something'
            }
            self.give_data_last_service()

    def give_data_last_service(self) -> None:
        """Отправка данных о статусе"""
        Interface.send_update_status(self, self.__update_status)

    def set_status_update(self, status: str) -> None:
        """Редактирование статуса"""
        self.__update_status['status_update'] = status

    def set_status_comment(self, comment: str) -> None:
        """Редактирование комментария статуса"""
        self.__update_status['status_comment'] = comment


serv = Service()
