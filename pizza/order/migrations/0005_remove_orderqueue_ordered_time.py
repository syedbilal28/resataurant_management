# Generated by Django 3.0.8 on 2020-07-30 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200730_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderqueue',
            name='ordered_time',
        ),
    ]
