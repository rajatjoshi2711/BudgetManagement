# Generated by Django 3.0.7 on 2021-05-06 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0003_auto_20210506_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_model',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 32, 49, 499661)),
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='invoice_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 32, 49, 499661)),
        ),
        migrations.AlterField(
            model_name='purchase_order_model',
            name='po_date',
            field=models.DateField(default=datetime.date(2021, 5, 6)),
        ),
    ]
