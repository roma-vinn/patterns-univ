from pizza_builder import PizzaBuilder
from pizzaiolo import Pizzaiolo


def main():
    pizzaiolo = Pizzaiolo()
    pizzaiolo.set_pizza_builder(PizzaBuilder())

    margarita = pizzaiolo.cook_Margarita()
    print(f"Margarita: {margarita}")
    print(f"Cost: {margarita.cost}")

    pizzaiolo2 = Pizzaiolo()
    print("Same pizzaiolo:", hash(pizzaiolo) == hash(pizzaiolo2))

    peperoni = pizzaiolo2.cook_Peperoni()
    print(f"Peperoni: {peperoni}")
    print(f"Cost: {peperoni.cost}")

    hawaiian = pizzaiolo2.cook_Hawaiian()
    print(f"Hawaiian: {hawaiian}")
    print(f"Cost: {hawaiian.cost}")


if __name__ == '__main__':
    main()
