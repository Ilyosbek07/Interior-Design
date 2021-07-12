# Generated by Django 3.2.3 on 2021-06-11 12:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_blogmodel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created_at'),
            preserve_default=False,
        ),
    ]