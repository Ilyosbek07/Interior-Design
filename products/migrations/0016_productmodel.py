# Generated by Django 3.2.3 on 2021-06-19 07:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_blogmodel_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='title')),
                ('title_en', models.CharField(max_length=25, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=25, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=25, null=True, verbose_name='title')),
                ('short_description', models.TextField(null=True)),
                ('long_description', ckeditor.fields.RichTextField(verbose_name='content')),
                ('long_description_en', ckeditor.fields.RichTextField(null=True, verbose_name='content')),
                ('long_description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='content')),
                ('long_description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='content')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]