from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from employee import Manager, SalesPerson, StaffList, ITSupport


class Visitor(ABC):
    @abstractmethod
    def visit_manager(self, manager: Manager):
        pass

    @abstractmethod
    def visit_sales_person(self, sales_person: SalesPerson):
        pass

    @abstractmethod
    def visit_it_support(self, it_support: ITSupport):
        pass

    @abstractmethod
    def visit_staff_list(self, staff_list: StaffList):
        pass


class RaiseVisitor(Visitor):
    def __init__(self, percent: int):
        assert 1 <= percent <= 50, f'Raise should be between 1% and 50%, got {percent}%'
        self._percent = percent

    def visit_manager(self, manager: Manager):
        salary = manager.get_salary()
        manager.set_salary(salary + int(salary * (self._percent / 100)))

    def visit_sales_person(self, sales_person: SalesPerson):
        salary = sales_person.get_salary()
        sales_person.set_salary(salary + int(salary * (self._percent / 100)))

    def visit_it_support(self, it_support: ITSupport):
        salary = it_support.get_salary()
        it_support.set_salary(salary + int(salary * (self._percent / 100)))

    def visit_staff_list(self, staff_list: StaffList):
        print(f'Each member of staff list got a {self._percent}% raise.')


class FineVisitor(Visitor):
    def __init__(self, fine: int):
        assert 1 <= fine, f'Fine should be between > 0, got {fine}'
        self._fine = fine

    def visit_manager(self, manager: Manager):
        salary = manager.get_salary()
        manager.set_salary(max(0, salary - self._fine))  # fine can't be greater than salary

    def visit_sales_person(self, sales_person: SalesPerson):
        salary = sales_person.get_salary()
        sales_person.set_salary(max(0, salary - self._fine))  # fine can't be greater than salary

    def visit_it_support(self, it_support: ITSupport):
        salary = it_support.get_salary()
        it_support.set_salary(max(0, salary - self._fine))  # fine can't be greater than salary

    def visit_staff_list(self, staff_list: StaffList):
        print(f'Each member of staff list got a {self._fine} fine.')
