from django.db import models


class ProductData(models.Model):

    class Meta:
        db_table = 'catalog_product'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class OrderData(models.Model):

    class Meta:
        db_table = 'order'

    product_id = models.IntegerField()
    client_id = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
