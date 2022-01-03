class Package:

    def __init__(self, id='', address='', city='', zipcode='', delivery_time='', weight='', notes=''):
        self.id = id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.delivery_time = delivery_time
        self.weight = weight
        self.notes = notes
        self.status = 'Not Delivered.'

    def set_status(self, time):
        self.status = 'Delivered at {0}.'.format(time)

    def set_delivery_time(self, time):
        self.delivery_time = time

