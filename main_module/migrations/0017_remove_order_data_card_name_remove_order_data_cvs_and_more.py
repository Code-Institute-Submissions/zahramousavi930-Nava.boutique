# Generated by Django 4.2 on 2023-12-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0016_alter_products_color_alter_products_color2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_data',
            name='card_name',
        ),
        migrations.RemoveField(
            model_name='order_data',
            name='cvs',
        ),
        migrations.RemoveField(
            model_name='order_data',
            name='expiration_date',
        ),
        migrations.AlterField(
            model_name='order_data',
            name='street_address2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
