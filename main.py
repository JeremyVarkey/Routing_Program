from HashMap import HashMap
from Package import Package
from Truck import Truck
import Reader

if __name__ == '__main__':
    packages = Reader.read_packages('WGUPS Package File.csv')
    locations = Reader.get_locations('WGUPS Distance Table.csv')
    distances = Reader.get_distances('WGUPS Distance Table.csv')
    mileage = 0.0


    # Load packages manually into truck 1; packages that need to delivery early; Leave at 8AM
    truck_one = Truck(1, 8)
    truck_one.add_package(packages.get('1'))
    truck_one.add_package(packages.get('13'))
    truck_one.add_package(packages.get('14'))
    truck_one.add_package(packages.get('15'))
    truck_one.add_package(packages.get('16'))
    truck_one.add_package(packages.get('20'))
    truck_one.add_package(packages.get('29'))
    truck_one.add_package(packages.get('30'))
    truck_one.add_package(packages.get('31'))
    truck_one.add_package(packages.get('34'))
    truck_one.add_package(packages.get('37'))
    truck_one.add_package(packages.get('40'))
    truck_one.add_package(packages.get('19'))
    truck_one.add_package(packages.get('27'))
    truck_one.add_package(packages.get('35'))

    # Load packages manually into truck 2; packages that are delayed or only for truck 2; Leave at 9:05AM
    truck_two = Truck(2, 9.1)
    truck_two.add_package(packages.get('6'))
    truck_two.add_package(packages.get('25'))
    truck_two.add_package(packages.get('18'))
    truck_two.add_package(packages.get('36'))
    truck_two.add_package(packages.get('3'))
    truck_two.add_package(packages.get('38'))
    truck_two.add_package(packages.get('28'))
    truck_two.add_package(packages.get('6'))
    truck_two.add_package(packages.get('32'))
    truck_two.add_package(packages.get('2'))
    truck_two.add_package(packages.get('33'))


    # Load packages manually into truck 3; packages that are wrong address and others; Leave when a truck comes to hub
    truck_three = Truck(3, 13)
    packages.get('9').set_address('410 S State St', 'Salt Lake City', 'UT', '84111')
    truck_three.add_package(packages.get('9'))  # Wrong address; change to '410 S State St, Salt Lake City, UT, 84111' @ 10:20AM
    truck_three.add_package(packages.get('7'))
    truck_three.add_package(packages.get('39'))
    truck_three.add_package(packages.get('11'))
    truck_three.add_package(packages.get('8'))
    truck_three.add_package(packages.get('17'))
    truck_three.add_package(packages.get('12'))
    truck_three.add_package(packages.get('21'))
    truck_three.add_package(packages.get('4'))
    truck_three.add_package(packages.get('5'))
    truck_three.add_package(packages.get('24'))
    truck_three.add_package(packages.get('23'))
    truck_three.add_package(packages.get('26'))
    truck_three.add_package(packages.get('10'))
    truck_three.add_package(packages.get('21'))
    truck_three.add_package(packages.get('22'))

    mileage += truck_one.conduct_deliveries(locations, distances)
    mileage += truck_two.conduct_deliveries(locations, distances)
    mileage += truck_three.conduct_deliveries(locations, distances)
    print(mileage)

    delivered = []
    for package in packages.get_map():
        delivered.append(package[0][1])

    for i in delivered:
        i.print_package()

    print(mileage)