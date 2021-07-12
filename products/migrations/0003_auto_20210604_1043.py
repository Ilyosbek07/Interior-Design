# Generated by Django 3.2.3 on 2021-06-04 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210604_0957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caruselmodel',
            options={'verbose_name': 'carusel', 'verbose_name_plural': 'carusels'},
        ),
        migrations.AlterField(
            model_name='caruselmodel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='caruselmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='caruselmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='caruselmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]