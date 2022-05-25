from controller import Controller
from device import TV, Radio


def main():
    tv = TV()
    radio = Radio()

    controller_tv = Controller(target=tv)
    controller_radio = Controller(target=radio)

    controller_universal = Controller(target=[tv, radio])

    # controller.deviceOn();
    #
    #         for (int i = 0; i < 30; i++) {
    #             controller.deviceNextChanel();
    #         }
    #         controller.deviceVolumeUp();
    #
    #         controller.deviceVolumeUp();
    #         controller.deviceVolumeUp();
    #
    #         controller.devicePrevChanel();
    #
    #         controller.deviceVolumeDown();
    #
    #         controller.deviceOff();

    controller_tv.device_on()
    for _ in range(10):
        controller_tv.device_next_channel()

    controller_tv.device_volume_up()
    controller_tv.device_volume_up()
    controller_tv.device_volume_up()

    controller_radio.device_next_channel()  # won't work

    controller_tv.device_prev_channel()
    controller_tv.device_volume_down()

    controller_radio.device_on()

    for _ in range(5):
        controller_radio.device_volume_down()
    controller_radio.device_next_channel()

    controller_universal.device_off()


if __name__ == '__main__':
    main()
    # OUTPUT:
    # TV is on.
    # TV channel = 2
    # TV channel = 3
    # TV channel = 4
    # TV channel = 5
    # TV channel = 6
    # TV channel = 7
    # TV channel = 8
    # TV channel = 9
    # TV channel = 10
    # TV channel = 11
    # TV volume = 51
    # TV volume = 52
    # TV volume = 53
    # TV channel = 10
    # TV volume = 52
    # Radio is on.
    # Radio volume = 49
    # Radio volume = 48
    # Radio volume = 47
    # Radio volume = 46
    # Radio volume = 45
    # Radio channel = 2
    # TV is off.
    # Radio is off.
