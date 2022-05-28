from payment import PaymentMethod


class Customer:
    def __init__(self):
        self._payment_method = None

    def set_payment_method(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    def make_payment(self, amount: int):
        if self._payment_method is not None:
            self._payment_method.make_payment(amount)
        else:
            print("Need to set up payment method first")
