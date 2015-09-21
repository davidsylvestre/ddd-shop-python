from mapper.object_mapper import ObjectMapper

from catalog.models import OrderData
from catalog.domain.entities.order import Order


class OrderRepository(object):

    def __init__(self):
        self.mapper = ObjectMapper()
        self.mapper.create_map(Order, OrderData)

    def all(self):
        return OrderData.objects.all()

    def save(self, order):
        order_data = self.mapper.map(order, OrderData)
        order_data.save()
