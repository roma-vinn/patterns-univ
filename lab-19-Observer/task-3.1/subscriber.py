from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, context: str):
        pass


class MaxLenLineSubscriber(Subscriber):
    def __init__(self):
        self._max_len_line = ''

    def update(self, context: str):
        if len(context) > len(self._max_len_line):
            self._max_len_line = context

    def get_max_len_line(self):
        return self._max_len_line


class MaxLenWordSubscriber(Subscriber):
    def __init__(self):
        self._max_len_word = ''

    def update(self, context: str):
        words = context.split()
        for word in words:
            if word.isalpha() and len(word) > len(self._max_len_word):
                self._max_len_word = word

    def get_max_len_word(self):
        return self._max_len_word


class WordCounterSubscriber(Subscriber):
    def __init__(self):
        self._word_count = 0

    def update(self, context: str):
        words = context.split()
        for word in words:
            if word.isalpha():
                self._word_count += 1

    def get_word_count(self):
        return self._word_count


class LineWithLongestWordSubscriber(Subscriber):
    def __init__(self):
        self._max_len_word = ''
        self._line = ''

    def update(self, context: str):
        words = context.split()
        for word in words:
            if word.isalpha() and len(word) > len(self._max_len_word):
                self._max_len_word = word
                self._line = context

    def get_line_with_longest_word(self):
        return self._line
