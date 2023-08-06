from dataclasses import dataclass
from datetime import datetime
from random import random
from time import time
from uuid import uuid4

from pydantic import BaseModel

from utils import timeitit


class OrdinaryClass:
    id: str
    time_complex: datetime
    time_simple: int
    one_data: float
    another_data: float

    def __init__(self) -> None:
        self.id: str = uuid4().hex
        self.time_complex: datetime = datetime.now()
        self.time_simple: int = int(time())
        self.one_data: float = random() * 1000.0
        self.another_data: float = random() * 1000.0


class SlotsClass:
    __slots__ = "id", "time_complex", "time_simple", "one_data", "another_data"

    def __init__(self) -> None:
        self.id: str = uuid4().hex
        self.time_complex: datetime = datetime.now()
        self.time_simple: int = int(time())
        self.one_data: float = random() * 1000.0
        self.another_data: float = random() * 1000.0


@dataclass
class DataClass:
    id: str
    time_complex: datetime
    time_simple: int
    one_data: float
    another_data: float

    def __init__(self) -> None:
        self.id: str = uuid4().hex
        self.time_complex: datetime = datetime.now()
        self.time_simple: int = int(time())
        self.one_data: float = random() * 1000.0
        self.another_data: float = random() * 1000.0


class PydanticClass(BaseModel):
    id: str
    time_complex: datetime
    time_simple: int
    one_data: float
    another_data: float


@timeitit
def gen_ordinary_models(number: int) -> list[OrdinaryClass]:
    return [OrdinaryClass() for _ in range(number)]


@timeitit
def gen_slots_models(number: int) -> list[SlotsClass]:
    return [SlotsClass() for _ in range(number)]


@timeitit
def gen_dataclass_models(number: int) -> list[DataClass]:
    return [DataClass() for _ in range(number)]


@timeitit
def gen_pydanntic_models(number: int) -> list[PydanticClass]:
    return [
        PydanticClass(
            id=uuid4().hex,
            time_complex=datetime.now(),
            time_simple=int(time()),
            one_data=random() * 1000.0,
            another_data=random() * 1000.0,
        )
        for _ in range(number)
    ]


if __name__ == "__main__":
    pass
