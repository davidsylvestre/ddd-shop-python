class Order(object):

    def __init__(self, product, client):
        self.product_id = product.id
        self.client_id = client.social_number
        self.price = product.price

        if client.vip:
            self.price = self.give_discount()

    def give_discount(self):
        self.price -= self.price * 0.09
        return self.price

    def cancel():
        pass
        # .....
