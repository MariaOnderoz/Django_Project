from django.urls import path

from catalog.views import home, contacts, product_detail, products
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path ('', home, name='home'),
    path('', products, name='products'),
    path ('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_detail, name='product_detail')
]
