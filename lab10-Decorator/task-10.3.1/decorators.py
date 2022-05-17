from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def show(self):
        pass


class BaseDecorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def show(self):
        self._component.show()


class PrintableString(Component):
    def __init__(self, base: str):
        self._base = base

    def show(self):
        print(self._base, end='')


class PostComaDecorator(BaseDecorator):
    def __init__(self, component: Component):
        super(PostComaDecorator, self).__init__(component)

    def show(self):
        super(PostComaDecorator, self).show()
        print(',', end='')


class PostEndlDecorator(BaseDecorator):
    def __init__(self, component: Component):
        super(PostEndlDecorator, self).__init__(component)

    def show(self):
        super(PostEndlDecorator, self).show()
        print()


class PostExclaimDecorator(BaseDecorator):
    def __init__(self, component: Component):
        super(PostExclaimDecorator, self).__init__(component)

    def show(self):
        super(PostExclaimDecorator, self).show()
        print('!', end='')


class PostWordDecorator(BaseDecorator):
    def __init__(self, component: Component, word: str):
        super(PostWordDecorator, self).__init__(component)
        self._word = word

    def show(self):
        super(PostWordDecorator, self).show()
        print(self._word, end='')


class PreWordDecorator(BaseDecorator):
    def __init__(self, component: Component, word: str):
        super(PreWordDecorator, self).__init__(component)
        self._word = word

    def show(self):
        print(self._word, end='')
        super(PreWordDecorator, self).show()
