from decimal import Decimal

from django.views.generic import View
from django.shortcuts import render

from ddd_shop_python.libs.domain_event import DomainEvents

from catalog.domain.entities.product import Product
from catalog.domain.repositories.order_repository import OrderRepository
from catalog.domain.repositories.product_repository import ProductRepository
from catalog.domain.events.order_completed import OrderCompleted
from catalog.domain.factories.order_factory import OrderFactory


class OrderView(View):

    def get(self, request):
        repository = OrderRepository()
        orders = repository.all()
        return render(request, 'order/list.html', {'orders': orders})

    def post(self, request):

        client_id = 1  # FAKE
        product_id = request.POST['product_id']

        order = OrderFactory.create(client_id, product_id)

        OrderRepository().save(order)

        return render(request, 'order/done.html')


class ProductView(View):

    def get(self, request):
        return render(request, 'product/new.html')

    def post(self, request):

        name = request.POST['name']
        description = request.POST['description']
        price = Decimal(request.POST['price'])

        product = Product(name, description, price)

        repository = ProductRepository()
        repository.save(product)

        return render(request, 'product/new.html')


class CatalogView(View):

    def get(self, request):

        products = ProductRepository().all()

        return render(request, 'catalog/catalog_home.html', {'products': products})
