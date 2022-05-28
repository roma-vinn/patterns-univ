from abc import ABC, abstractmethod
from subscriber import Subscriber


class Publisher(ABC):
    @abstractmethod
    def subscribe(self, sub: Subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, sub: Subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self, context: str):
        pass
