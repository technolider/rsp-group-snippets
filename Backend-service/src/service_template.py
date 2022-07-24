from interface import Interface


class Service(Interface):
    def __init__(self) -> None:
        """Получение данных с SNS (data, last_target, pre_last_target) и функции send_update_status"""
        super().__init__()

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
