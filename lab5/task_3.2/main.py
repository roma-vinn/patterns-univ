# Expenses client
from sales import SalesTeam, SalesPerson, Manager


def main():
    jane = Manager(name='Jane')
    bob = SalesPerson(name='Bob', manager=jane)
    sue = SalesPerson(name='Sue', manager=jane)
    team = SalesTeam().add_member(jane).add_member(bob).add_member(sue)

    jane.pay_expenses(100)
    print('>' * 50)
    bob.pay_expenses(300)
    print('>' * 50)
    team.pay_expenses(200)


if __name__ == '__main__':
    main()
    # Manager Jane has been paid $100
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # SalesPerson Bob has been paid $300
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Manager Jane has been paid $200
    # SalesPerson Sue has been paid $200
    # SalesPerson Bob has been paid $200
