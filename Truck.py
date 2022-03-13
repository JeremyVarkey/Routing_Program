import Reader
import datetime
from Package import Package


class Truck:

    def __init__(self, id, time):
        self.truck_id = id
        self.truck = []
        self.delivered = []
        self.visited = ['4001 South 700 East']
        self.current = '4001 South 700 East'
        self.speed = 18
        self.mileage = 0
        self.capacity = 16
        self.status = 'In Hub'
        self.time_elapsed = 0.0
        self.time_start = time

    def get_time(self):
        return self.time_start + self.time_elapsed

    def add_package(self, package):
        if len(self.truck) < self.capacity:
            self.truck.append(package)
        else:
            print("No more space in the truck!")

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

    def deliver_packages(self):
        to_delete = []
        for package in self.truck:
            if self.current == package.get_address():
                time = self.time_elapsed + self.time_start
                package.set_status('Delivered at: {}'.format(datetime.timedelta(hours=time)).rsplit(':', 1)[0])
                to_delete.append(package)
                self.delivered.append(package)
        for package in to_delete:
            self.truck.remove(package)

    def get_current(self):
        return self.current

    #  finds and travels to the next unvisited location
    def next_location(self, locations, distances):
        min_d = 500.00
        next_d = ''
        for location in locations:
            if location not in self.visited:
                if min_d > Reader.get_distance_between(locations, distances, self.current, location):
                    min_d = Reader.get_distance_between(locations, distances, self.current, location)
                    next_d = location

        self.visited.append(next_d)
        self.current = next_d
        self.time_elapsed += min_d / self.speed
        self.mileage += min_d

    def conduct_deliveries(self, locations, distances):
        while len(self.truck) >= 1:
            self.next_location(locations, distances)
            self.deliver_packages()

        if self.truck_id == 1:
            self.mileage += Reader.get_distance_between(locations, distances, self.current, '4001 South 700 East')
            self.current = '4001 South 700 East'
        return self.mileage
