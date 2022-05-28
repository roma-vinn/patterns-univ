from fan import Fan


def main():
    fan = Fan()

    fan.turn_up()
    fan.turn_up()
    fan.turn_down()
    fan.turn_down()
    fan.turn_up()


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Turning on: Low
    # Increasing speed: Medium
    # Decreasing speed: Low
    # Turning fan off
    # Turning on: Low
