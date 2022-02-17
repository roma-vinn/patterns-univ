from transport import Bus, Tram, Trolleybus


class SkodaBus(Bus):
    def __init__(self):
        super(SkodaBus, self).__init__(4_500_000, 25)

    def go_by_way(self):
        print('Skoda Bus runs!')


class VolvoBus(Bus):
    def __init__(self):
        super(VolvoBus, self).__init__(6_000_000, 20)

    def go_by_way(self):
        print('Volvo Bus runs!')


class SkodaTram(Tram):
    def __init__(self):
        super(SkodaTram, self).__init__(9_000_000, 8)

    def go_by_rails(self):
        print('Skoda Tram goes!')


class VolvoTram(Tram):
    def __init__(self):
        super(VolvoTram, self).__init__(10_000_000, 7)

    def go_by_rails(self):
        print('Volvo Tram goes!')


class SkodaTrolley(Trolleybus):
    def __init__(self):
        super(SkodaTrolley, self).__init__(6_800_000, 13)

    def go_by_contact_network(self):
        print('Skoda trolleybus goes!')


class VolvoTrolley(Trolleybus):
    def __init__(self):
        super(VolvoTrolley, self).__init__(7_000_000, 13)

    def go_by_contact_network(self):
        print('Volvo trolleybus goes!')
