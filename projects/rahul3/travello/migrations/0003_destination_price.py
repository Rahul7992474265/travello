# Generated by Django 3.1.6 on 2021-03-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_remove_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
