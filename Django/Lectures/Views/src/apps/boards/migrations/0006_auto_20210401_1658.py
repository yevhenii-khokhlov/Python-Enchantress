# Generated by Django 3.1.7 on 2021-04-01 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20210329_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Col',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32)),
                ('position', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Order position')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cols', to='boards.board')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='col',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='boards.col'),
        ),
    ]
