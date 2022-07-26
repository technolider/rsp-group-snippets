import os

from src.worker import Worker

QUEUE_NAME = os.getenv('QUEUE_NAME')

worker = Worker(QUEUE_NAME)
