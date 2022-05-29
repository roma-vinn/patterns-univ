from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from spy import Spy


class MilitaryObject(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def accept(self, spy: Spy):
        pass


class GeneralStaff(MilitaryObject):
    def __init__(self, generals_count: int, secret_paper_count: int):
        self.generals_count = generals_count
        self.secret_paper_count = secret_paper_count

    def __str__(self):
        return f"GeneralStaff: {self.generals_count} generals and {self.secret_paper_count} secret papers."

    def accept(self, spy: Spy):
        spy.visit_general_staff(self)


class MilitaryBase(MilitaryObject):
    def __init__(self, officers_count: int, soldiers_count: int, jeeps_count: int, tanks_count: int):
        self.officers_count = officers_count
        self.soldiers_count = soldiers_count
        self.jeeps_count = jeeps_count
        self.tanks_count = tanks_count

    def __str__(self):
        return f"MilitaryBase: {self.officers_count} officers," \
               f" {self.soldiers_count} soldiers," \
               f" {self.jeeps_count} jeeps and" \
               f" {self.tanks_count} tanks."

    def accept(self, spy: Spy):
        spy.visit_military_base(self)
