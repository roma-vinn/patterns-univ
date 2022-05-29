from employee import Manager, SalesPerson, StaffList, ITSupport
from visitor import RaiseVisitor, FineVisitor


def main():
    staff_list = StaffList()

    staff_list.add_employee(Manager(60_000))
    staff_list.add_employee(SalesPerson(50_000))
    staff_list.add_employee(ITSupport(40_000))

    print(f'Total amount paid to staff: {staff_list.get_salary()}')

    staff_list.accept(RaiseVisitor(10))
    print(f'Total amount paid to staff: {staff_list.get_salary()}')

    staff_list.accept(FineVisitor(1000))
    print(f'Total amount paid to staff: {staff_list.get_salary()}')


if __name__ == '__main__':
    main()
