from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0022_orderdetail_order_nimber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_nimber',
            field=models.CharField(max_length=255),  
        ),
    ]
