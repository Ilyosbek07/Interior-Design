# Generated by Django 3.2.3 on 2021-06-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20210613_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammodel',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
