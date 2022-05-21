from operation_handler import AdditionHandler, SubtractionHandler, MultiplicationHandler, DivisionHandler, PowerHandler


def get_handler():
    add = AdditionHandler()
    sub = SubtractionHandler()
    mul = MultiplicationHandler()
    div = DivisionHandler()
    pow_ = PowerHandler()

    add.set_next(sub)
    sub.set_next(mul)
    mul.set_next(div)
    div.set_next(pow_)

    return add


def main():
    handler = get_handler()

    a, b = 4, 2
    operations = ['+', '-', '*', '/', '**']

    for op in operations:
        handler.handle(a, b, op)


if __name__ == '__main__':
    main()
    # num1 + num2 = 6
    # num1 - num2 = 2
    # num1 * num2 = 8
    # num1 / num2 = 2.0
    # num1 ** num2 = 16
