from collections.abc import Callable
from dataclasses import dataclass

from src.base_message import BaseMessage, Trace
from src.rabbit import handle, put

default_function = Callable[[BaseMessage], None]


@dataclass
class MethodMeta:
    name: str
    function: default_function


class Worker:
    def __init__(self, queue_name: str):
        self.queue_name: str = queue_name
        self.methods: dict[str, MethodMeta] = dict()

    def run(self):
        handle(self.callback, self.queue_name)

    def callback(self, body: dict):
        print('🟢 > Event processing has been started', body)
        msg: BaseMessage = BaseMessage(**body)

        self.methods.get(msg.method).function(msg)
        if not (msg.previous is None):
            trace: Trace = msg.previous[-1]
            prev_msg: BaseMessage = BaseMessage(previous=msg.previous[:-1], service=trace.service, method=trace.method,
                                                ctx=msg.ctx)
            ask(prev_msg, trace.service, trace.method)

    def method(self, function: default_function):
        if self.methods.get(function.__name__):
            raise Exception('Метод уже зарегистрирован')

        self.methods[function.__name__] = MethodMeta(name=function.__name__, function=function)

        return function


def response(msg: BaseMessage):
    msg = BaseMessage(service=msg.previous[-1].service, method=msg.previous[-1].method, previous=msg.previous[:-1],
                      ctx=msg.ctx)
    put(msg.dict(), msg.service)


def ask(msg: BaseMessage, service: str, method: str):
    msg = BaseMessage(service=service, method=method,
                      previous=msg.previous + [Trace(service=msg.service, method=msg.method)],
                      ctx=msg.ctx)
    put(msg.dict(), msg.service)


def abort(msg: BaseMessage):
    msg.previous = []