# Generated by Django 4.2.2 on 2024-06-01 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('cancel_publication', 'может отменять публикацию продукта'), ('change_product_description', 'может менять описание любого продукта'), ('change_category', 'может менять категорию любого продукта')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
