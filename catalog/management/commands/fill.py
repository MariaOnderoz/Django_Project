import json

from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def json_read_data():
        with open('data.json', encoding='UTF-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Очистка таблиц для устранения конфликтов ID
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []

        data = self.json_read_data()  # Чтение данных один раз

        for entry in data:
            if entry['model'] == 'catalog.category':
                category_instance = Category(
                    id=entry['pk'],  # Установка PK из JSON
                    name=entry['fields']['name'],
                    description=entry['fields']['description']
                )
                category_for_create.append(category_instance)

        Category.objects.bulk_create(category_for_create)

        for entry in data:
            if entry['model'] == 'catalog.product':
                product_instance = Product(
                    id=entry['pk'],  # Установка PK из JSON
                    name=entry['fields']['name'],
                    description=entry['fields']['description'],
                    category_id=entry['fields']['category'],  # Прямое использование PK категории
                    price=entry['fields']['price']
                )
                product_for_create.append(product_instance)

        Product.objects.bulk_create(product_for_create)
        print("Data fill успешно выполнен")