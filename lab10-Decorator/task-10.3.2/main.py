from beverages import Espresso, DarkRoast, Decaf
from toppings import Milk, Cream, SourCream, Sugar


def main():
    bev1 = Sugar(Sugar(Espresso()))
    print(f'{bev1.description() = }, {bev1.cost() = }\n')

    bev2 = Sugar(Sugar(SourCream(DarkRoast())))
    print(f'{bev2.description() = }, {bev2.cost() = }\n')

    bev3 = Sugar(Cream(Espresso()))
    print(f'{bev3.description() = }, {bev3.cost() = }\n')

    bev4 = Sugar(Sugar(Milk(Decaf())))
    print(f'{bev4.description() = }, {bev4.cost() = }\n')


if __name__ == '__main__':
    main()
    # bev1.description() = 'Espresso + sugar + sugar', bev1.cost() = 14
    #
    # bev2.description() = 'Dark Roast + sour cream + sugar + sugar', bev2.cost() = 14
    #
    # bev3.description() = 'Espresso + cream + sugar', bev3.cost() = 18
    #
    # bev4.description() = 'Decaf + milk + sugar + sugar', bev4.cost() = 23
    #
