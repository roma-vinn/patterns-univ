class Lamp:
    def __init__(self, name='default'):
        self._name = name
        self._is_light_on = False

    def light_on(self):
        if self._is_light_on:
            return
        print(f'{self._name}: Light is on')
        self._is_light_on = True

    def light_off(self):
        if not self._is_light_on:
            return
        print(f'{self._name}: Light is off')
        self._is_light_on = False
