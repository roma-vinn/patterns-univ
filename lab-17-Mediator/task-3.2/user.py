from abc import ABC, abstractmethod
from groups import Groups


class _User(ABC):
    @abstractmethod
    def send_message(self, message: str, user_to: str):
        pass

    @abstractmethod
    def send_message_all(self, message: str):
        pass

    @abstractmethod
    def send_message_group(self, message: str, group: str):
        pass

    @abstractmethod
    def receive_message(self, message: str, user_from: str):
        pass


class User(_User):
    def __init__(self, name: str, username: str, group=Groups.User):
        self._name = name
        self._username = username
        self._group = group
        self._chat = None

    def _check_chat(self):
        assert self._chat is not None, 'Chat must be assigned before chatting'

    def set_chat(self, chat):
        self._chat = chat

    @property
    def username(self):
        return self._username

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    def send_message(self, message: str, user_to: str):
        self._check_chat()
        self._chat.send_message(message, self._username, user_to)

    def send_message_all(self, message: str):
        self._check_chat()
        self._chat.send_message_all(message, self._username)

    def send_message_group(self, message: str, group: str):
        self._check_chat()
        self._chat.send_message_group(message, self._username, group)

    def receive_message(self, message: str, user_from: str):
        self._check_chat()
        print(f'{str(self)} received message from {user_from}:\n\t"{message}"')

    def __str__(self):
        return f'{self._username}[group={self._group}]'
