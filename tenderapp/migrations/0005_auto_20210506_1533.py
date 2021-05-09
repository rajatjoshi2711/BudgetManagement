# Generated by Django 3.0.7 on 2021-05-06 10:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0004_auto_20210506_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_model',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 33, 28, 782447)),
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='invoice_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 33, 28, 782447)),
        ),
        migrations.AlterField(
            model_name='purchase_order_model',
            name='po_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 6, 10, 3, 28, 774525, tzinfo=utc)),
        ),
    ]
