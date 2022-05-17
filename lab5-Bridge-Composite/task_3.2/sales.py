from abc import ABC, abstractmethod


class Sales(ABC):
    @abstractmethod
    def pay_expenses(self, amount: int):
        pass


class Manager(Sales):
    def __init__(self, name: str):
        self._name = name

    def pay_expenses(self, amount: int):
        print(f"Manager {self._name} has been paid ${amount}")


class SalesPerson(Sales):
    def __init__(self, name: str, manager: Manager):
        self._name = name
        self._manager = manager

    def pay_expenses(self, amount: int):
        print(f"SalesPerson {self._name} has been paid ${amount}")


class SalesTeam(Sales):
    def __init__(self):
        self._members: set[Sales] = set()

    def add_member(self, sales: Sales):
        self._members.add(sales)
        return self

    def remove_member(self, sales: Sales):
        self._members.remove(sales)

    def pay_expenses(self, amount: int):
        for member in self._members:
            member.pay_expenses(amount)
