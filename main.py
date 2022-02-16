from HashMap import HashMap
from Package import Package
from Truck import Truck
import Reader

if __name__ == '__main__':
    packages = Reader.read_packages('WGUPS Package File.csv')
    locations = Reader.get_locations('WGUPS Distance Table.csv')
    distances = Reader.get_distances('WGUPS Distance Table.csv')




    # Load packages manually into truck 1; packages that need to delivery early
    truck_one = Truck()
    truck_one.add_package(packages.get(1))
    truck_one.add_package(packages.get(2))
    truck_one.add_package(packages.get(4))
    truck_one.add_package(packages.get(13))
    truck_one.add_package(packages.get(14))
    truck_one.add_package(packages.get(15))
    truck_one.add_package(packages.get(16))
    truck_one.add_package(packages.get(19))
    truck_one.add_package(packages.get(20))
    truck_one.add_package(packages.get(29))
    truck_one.add_package(packages.get(30))
    truck_one.add_package(packages.get(31))
    truck_one.add_package(packages.get(34))
    truck_one.add_package(packages.get(37))
    truck_one.add_package(packages.get(40))
    truck_one.add_package(packages.get(21))

    # Load packages manually into truck 2; packages that are delayed or only for truck 2
    truck_two = Truck()
    truck_two.add_package(packages.get(3))
    truck_two.add_package(packages.get(18))
    truck_two.add_package(packages.get(25))
    truck_two.add_package(packages.get(6))
    truck_two.add_package(packages.get(28))
    truck_two.add_package(packages.get(32))
    truck_two.add_package(packages.get(36))
    truck_two.add_package(packages.get(38))
    truck_two.add_package(packages.get(5))
    truck_two.add_package(packages.get(7))
    truck_two.add_package(packages.get(8))
    truck_two.add_package(packages.get(10))
    truck_two.add_package(packages.get(11))
    truck_two.add_package(packages.get(12))
    truck_two.add_package(packages.get(17))
    truck_two.add_package(packages.get(22))

    # Load packages manually into truck 3; packages that are wrong address and others
    truck_three = Truck()
    truck_three.add_package(packages.get(9))  # Wrong address; change to '410 S State St, Salt Lake City, UT, 84111' @ 10:20AM
    truck_three.add_package(packages.get(23))
    truck_three.add_package(packages.get(24))
    truck_three.add_package(packages.get(26))
    truck_three.add_package(packages.get(27))
    truck_three.add_package(packages.get(33))
    truck_three.add_package(packages.get(35))
    truck_three.add_package(packages.get(39))


