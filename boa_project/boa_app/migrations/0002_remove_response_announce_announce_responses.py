# Generated by Django 4.2 on 2023-04-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boa_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='announce',
        ),
        migrations.AddField(
            model_name='announce',
            name='responses',
            field=models.ManyToManyField(related_name='responses', to='boa_app.response'),
        ),
    ]
