# Generated by Django 4.1 on 2022-09-02 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0026_orders_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.IntegerField(),
        ),
    ]
