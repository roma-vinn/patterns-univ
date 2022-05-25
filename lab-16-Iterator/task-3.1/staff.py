class Employee:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name


class StaffList:
    def __init__(self, employees: list[Employee]):
        self._employees = employees
        self._i = None

    # magic methods that allow you to treat this class as iterator in Python
    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        while self._i < len(self._employees):
            employee = self._employees[self._i]
            self._i += 1
            return employee
        raise StopIteration
