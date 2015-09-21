from django.views.generic import View
from django.shortcuts import render

from decimal import Decimal

from catalog.domain.entities.product import Product
from catalog.domain.entities.order import Order
from catalog.domain.entities.client import Client
from catalog.domain.repositories.product_repository import ProductRepository
from catalog.domain.repositories.order_repository import OrderRepository


class OrderView(View):

    def get(self, request):
        repository = OrderRepository()
        orders = repository.all()
        return render(request, 'order/list.html', {'orders': orders})

    def post(self, request):

        # INFRA
        client = Client(129182942, 'Joao', 'Silva')

        product = ProductRepository().get(request.POST['product_id'])

        # DOMAIN
        order = Order(product, client)

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
