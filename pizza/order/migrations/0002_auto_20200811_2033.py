# Generated by Django 3.1 on 2020-08-11 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='size',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('Large', 'Large'), ('Medium', 'Medium'), ('Small', 'Small')], max_length=256)),
                ('quantity', models.IntegerField()),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.pizza')),
                ('topping', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.toppings')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Items',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='order.item'),
        ),
    ]
