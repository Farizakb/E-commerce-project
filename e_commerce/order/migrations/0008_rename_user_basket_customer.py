# Generated by Django 4.1.3 on 2022-11-15 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_basket_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='user',
            new_name='customer',
        ),
    ]
