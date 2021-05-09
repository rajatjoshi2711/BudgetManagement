# Generated by Django 3.0.7 on 2021-05-06 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0006_auto_20210506_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_model',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 43, 25, 953737)),
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='invoice_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 43, 25, 953737)),
        ),
        migrations.AlterField(
            model_name='payment_model',
            name='date',
            field=models.DateTimeField(default='2021-05-01'),
        ),
        migrations.AlterField(
            model_name='purchase_order_model',
            name='po_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 43, 25, 950746)),
        ),
    ]
