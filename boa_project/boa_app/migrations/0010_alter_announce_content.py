# Generated by Django 4.2 on 2023-05-14 18:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boa_app', '0009_alter_announce_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
