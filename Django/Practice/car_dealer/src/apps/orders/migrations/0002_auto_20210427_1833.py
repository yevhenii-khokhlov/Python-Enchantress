# Generated by Django 3.1.7 on 2021-04-27 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='car_id',
            new_name='car',
        ),
    ]