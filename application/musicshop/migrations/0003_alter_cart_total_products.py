# Generated by Django 4.1.3 on 2022-12-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0002_rename_imagecallery_imagegallery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_products',
            field=models.IntegerField(default=0, verbose_name='Общее кол-во товара'),
        ),
    ]
