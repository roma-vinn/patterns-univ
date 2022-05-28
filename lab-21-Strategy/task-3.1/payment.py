from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount: int):
        pass


class BankPayment(PaymentMethod):
    def make_payment(self, amount: int):
        print(f'Payment ${amount} made from bank account.')


class PayPalPayment(PaymentMethod):
    def make_payment(self, amount: int):
        print(f'Payment ${amount} made from PayPal.')


class ApplePayPayment(PaymentMethod):
    def make_payment(self, amount: int):
        print(f'Payment ${amount} made from Apple Pay.')


class GooglePayPayment(PaymentMethod):
    def make_payment(self, amount: int):
        print(f'Payment ${amount} made from Google Pay.')
