# Generated by Django 4.1.3 on 2022-11-11 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='product.category')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('value', models.IntegerField()),
                ('is_percentage', models.BooleanField(default=True)),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('code', models.IntegerField()),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.category')),
                ('discounts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.discount')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('category', models.ManyToManyField(blank=True, related_name='property', to='product.category')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('title', models.CharField(max_length=100)),
                ('properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_value', to='product.property')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='ProductPropertyValue',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('count', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_property', to='product.product')),
                ('property_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_property', to='product.propertyvalue')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('path', models.ImageField(upload_to='product_image')),
                ('is_main', models.BooleanField(default=True)),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('content', models.CharField(max_length=255)),
                ('review', models.CharField(choices=[('1', '1 Star'), ('2', '2 Star'), ('3', '3 Star'), ('4', '4 Star'), ('5', '5 Star')], max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_comment', to=settings.AUTH_USER_MODEL)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_comment', to='product.product')),
            ],
            bases=('blog.abstractmodel',),
        ),
    ]
