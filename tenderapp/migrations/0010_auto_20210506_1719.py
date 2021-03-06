# Generated by Django 3.0.7 on 2021-05-06 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0009_auto_20210506_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_model',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 17, 19, 2, 91715)),
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='invoice_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 17, 19, 2, 91715)),
        ),
        migrations.AlterField(
            model_name='purchase_order_model',
            name='po_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 17, 19, 2, 91715)),
        ),
        migrations.AlterField(
            model_name='vendor_model',
            name='black_list',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='vendor_model',
            name='is_gst',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='vendor_model',
            name='is_pan',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
