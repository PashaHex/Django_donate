# Generated by Django 4.1.1 on 2022-09-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_office_item_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='state',
            field=models.BooleanField(choices=[(0, 'Available'), (1, 'Booked')], default=0),
        ),
    ]