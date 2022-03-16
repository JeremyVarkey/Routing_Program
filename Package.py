import datetime

#  Package class is used to store package data, such as package id, address, city, state, zipcode, estimated delivery time, status, weight, and additional notes
class Package:

    #  Constructor; in addition to variables that assign based on inputs from accompanying CSV, stores inputs for departure time, delivery time, and status
    #  Space time complexity: O(1)
    def __init__(self, id='', address='', city='', state='', zipcode='', delivery_time='', weight='', notes=''):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_time = delivery_time
        self.departure_time = 0.0
        self.delivered_time = 0.0
        self.weight = weight
        self.notes = notes
        self.status = 'En Route'

    #  Sets departure time to input
    #  Space time complexity: O(1)
    def set_departure_time(self, time):
        self.departure_time = time

    #  Returns delivered time
    #  Space time complexity: O(1)
    def get_delivered_time(self):
        return self.delivered_time

    #  Sets the status of the package according to the time delivered
    #  Space time complexity: O(1)
    def set_status(self, time):
        self.delivered_time = time
        self.status = 'Delivered at: {}'.format(datetime.timedelta(hours=time)).rsplit(':', 1)[0]

    #  Sets address of the package
    #  Space time complexity: O(1)
    def set_address(self, address, city, state, zipcode):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    #  Gets id of package
    #  Space time complexity: O(1)
    def get_id(self):
        return self.id

    #  Gets address of the package
    #  Space time complexity: O(1)
    def get_address(self):
        return self.address

    #  Prints the contents of package
    #  Space time complexity: O(1)
    def print_package(self):
        print('ID: {0} \nAddress: {1}, {2}, {3}, {4} \nWeight: {5} \nExpected Delivery: {6} \nStatus: {7}'
              .format(self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.delivery_time,
                      self.status))
        print()

    #  Print contents of package at a given time, with the status of the package depending on the specified time, delivery time, and departure time
    #  Space time complexity: O(1)
    def print_package_at_time(self, time):
        if time < self.departure_time and time < self.delivered_time:
            print('ID: {0} \nAddress: {1}, {2}, {3}, {4} \nWeight: {5} \nExpected Delivery: {6} \nStatus: {7}'
                  .format(self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.delivery_time,
                          'In Hub'))
            print()
        elif self.departure_time < time < self.delivered_time:
            print('ID: {0} \nAddress: {1}, {2}, {3}, {4} \nWeight: {5} \nExpected Delivery: {6} \nStatus: {7}'
                  .format(self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.delivery_time,
                          'En Route'))
            print()
        else:
            print('ID: {0} \nAddress: {1}, {2}, {3}, {4} \nWeight: {5} \nExpected Delivery: {6} \nStatus: {7}'
                  .format(self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.delivery_time,
                          self.status))
            print()