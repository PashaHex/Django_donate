# Generated by Django 4.1.1 on 2022-10-20 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_item_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimate', models.IntegerField()),
                ('comment', models.TextField()),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]