from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from military import GeneralStaff, MilitaryBase


class Spy(ABC):
    @abstractmethod
    def visit_general_staff(self, general_staff: GeneralStaff):
        pass

    @abstractmethod
    def visit_military_base(self, military_base: MilitaryBase):
        pass


class SecretAgent(Spy):
    def visit_general_staff(self, general_staff: GeneralStaff):
        print(f'Secret Agent counted {general_staff.generals_count} generals and'
              f' copied all {general_staff.secret_paper_count} secret papers.')

    def visit_military_base(self, military_base: MilitaryBase):
        print(f'Secret agent counted {military_base.officers_count} officers,'
              f' {military_base.soldiers_count} soldiers,'
              f' {military_base.jeeps_count} jeeps and'
              f' {military_base.tanks_count} tanks'
              f' on the military base.')


class Saboteur(Spy):
    def visit_general_staff(self, general_staff: GeneralStaff):
        print(f'Saboteur destroyed at most 10 out of {general_staff.secret_paper_count} secret papers.')
        general_staff.secret_paper_count = max(0, general_staff.secret_paper_count - 10)

    def visit_military_base(self, military_base: MilitaryBase):
        print(f'Saboteur destroyed at most 5 out of {military_base.jeeps_count} jeeps and'
              f' at most 1 of {military_base.tanks_count} tank.')
        military_base.jeeps_count = max(0, military_base.jeeps_count - 5)
        military_base.tanks_count = max(0, military_base.tanks_count - 1)
