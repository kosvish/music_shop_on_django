# Generated by Django 4.1.4 on 2022-12-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0008_remove_cart_for_anonymous_user_cart_session_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='description_of_artist',
            field=models.TextField(default='Описание появится позже', verbose_name='Описание исполнителя'),
        ),
    ]
