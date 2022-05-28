from abc import ABC, abstractmethod


class Enemy(ABC):
    def defend(self):  # Template method
        self.pick_up_weapon()
        self.defense_action()
        self.move_to_safety()
        print()

    @abstractmethod
    def pick_up_weapon(self):
        pass

    @abstractmethod
    def move_to_safety(self):
        pass

    @abstractmethod
    def defense_action(self):
        pass


class Troll(Enemy):
    def pick_up_weapon(self):
        print('Pick up club')

    def move_to_safety(self):
        print('Return to mountains')

    def defense_action(self):
        print('Defend with club')


class Pirate(Enemy):
    def pick_up_weapon(self):
        print('Pick up sword')

    def move_to_safety(self):
        print('Return to the ship')

    def defense_action(self):
        print('Defend with sword')
