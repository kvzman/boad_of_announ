# Generated by Django 4.2 on 2023-05-14 17:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boa_app', '0008_mailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
