# Generated by Django 3.1.7 on 2021-04-27 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20210427_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='color_id',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='dealer_id',
            new_name='dealer',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='model_id',
            new_name='model',
        ),
    ]
