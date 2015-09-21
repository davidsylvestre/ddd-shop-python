from address import Address


class Client(object):

    def __init__(self, social_number, name, last_name):
        self.social_number = social_number
        self.name = Name(name, last_name)
        self.shipping_address = None

    def new_shipping_address(self, street, number, city):
        self.shipping_address = Address(street, number, city)

    @property
    def vip(self):
        # ...
        # logic to determine if client is vip
        return True


class Name(object):  # value object

    def __init__(self, first, last, prefix='Sr'):
        self.first = first
        self.last = last
        self.prefix = prefix

    @property
    def full(self):
        return self.name + self.last_name
