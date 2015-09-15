from django.views.generic import View
from django.shortcuts import render

from decimal import Decimal

from catalog.domain.entities.product import Product
from catalog.domain.repositories.product_repository import ProductRepository


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
