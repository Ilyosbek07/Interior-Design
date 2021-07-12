# Generated by Django 3.2.3 on 2021-06-03 11:02

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='phone')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='title')),
                ('short_description', models.TextField(verbose_name='short_description')),
                ('long_description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='long_description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('short_description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
                ('job', models.CharField(max_length=55, verbose_name='job')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
        ),
    ]