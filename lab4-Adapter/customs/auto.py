class Auto:
    def __init__(self, age: int, model: str, damaged: bool, mileage: int):
        self.age = age
        self.model = model
        self.damaged = damaged
        self.mileage = mileage

    def __str__(self):
        return f'Auto(age={self.age}, model={self.model}, damaged={self.damaged}, mileage={self.mileage})'
