class Truck:

    def __init__(self):
        self.truck = []
        self.speed = 18
        self.mileage = 0
        self.capacity = 16
        self.status = 'In Hub'

    def add_package(self, package):
        self.truck.append(package)

    def remove_package(self, package):
        self.truck.remove(package)

    def add_miles(self, miles):
        self.mileage += miles

    def set_status(self, status):
        self.status = status
