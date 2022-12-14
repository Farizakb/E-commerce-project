# Generated by Django 4.1.3 on 2022-11-11 07:54

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
            name='City',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('cities', models.CharField(max_length=255, verbose_name='City')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('countries', models.CharField(max_length=255, verbose_name='Country')),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.abstractmodel')),
                ('company_name', models.CharField(blank=True, help_text='Max 255 char.', max_length=255, null=True, verbose_name='Company name')),
                ('address', models.TextField(verbose_name='Address')),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shipping_City', to='order.city', verbose_name='City')),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shipping_Country', to='order.country', verbose_name='Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('blog.abstractmodel',),
        ),
        migrations.AddField(
            model_name='city',
            name='countries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City_Country', to='order.country', verbose_name='Country'),
        ),
    ]
