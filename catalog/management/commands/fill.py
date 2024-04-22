import json

from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_data():
        with open('data.json', encoding='UTF-8') as file:
            return json.load(file)


    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_data():
            if category['model'] == 'catalog.category':
                category_for_create.append(
                    Category(name=category['fields']['name'],
                             description=category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_data():
            if product['model'] == 'catalog.product':
                product_for_create.append(
                    Product(name=product['fields']['name'],
                            description=product['fields']['description'],
                            category=Category.objects.get(pk=product['fields']['category']),
                            price=product['fields']['price']))
        Product.objects.bulk_create(product_for_create)





