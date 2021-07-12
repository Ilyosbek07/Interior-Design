# Generated by Django 3.2.3 on 2021-06-19 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last_name')),
                ('company', models.CharField(max_length=30, verbose_name='company')),
                ('phone', models.CharField(max_length=30, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('address1', models.CharField(max_length=30, verbose_name='address1')),
                ('address2', models.CharField(max_length=30, verbose_name='address2')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('state', models.CharField(max_length=30, verbose_name='state')),
                ('postcode', models.CharField(max_length=30, verbose_name='postcode')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('product', models.ManyToManyField(related_name='orders', to='products.ProductModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'oreder',
                'verbose_name_plural': 'orders',
            },
        ),
    ]