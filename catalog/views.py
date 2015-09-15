from django.views.generic import View
from django.shortcuts import render

from catalog.models import Product


class CatalogView(View):

    def get(self, request):

        # product = Product()
        # product.name = 'Teste'
        # product.description = 'Teste Description'
        # product.price = 10
        # product.save()

        products = Product.objects.all()

        return render(request, 'catalog/catalog_home.html', {'products': products})
