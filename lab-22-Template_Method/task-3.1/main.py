from enemy import Troll, Pirate


def main():
    pirate = Pirate()
    pirate.defend()

    troll = Troll()
    troll.defend()


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Pick up sword
    # Defend with sword
    # Return to the ship
    #
    # Pick up club
    # Defend with club
    # Return to mountains
