from airport_operator import AirportOperator
from runway import Runway
from plane import Plane


def main():
    runway1 = Runway(runway_id=1)
    runway2 = Runway(runway_id=2)

    plane1 = Plane(plane_id="ABC1", runway_id=runway1.get_id())
    plane2 = Plane(plane_id="ABC2", runway_id=runway2.get_id())
    plane3 = Plane(plane_id="ABC3", runway_id=runway2.get_id())

    operator = AirportOperator()

    operator.add_plane(plane1)
    operator.add_plane(plane2)
    operator.add_plane(plane3)

    operator.add_runway(runway1)
    operator.add_runway(runway2)

    plane1.take_off()
    plane2.take_off()
    plane3.take_off()


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Plane ABC1 is taking off.
    # Plane ABC2 is taking off.
    # Runway ID=2 is not available.
