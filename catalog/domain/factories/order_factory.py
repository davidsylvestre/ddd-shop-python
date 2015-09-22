from catalog.domain.repositories.client_repository import ClientRepository
from catalog.domain.repositories.product_repository import ProductRepository
from catalog.domain.entities.order import Order


class OrderFactory(object):

    @classmethod
    def create(cls, client_id, product_id):

        client = ClientRepository().get(client_id)
        product = ProductRepository().get(product_id)

        if client is None:
            raise Exception('...')

        if product is None:
            raise Exception('...')

        # ... OUTRAS REGRAS AQUI

        return Order(product, client)
