# Generated by Django 4.2 on 2023-04-29 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boa_app', '0004_responses_delete_response'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Responses',
            new_name='Response',
        ),
    ]
