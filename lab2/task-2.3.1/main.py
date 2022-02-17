import random
from creators import Cooker, EspressoCooker, AmericanoCooker, CappuccinoCooker, LatteCooker, CocoaCooker
from collections import Counter

def main():
    menu: 'list[Cooker]' = [EspressoCooker(), AmericanoCooker(), CappuccinoCooker(), LatteCooker(), CocoaCooker()]
    working_hours = 8  # one day
    avg_clients_per_hour = 18
    total_revenue = 0
    total_ingredients = []

    for _ in range(working_hours):
        clients = int(random.normalvariate(avg_clients_per_hour, 3))
        for _ in range(clients):
            drink = random.choice(menu).cook()
            total_revenue += drink.cost
            total_ingredients += drink.ingredients_list

    print(f'For {working_hours} working hours:')
    print(f'\tTotal revenue: {total_revenue}')
    print(f'\tTotal ingredients usage:')  # additionally, added ingredients accounting
    for k, v in Counter(total_ingredients).items():
        print(f'\t\t{k.name} - {v}')


if __name__ == '__main__':
    main()
