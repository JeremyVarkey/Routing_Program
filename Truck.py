import Reader
from Package import Package


class Truck:

    def __init__(self):
        self.truck = []
        self.visited = ['4001 South 700 East']
        self.current = '4001 South 700 East'
        self.speed = 18
        self.mileage = 0
        self.capacity = 16
        self.status = 'In Hub'

    def add_package(self, package):
        if len(self.truck) < self.capacity:
            self.truck.append(package)
        else:
            print("No more space in the truck!")

    def remove_package(self, package):
        self.truck.remove(package)

    def add_miles(self, miles):
        self.mileage += miles
        # implement an if statement to take into account if there is not packages left to return to Hub

    def set_status(self, status):
        self.status = status

    def add_visited(self, address):
        self.visited.append(address)

    def set_location(self, location):
        self.current = location

    def list_packages(self):
        for package in self.truck:
            package.print_package()

    #delivers one package; returns NoneType if no package delivered
    def deliver_package(self):
        for package in self.truck:
            if self.current == package.get_address():
                package.set_status('Delivered')
                self.remove_package(package)
                return package
        return None

    def get_current(self):
        return self.current

    #  finds (but does not travel to) the next unvisited location
    def next_location(self, locations, distances):
        min_d = 500.00
        next_d = ''
        for location in locations:
            if location not in self.visited:
                if min_d > Reader.get_distance_between(locations, distances, self.current, location):
                    min_d = Reader.get_distance_between(locations, distances, self.current, location)
                    next_d = location

        return next_d
