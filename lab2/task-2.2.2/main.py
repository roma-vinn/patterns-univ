from concrete_factories import SkodaFactory, VolvoFactory
from transport_factory import TransportFactory
from transport import Transport


def main():
    costs = {}
    for company in ['skoda', 'volvo']:
        costs[company] = calc_cost(company)
        print(f'For company {company} cost: {costs[company]}')

    print()
    print(f"Optimal company is {min(costs.items(), key=lambda x: x[1])[0]}")


def calc_cost(company: str):
    a = 10  # number of Buses
    t = 5  # number of Trams
    tr = 40  # number of Trolleybuses
    n = 200_000  # expected usage in km

    transport_list: 'list[Transport]' = []

    if company.lower() == 'skoda':
        factory: TransportFactory = SkodaFactory()
    elif company.lower() == 'volvo':
        factory: TransportFactory = VolvoFactory()
    else:
        raise ValueError(f"Incorrect company. Should be one of ['skoda', 'volvo'], got: {company.lower()}")

    for _ in range(a):
        transport_list.append(factory.create_bus())

    for _ in range(t):
        transport_list.append(factory.create_tram())

    for _ in range(tr):
        transport_list.append(factory.create_trolleybus())

    return sum([transport.cost + n * transport.usage_cost for transport in transport_list])


if __name__ == '__main__':
    main()
