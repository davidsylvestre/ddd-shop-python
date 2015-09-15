from django.views.generic import View
from django.shortcuts import render

from catalog.domain.entities.product import Product
from catalog.domain.repositories.product_repository import ProductRepository


class CatalogView(View):

    def get(self, request):

        product = Product('Vai', 'Descricao do Livro', 10)

        repository = ProductRepository()
        repository.save(product)

        products = repository.all()

        return render(request, 'catalog/catalog_home.html', {'products': products})
