from mapper.object_mapper import ObjectMapper

from catalog.models import ProductData
from catalog.domain.entities.product import Product


class ProductRepository(object):

    def __init__(self):
        self.mapper = ObjectMapper()
        self.mapper.create_map(Product, ProductData)

    def save(self, product):
        product_data = self.mapper.map(product, ProductData)
        product_data.save()

    def all(self):
        return ProductData.objects.all()
