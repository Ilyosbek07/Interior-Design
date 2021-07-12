# Generated by Django 3.2.3 on 2021-06-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20210604_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='message')),
                ('phone', models.CharField(max_length=25, verbose_name='phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
