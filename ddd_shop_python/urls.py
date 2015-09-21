"""ddd_shop_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from catalog.views import CatalogView, ProductView, OrderView

urlpatterns = [
    url(r'^$', CatalogView.as_view(), name='home'),
    url(r'^products/new', ProductView.as_view(), name='productView'),
    url(r'^order', OrderView.as_view(), name='orderView'),
    url(r'^admin/', include(admin.site.urls)),
]
