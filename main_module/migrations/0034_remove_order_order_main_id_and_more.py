# Generated by Django 4.2 on 2023-12-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0033_alter_order_payment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_main_id',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order_nimber',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order_number',
            field=models.IntegerField(default=234),
            preserve_default=False,
        ),
    ]