# Generated by Django 4.1.3 on 2022-12-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('musicshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageCallery',
            new_name='ImageGallery',
        ),
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='musicshop.cartproduct', verbose_name='Продукты для корзины'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес'),
        ),
    ]