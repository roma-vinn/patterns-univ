from plane import Plane
from runway import Runway


class AirportOperator:
    def __init__(self):
        self._runways: dict[int, Runway] = {}
        self._planes_on_ground: dict[str, Plane] = {}
        self._planes_in_the_air: dict[str, Plane] = {}

    def add_plane(self, plane: Plane):
        assert plane.get_id() not in self._planes_on_ground and plane.get_id() not in self._planes_in_the_air, \
            f"Plane with ID={plane.get_id()} already registered."
        assert plane.get_runway_id() not in self._runways, f"No runway with ID={plane.get_runway_id()}"

        self._planes_on_ground[plane.get_id()] = plane
        plane.set_operator(self)

    def add_runway(self, runway: Runway):
        assert runway.get_id() not in self._runways, f'Runway with ID={runway.get_id()} already registered.'

        self._runways[runway.get_id()] = runway

    def take_off(self, plane_id: str, runway_id: int):
        if plane_id in self._planes_on_ground and self._runways[runway_id].get_is_available():
            plane = self._planes_on_ground.pop(plane_id)
            print(f'Plane {plane_id} is taking off.')
            plane.set_in_the_air(True)
            self._runways[runway_id].set_is_available(False)
            plane.set_in_the_air(True)
            self._planes_in_the_air[plane_id] = plane
        else:
            if plane_id not in self._planes_on_ground:
                print(f'Plane ID={plane_id} is already in the air.')
            if not self._runways[runway_id].get_is_available():
                print(f'Runway ID={runway_id} is not available.')
