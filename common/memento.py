class Originator:
    _state = ""

    @property
    def state(self):
        return self._state

    class Memento:
        _state = ""

        def __init__(self, state):
            self._state = state

        @property
        def state(self):
            return self._state

    def save(self):
        return Originator.Memento(self.state)

    def restore(self, memento: Memento):
        self._state = memento.state
