# Generated by Django 4.1.3 on 2022-12-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0004_alter_cartproduct_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AddField(
            model_name='album',
            name='out_of_stock',
            field=models.IntegerField(default=False, verbose_name='Нет в наличии'),
        ),
    ]