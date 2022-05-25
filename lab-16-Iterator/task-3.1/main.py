from staff import Employee, StaffList


def main():
    zak = Employee('Zak')
    sarah = Employee('Sarah')
    anna = Employee('Anna')

    staff_list = StaffList([zak, sarah, anna])
    for employee in staff_list:
        print(employee.get_name())

    print('---')

    # or explicitly like this
    staff_iter = iter(staff_list)
    try:
        while True:
            employee = next(staff_iter)
            print(employee.get_name())
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
    # OUTPUT:
    # Zak
    # Sarah
    # Anna
    # ---
    # Zak
    # Sarah
    # Anna
