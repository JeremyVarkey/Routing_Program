import datetime


class Package:

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

    def set_departure_time(self, time):
        self.departure_time = time

    def get_delivered_time(self):
        return self.delivered_time

    def set_status(self, time):
        self.delivered_time = time
        self.status = 'Delivered at: {}'.format(datetime.timedelta(hours=time)).rsplit(':', 1)[0]

    def set_address(self, address, city, state, zipcode):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def print_package(self):
        print('ID: {0} \nAddress: {1}, {2}, {3}, {4} \nWeight: {5} \nExpected Delivery: {6} \nStatus: {7}'
              .format(self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.delivery_time,
                      self.status))
        print()

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