from django.views.generic import View
from django.shortcuts import render

from catalog.models import ProductData

from mapper.object_mapper import ObjectMapper


class Product(object):

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class ProductRepository(object):

    def __init__(self):
        self.mapper = ObjectMapper()
        self.mapper.create_map(Product, ProductData)

    def save(self, product):
        product_data = self.mapper.map(product, ProductData)
        product_data.save()

    def all(self):
        return ProductData.objects.all()


class CatalogView(View):

    def get(self, request):

        product = Product('Vai', 'Descricao do Livro', 10)

        repository = ProductRepository()
        repository.save(product)

        products = repository.all()

        return render(request, 'catalog/catalog_home.html', {'products': products})
