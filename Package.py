class Package:

    def __init__(self, id='', address='', city='', state='', zipcode='', delivery_time='', weight='', notes=''):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_time = delivery_time
        self.weight = weight
        self.notes = notes
        self.status = 'Not Delivered.'

    def set_status(self, time):
        self.status = 'Delivered at {0}.'.format(time)

    def set_address(self, address, city, state, zipcode):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def set_delivery_time(self, time):
        self.delivery_time = time

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def print_package(self):
        print('ID: {0} \nAddress: {1}, {2}, {3}, {4} \nWeight: {5} \nExpected Delivery: {6} \nStatus: {7}'
              .format(self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.delivery_time, self.status))
        print()

