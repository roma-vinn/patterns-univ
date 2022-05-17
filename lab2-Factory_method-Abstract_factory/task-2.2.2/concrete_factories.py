from concrete_transport import SkodaBus, SkodaTram, SkodaTrolley, VolvoBus, VolvoTram, VolvoTrolley
from transport_factory import TransportFactory


class SkodaFactory(TransportFactory):
    """Concrete factory for Skoda"""
    def create_bus(self) -> SkodaBus:
        return SkodaBus()

    def create_tram(self) -> SkodaTram:
        return SkodaTram()

    def create_trolleybus(self) -> SkodaTrolley:
        return SkodaTrolley()


class VolvoFactory(TransportFactory):
    """Concrete factory for Volvo"""
    def create_bus(self) -> VolvoBus:
        return VolvoBus()

    def create_tram(self) -> VolvoTram:
        return VolvoTram()

    def create_trolleybus(self) -> VolvoTrolley:
        return VolvoTrolley()
