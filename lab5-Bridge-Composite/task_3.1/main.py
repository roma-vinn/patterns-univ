from beverages import Coffee, Tea, Chocolate
from toppings import Milk, ExtraCoffee, ExtraHotWater
from servings import TakeOut, Delivery


def main():
    coffee = Coffee(topping=ExtraCoffee(1))
    coffee.prepare()
    coffee.drink()
    print(f'{coffee.cost() = }')
    print()

    tea = Tea(sugar=1, topping=Milk(100))
    tea.prepare()
    tea.drink()
    print(f'{tea.cost() = }')
    print()

    chocolate = Chocolate(topping=ExtraHotWater(50))
    chocolate.prepare()
    chocolate.drink()
    print(f'{chocolate.cost() = }')
    print()

    # Additional: added serving (in cafe, take-out and delivery)
    tea_takeout = Tea(sugar=2, serving=TakeOut())
    tea_takeout.prepare()
    tea_takeout.drink()
    print(f'{tea_takeout.cost() = }')
    print()

    coffee_delivery = Tea(sugar=1, topping=Milk(150), serving=Delivery('Khreshchatyk, 1'))
    coffee_delivery.prepare()
    coffee_delivery.drink()
    print(f'{coffee_delivery.cost() = }')
    print()


if __name__ == '__main__':
    main()

    # Preparing:
    # 	Pouring some coffee
    # 	Putting some extra coffee: 1portion
    # Drinking coffee with extra coffee in cafe
    # coffee.cost() = 15
    #
    # Preparing:
    # 	Pouring some tea
    # 	Putting some milk: 100ml
    # 	Adding sugar: 1 pieces
    # Drinking tea with milk in cafe
    # tea.cost() = 12
    #
    # Preparing:
    # 	Pouring some chocolate
    # 	Putting some extra hot water: 50ml
    # Drinking chocolate with extra hot water in cafe
    # chocolate.cost() = 15
    #
    # Preparing:
    # 	Pouring some tea
    # 	Adding sugar: 2 pieces
    # Taking tea as take-out
    # tea_takeout.cost() = 10
    #
    # Preparing:
    # 	Pouring some tea
    # 	Putting some milk: 150ml
    # 	Adding sugar: 1 pieces
    # Taking tea with milk as delivery to Khreshchatyk, 1
    # coffee_delivery.cost() = 54
