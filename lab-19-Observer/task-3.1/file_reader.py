import os
from publisher import Publisher
from subscriber import Subscriber


class FileReader(Publisher):
    def __init__(self, file_path: str):
        assert os.path.exists(file_path) and os.path.isfile(file_path), f'File {file_path} does not meet requirements'

        self._file_path = file_path
        self._finished = False

        self._subscribers: list[Subscriber] = []

    def read_by_line(self):
        with open(self._file_path, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                print(f'Read: {line}')
                self.notify_subscribers(line)

    def subscribe(self, sub: Subscriber):
        self._subscribers.append(sub)

    def unsubscribe(self, sub: Subscriber):
        self._subscribers.remove(sub)

    def notify_subscribers(self, context: str):
        for sub in self._subscribers:
            sub.update(context)
