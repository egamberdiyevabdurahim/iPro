# Generated by Django 5.0.2 on 2024-02-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='viewed_list',
            field=models.IntegerField(default=0),
        ),
    ]
