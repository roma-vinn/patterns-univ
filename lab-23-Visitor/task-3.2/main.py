from military import GeneralStaff, MilitaryBase
from spy import SecretAgent, Saboteur


def main():
    generalStaff = GeneralStaff(20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    print(militaryBase)

    print('-' * 80)

    secret_agent = SecretAgent()
    saboteur = Saboteur()

    generalStaff.accept(secret_agent)
    militaryBase.accept(secret_agent)

    print(generalStaff)
    print(militaryBase)

    print('-' * 80)

    generalStaff.accept(saboteur)
    militaryBase.accept(saboteur)

    print(generalStaff)
    print(militaryBase)


if __name__ == '__main__':
    main()
    # OUTPUT:
    # GeneralStaff: 20 generals and 100 secret papers.
    # MilitaryBase: 10 officers, 1000 soldiers, 300 jeeps and 20 tanks.
    # --------------------------------------------------------------------------------
    # Secret Agent counted 20 generals and copied all 100 secret papers.
    # Secret agent counted 10 officers, 1000 soldiers, 300 jeeps and 20 tanks on the military base.
    # GeneralStaff: 20 generals and 100 secret papers.
    # MilitaryBase: 10 officers, 1000 soldiers, 300 jeeps and 20 tanks.
    # --------------------------------------------------------------------------------
    # Saboteur destroyed at most 10 out of 100 secret papers.
    # Saboteur destroyed at most 5 out of 300 jeeps and at most 1 of 20 tank.
    # GeneralStaff: 20 generals and 90 secret papers.
    # MilitaryBase: 10 officers, 1000 soldiers, 295 jeeps and 19 tanks.
