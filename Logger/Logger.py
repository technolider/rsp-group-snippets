import logging

class Logger():
    def __init__(self, log_file_name:str) -> None:
        self.recieve_logger = logging.getLogger("RECIEVED")
        self.sent_logger = logging.getLogger("SENT")
        self.recieve_logger.setLevel(logging.INFO)
        self.sent_logger.setLevel(logging.INFO)

        recieve_logger_fh = logging.FileHandler("backend/logs/{}_recieved.log".format(log_file_name))
        sent_logger_fh = logging.FileHandler("backend/logs/{}_sent.log".format(log_file_name))

        logger_formatter = logging.Formatter('%(asctime)s - %(message)s')

        recieve_logger_fh.setFormatter(logger_formatter)
        sent_logger_fh.setFormatter(logger_formatter)

        self.recieve_logger.addHandler(recieve_logger_fh)
        self.sent_logger.addHandler(sent_logger_fh)

    
    def log_recieved(self, sender: str) -> None:
        """
        Вносит в логи время получения запроса и адрес отправителя
        Данные об отправителе вносятся ВРУЧНУЮ
        """
        self.recieve_logger.info(sender)


    def log_sent(self, recipient: str) -> None:
        """
        Вносит в логи время отправки запроса и адрес получателя
        Данные о получателе вносятся ВРУЧНУЮ
        """
        self.sent_logger.info(recipient)


