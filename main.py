# WGU UPS C950 Jeremy Varkey #001460735

from HashMap import HashMap
from Package import Package
from Truck import Truck
import Reader

if __name__ == '__main__':
    #  Initial display message greeting the user
    print('------WGU UPS Routing Program------')
    print('Running deliveries...')
    print('')
    packages = Reader.read_packages('WGUPS Package File.csv')
    locations = Reader.get_locations('WGUPS Distance Table.csv')
    distances = Reader.get_distances('WGUPS Distance Table.csv')

    # Load packages manually into truck 1; Leave at 9:05AM
    truck_one = Truck(1, 9.1)
    truck_one.add_package(packages.get('34'))
    truck_one.add_package(packages.get('22'))
    truck_one.add_package(packages.get('26'))
    truck_one.add_package(packages.get('24'))
    truck_one.add_package(packages.get('21'))
    truck_one.add_package(packages.get('12'))
    truck_one.add_package(packages.get('25'))
    truck_one.add_package(packages.get('6'))
    truck_one.add_package(packages.get('17'))
    truck_one.add_package(packages.get('40'))
    truck_one.add_package(packages.get('32'))

    # Load packages manually into truck 2; Primarily packages that need to arrive early; Leave at 8AM
    truck_two = Truck(2, 8)
    truck_two.add_package(packages.get('16'))
    truck_two.add_package(packages.get('13'))
    truck_two.add_package(packages.get('19'))
    truck_two.add_package(packages.get('15'))
    truck_two.add_package(packages.get('14'))
    truck_two.add_package(packages.get('20'))
    truck_two.add_package(packages.get('3'))
    truck_two.add_package(packages.get('18'))
    truck_two.add_package(packages.get('36'))
    truck_two.add_package(packages.get('31'))
    truck_two.add_package(packages.get('30'))
    truck_two.add_package(packages.get('38'))
    truck_two.add_package(packages.get('1'))
    truck_two.add_package(packages.get('37'))
    truck_two.add_package(packages.get('29'))

    # Load packages manually into truck 3; packages that are wrong address and others; Leave at 1PM to account for address change at 10:20AM
    truck_three = Truck(3, 13)
    packages.get('9').set_address('410 S State St', 'Salt Lake City', 'UT', '84111')
    truck_three.add_package(
        packages.get('9'))  # Wrong address; change to '410 S State St, Salt Lake City, UT, 84111' by 10:20AM
    truck_three.add_package(packages.get('28'))
    truck_three.add_package(packages.get('2'))
    truck_three.add_package(packages.get('33'))
    truck_three.add_package(packages.get('10'))
    truck_three.add_package(packages.get('5'))
    truck_three.add_package(packages.get('4'))
    truck_three.add_package(packages.get('8'))
    truck_three.add_package(packages.get('39'))
    truck_three.add_package(packages.get('27'))
    truck_three.add_package(packages.get('35'))
    truck_three.add_package(packages.get('23'))
    truck_three.add_package(packages.get('11'))
    truck_three.add_package(packages.get('7'))

    #  Prints total mileage of the deliveries taken for the day
    mileage = truck_one.conduct_deliveries(locations, distances) + truck_two.conduct_deliveries(locations,
                                                                                                distances) + truck_three.conduct_deliveries(locations, distances)
    print('Total mileage: {:.2f} \n'.format(mileage))

    #  Prints the results for each package data at EOD.
    #  Space-time complexity: O(N)
    delivered = []
    for package in packages.get_map():
        delivered.append(package[0][1])
    for i in delivered:
        i.print_package()

    #  Begins user input portion of program.
    #  User has three options:
    #  (1) View all packages at a particular point in [Military] time.
    #  (2) View one package at a particular point in [Military] time.
    #  (3) End program.
    user_input = 1
    while user_input != 3:
        #  Get user input and convert to int
        #  Space-time complexity: O(1)
        user_input = int(input('Please type what you would like to view next:\n'
                               '1. View all packages at a particular time. (1)\n'
                               '2. View one package at a particular time. (2)\n'
                               '3. End program. (3)\n'))

        #  If user input is for all packages at particular time, get time input and return status all packages.
        #  First convert user input from military time into a float. Then compare to each packages delivery and start time using "print_package_at_time" function.
        #  Space-time complexity O(N)
        if user_input == 1:
            try:
                user_time = input('Please input in military time (HH:MM): ')
                hours, minutes = user_time.split(':')
                hours = int(hours)
                minutes = float(int(minutes) / 60)
                converted_time = hours + minutes
                for package in delivered:
                    package.print_package_at_time(converted_time)
            except ValueError:
                print('Please input in HH:MM format.\n')

        #  If user input is for one package at a particular time, get time input and return status of one package.
        #  First convert user input from military time into a float. Then compare to the specified package delivery and start time using "print_package_at_time"function.
        #  Space-time complexity: O(1)
        elif user_input == 2:
            try:
                user_time = input('Please input in military time (HH:MM): ')
                hours, minutes = user_time.split(':')
                hours = int(hours)
                minutes = float(int(minutes) / 60)
                converted_time = hours + minutes
                user_package = int(input('Please input a package id #1 - 40: '))
                while user_package not in range(1, len(delivered) + 1):
                    user_package = int(input('Please input a package id #1 - 40: \n'))
                package = packages.get(user_package)
                package.print_package_at_time(converted_time)
            except ValueError:
                print("Please input time in HH:MM format.\n")

        #  End program.
        #  Space-time complexity: O(1)
        elif user_input == 3:
            print('Closing program...\n')
