from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    FREE = 1
    BUSY = 2


@dataclass
class Desk:
    number: int
    status: Status

    @property
    def is_free(self):
        return self.status == Status.FREE


@dataclass
class Office:
    desks: list[Desk]

    def is_full(self):
        full = True
        for desk in self.desks:
            if desk.is_free:
                full = False
                break

        return full


desk = Desk(number=1, status=Status.BUSY)
office = Office(desks=[desk])

office.is_full()
