# Generated by Django 4.1.3 on 2022-11-08 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productpropertyvalue_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='propert_value',
            field=models.ManyToManyField(blank=True, to='product.propertyvalue'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product'),
        ),
        migrations.DeleteModel(
            name='ProductPropertyValue',
        ),
    ]
