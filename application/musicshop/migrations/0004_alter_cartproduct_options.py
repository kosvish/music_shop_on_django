# Generated by Django 4.1.3 on 2022-12-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0003_alter_cart_total_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartproduct',
            options={'verbose_name': 'Продукт корзины', 'verbose_name_plural': 'Продукты корзины'},
        ),
    ]
