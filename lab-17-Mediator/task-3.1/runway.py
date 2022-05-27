class Runway:
    def __init__(self, runway_id: int):
        self._is_available = True
        self._id = runway_id

    def get_id(self):
        return self._id

    def set_is_available(self, is_available: bool):
        self._is_available = is_available

    def get_is_available(self):
        return self._is_available
