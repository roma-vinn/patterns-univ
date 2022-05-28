from customer import Customer
from payment import BankPayment, PayPalPayment, ApplePayPayment, GooglePayPayment


def main():
    customer = Customer()
    customer.make_payment(100)

    customer.set_payment_method(PayPalPayment())
    customer.make_payment(100)

    customer.set_payment_method(BankPayment())
    customer.make_payment(200)

    customer.set_payment_method(ApplePayPayment())
    customer.make_payment(20)

    customer.set_payment_method(GooglePayPayment())
    customer.make_payment(10)


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Need to set up payment method first
    # Payment $100 made from PayPal.
    # Payment $200 made from bank account.
    # Payment $20 made from Apple Pay.
    # Payment $10 made from Google Pay.
