from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self._next = None

    @abstractmethod
    def handle(self, num1: float, num2: float, operation: str):
        pass

    def set_next(self, handler):
        self._next = handler


class AdditionHandler(Handler):
    def __init__(self):
        super(AdditionHandler, self).__init__()

    def handle(self, num1: float, num2: float, operation: str):
        if operation == '+':
            print(f'{num1 + num2 = }')
        elif self._next is not None:
            self._next.handle(num1, num2, operation)
        else:
            print(f"Operation {operation} can't be handled yet.")


class SubtractionHandler(Handler):
    def __init__(self):
        super(SubtractionHandler, self).__init__()

    def handle(self, num1: float, num2: float, operation: str):
        if operation == '-':
            print(f'{num1 - num2 = }')
        elif self._next is not None:
            self._next.handle(num1, num2, operation)
        else:
            print(f"Operation {operation} can't be handled yet.")


class MultiplicationHandler(Handler):
    def __init__(self):
        super(MultiplicationHandler, self).__init__()

    def handle(self, num1: float, num2: float, operation: str):
        if operation == '*':
            print(f'{num1 * num2 = }')
        elif self._next is not None:
            self._next.handle(num1, num2, operation)
        else:
            print(f"Operation {operation} can't be handled yet.")


class DivisionHandler(Handler):
    def __init__(self):
        super(DivisionHandler, self).__init__()

    def handle(self, num1: float, num2: float, operation: str):
        if operation == '/':
            print(f'{num1 / num2 = }')
        elif self._next is not None:
            self._next.handle(num1, num2, operation)
        else:
            print(f"Operation {operation} can't be handled yet.")


class PowerHandler(Handler):
    def __init__(self):
        super(PowerHandler, self).__init__()

    def handle(self, num1: float, num2: float, operation: str):
        if operation == '**':
            print(f'{num1 ** num2 = }')
        elif self._next is not None:
            self._next.handle(num1, num2, operation)
        else:
            print(f"Operation {operation} can't be handled yet.")
