import sys
sys.path.append("../../temp/src")

from service_template import Service

class HR_service(Service):
    def __init__(self):
        pass
        
    def send_status(self, status:str, comment:str) -> None:
        self.set_status_update(status)
        self.set_status_comment(comment)
        self.send_update_status()
    
    def BL_10_1(self):
        #TODO: Add call seach
        self.send_status("IN_PROGRESS", "Новая заявка")
    
    def BL_req_portret(self):
        #TODO: Add call ask portret via GUI
        self.send_status("IN_PROGRESS", "Ожидание портрета пользователя")

    def BL_req_expert(self):
        #TODO: Add call кадровый резерв
        self.send_status("IN_PROGRESS", "Просмотр резерва")

    def BL_communicate_to_expert(self):
        #TODO: Add call msg to expert
        self.send_status("IN_PROGRESS", "Приглашение резервных сотрудников")

    def BL_wait_expert(self):
        #TODO: Add call wait answer to expert
        self.send_status("IN_PROGRESS", "Ожидание ответа резервных сотрудников")

    def BL_create_vacancy(self):
        #TODO: Add call create vacancy
        self.send_status("IN_PROGRESS", "Создание вакансии")

    def BL_searh_new_expert(self):
        #TODO: Add call searhing new expert

obj = HR_service()
