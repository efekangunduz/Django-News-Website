# Generated by Django 3.2.7 on 2021-09-25 20:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0003_alter_images_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
