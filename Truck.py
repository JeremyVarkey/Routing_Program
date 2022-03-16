import Reader
import datetime
from Package import Package


#  Truck class which will track the truck id, the packages loaded into the truck (max of 16), the packages delivered from the truck
#  The locations visited by the truck, the current location of the truck, speed (fixed at 18), cumulative mileage, status, start time, and elapsed time
class Truck:

    #  Constructor
    # Space-time complexity: O(1)
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

    #  Return start time
    #  Space-time complexity: O(1)
    def get_start_time(self):
        return self.time_start

    #  Return the current time for the truck
    #  Space-time complexity: O(1)
    def get_time(self):
        return self.time_start + self.time_elapsed

    #  Add package to the truck
    #  Space-time complexity: O(1)
    def add_package(self, package):
        if len(self.truck) < self.capacity:
            self.truck.append(package)
        else:
            print("No more space in the truck!")

    #  Add miles to the mileage of the truck
    #  Space-time complexity: O(1)
    def add_miles(self, miles):
        self.mileage += miles

    #  Set status of the truck
    #  Space-time complexity: O(1)
    def set_status(self, status):
        self.status = status

    #  Add an address to the visited list
    #  Space time complexity: O(1)
    def add_visited(self, address):
        self.visited.append(address)

    #  Set the current location of the truck
    #  Space time complexity: O(1)
    def set_location(self, location):
        self.current = location

    #  print all packages in the truck currently
    #  Space time complexity: O(N)
    def list_packages(self):
        for package in self.truck:
            package.print_package()

    #  Delivers all packages in the truck whose address matches the current address
    #  Space time Complexity: O(N)
    def deliver_packages(self):
        to_delete = []

        #  Checks every package in the truck and moves to the to delete list if there is a match. Sets delivery time of package if delivered.
        #  Space time complexity: O(N)
        for package in self.truck:
            if self.current == package.get_address():
                package.set_status(self.get_time())
                to_delete.append(package)
                self.delivered.append(package)

        #  Removes packages from truck if delivered
        #  Space time complexity: O(N)
        for package in to_delete:
            self.truck.remove(package)

    #  Gets current location of truck
    #  Space time complexity: O(1)
    def get_current(self):
        return self.current

    #  Formats time from float to military time (HH:MM)
    #  Space time complexity: O(1)
    def format_time(self, time):
        return format(datetime.timedelta(hours=time)).rsplit(':', 1)[0]

    #  finds and travels to the next unvisited location; utilizes nearest neighbor algorithm
    #  Space time complexity: O(N^2)
    def next_location(self, locations, distances):
        min_d = 500.00
        next_d = ''

        #  Nearest Neighbor algorithm; for each locations in the locations list, check to see if it has been visited. If unvisited, see if it is a lower distance than the minimum distance.
        #  Space time complexity: O(N^2)
        for location in locations:
            if location not in self.visited:
                if min_d > Reader.get_distance_between(locations, distances, self.current, location):
                    min_d = Reader.get_distance_between(locations, distances, self.current, location)
                    next_d = location

        #  Once a location has been found, add it to the visited list and travel to the destination, incrementing both time and mileage
        #  Space time complexity: O(1)
        self.visited.append(next_d)
        self.current = next_d
        self.time_elapsed += min_d / self.speed
        self.mileage += min_d

    #  Unifying function to simulate truck deliveries through entire day; function stops when all packages are emptied from truck
    #  Space time complexity: O(N)
    def conduct_deliveries(self, locations, distances):

        #  Sets each package's in truck departure time to departure time given to truck
        #  Space time complexity: O(N)
        for i in self.truck:
            i.set_departure_time(self.time_start)

        #  While there are packages in the truck, move to the next location, and deliver packages for current destination
        #  Space time complexity: O(N^2) [since the functions iterate through locations list, and then packages list]
        while len(self.truck) >= 1:
            self.next_location(locations, distances)
            self.deliver_packages()

        #  The truck that leaves the earliest returns to the hub at the end of deliveries so that Truck 3 can leave.
        #  Space time complexity: O(1)
        if self.truck_id == 2:
            self.mileage += Reader.get_distance_between(locations, distances, self.current, '4001 South 700 East')
            self.current = '4001 South 700 East'

        print('Truck {} completed deliveries from {} to {} in {:.2f} miles.\n'.format(self.truck_id,
                                                                                      self.format_time(self.time_start),
                                                                                      self.format_time(self.get_time()),
                                                                                      self.mileage))
        return self.mileage
