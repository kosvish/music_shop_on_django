# Generated by Django 4.1.4 on 2022-12-09 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0014_alter_albumartist_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albumartist',
            old_name='album',
            new_name='name',
        ),
    ]
