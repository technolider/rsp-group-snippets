from __future__ import annotations
from pydantic import BaseModel


class Trace(BaseModel):
    service: str
    method: str


# TODO не предусмотрено сокрытие данных и защита от изменения внешнего контекста
class BaseMessage(BaseModel):
    ray_id: int = None
    previous: list[Trace]
    service: str
    method: str
    ctx: dict = dict()
