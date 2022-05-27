from abc import ABC, abstractmethod
from user import User
from groups import Groups


class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user_from: str, user_to: str):
        pass

    @abstractmethod
    def send_message_all(self, message: str, user_from: str):
        pass

    @abstractmethod
    def send_message_group(self, message: str, user_from: str, group: str):
        pass


class Chat(Mediator):
    def __init__(self):
        self._users: dict[str, User] = {}
        self._groups_dict: dict[str, set[User]] = {
            group.value: set() for group in Groups
        }

    def add_user(self, user: User):
        self._users.setdefault(user.username, user)
        self._groups_dict[user.group.value].add(user)
        user.set_chat(self)

    def add_users(self, users: list[User]):
        for user in users:
            self.add_user(user)

    def send_message(self, message: str, user_from: str, user_to: str):
        if user_from != user_to:
            receiver = self._users.get(user_to)
            receiver.receive_message(message, user_from)

    def send_message_all(self, message: str, user_from: str):
        for receiver in self._users.values():
            if receiver.username == user_from:
                continue
            receiver.receive_message(message, user_from)

    def send_message_group(self, message: str, user_from: str, group: str):
        for receiver in self._groups_dict[group]:
            if receiver.username == user_from:
                continue
            receiver.receive_message(message, user_from)
