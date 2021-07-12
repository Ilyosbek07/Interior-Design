# Generated by Django 3.2.3 on 2021-07-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210707_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='post.CategoryModel', verbose_name='category'),
        ),
    ]