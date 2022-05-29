from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from visitor import Visitor


class Employee(ABC):
    @abstractmethod
    def get_salary(self) -> int:
        pass

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Manager(Employee):
    def __init__(self, salary: int):
        self._salary = salary

    def set_salary(self, new_salary: int):
        self._salary = new_salary

    def get_salary(self) -> int:
        return self._salary

    def accept(self, visitor: Visitor):
        visitor.visit_manager(self)


class SalesPerson(Employee):
    def __init__(self, salary: int):
        self._salary = salary

    def set_salary(self, new_salary: int):
        self._salary = new_salary

    def get_salary(self) -> int:
        return self._salary

    def accept(self, visitor: Visitor):
        visitor.visit_sales_person(self)


class ITSupport(Employee):
    def __init__(self, salary: int):
        self._salary = salary

    def set_salary(self, new_salary: int):
        self._salary = new_salary

    def get_salary(self) -> int:
        return self._salary

    def accept(self, visitor: Visitor):
        visitor.visit_it_support(self)


class StaffList(Employee):
    def __init__(self):
        self._employees: set[Employee] = set()

    def add_employee(self, employee: Employee):
        self._employees.add(employee)

    def get_salary(self) -> int:
        total = 0
        for employee in self._employees:
            total += employee.get_salary()

        return total

    def accept(self, visitor: Visitor):
        visitor.visit_staff_list(self)
        for employee in self._employees:
            employee.accept(visitor)
