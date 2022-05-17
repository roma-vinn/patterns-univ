from abc import ABC, abstractmethod
from transport import Bus, Tram, Trolleybus


class TransportFactory(ABC):
    """Abstract transport factory"""
    @abstractmethod
    def create_bus(self) -> Bus:
        pass

    @abstractmethod
    def create_tram(self) -> Tram:
        pass

    @abstractmethod
    def create_trolleybus(self) -> Trolleybus:
        pass
