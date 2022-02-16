import Reader

class Truck:

    def __init__(self):
        self.truck = []
        self.visited = set('4001 South 700 East')
        self.current = ''
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

    def set_status(self, status):
        self.status = status

    def add_visited(self, address):
        self.visited.add(address)

    def current_location(self, location):
        self.current = location

    def next_location(self, locations, distances):
        min_d = 500.00
        next_d = ''
        for location in locations:
            if location not in self.visited:
                if min_d < Reader.get_distance_between(locations, distances, self.current, location):
                    min_d = Reader.get_distance_between(locations, distances, self.current, location)
                    next_d = location

        self.mileage += min_d
        self.current = next_d
        self.visited.add(self.current)




