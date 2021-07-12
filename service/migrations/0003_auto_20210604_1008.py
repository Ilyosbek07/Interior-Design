# Generated by Django 3.2.3 on 2021-06-04 05:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210604_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammodel',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='name_uz',
        ),
        migrations.AddField(
            model_name='teammodel',
            name='short_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='short_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='short_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
    ]