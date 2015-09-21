class Order(object):

    def __init__(self, product, client):
        self.product_id = product.id
        self.client_id = client.id
        self.price = product.price
