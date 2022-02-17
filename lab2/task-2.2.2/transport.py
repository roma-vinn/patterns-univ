from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, cost, usage_cost):
        self._cost = cost
        self._usage_cost = usage_cost

    @property
    def cost(self):
        return self._cost

    @property
    def usage_cost(self):
        return self._usage_cost


class Tram(Transport):
    @abstractmethod
    def go_by_rails(self):
        pass


class Bus(Transport):
    @abstractmethod
    def go_by_way(self):
        pass


class Trolleybus(Transport):
    @abstractmethod
    def go_by_contact_network(self):
        pass
