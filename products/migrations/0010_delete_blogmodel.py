# Generated by Django 3.2.3 on 2021-06-09 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_blogmodel_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogModel',
        ),
    ]