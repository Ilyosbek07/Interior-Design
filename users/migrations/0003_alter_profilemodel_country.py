# Generated by Django 3.2.3 on 2021-06-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='country'),
        ),
    ]