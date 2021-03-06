# Generated by Django 3.0.7 on 2021-05-06 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0011_auto_20210506_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_model',
            name='adv_pay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='request_model',
            name='bal_pay_amt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='request_model',
            name='net_pay_amt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='request_model',
            name='project_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='request_model',
            name='tds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='request_model',
            name='tds_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='request_model',
            name='vendor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 18, 50, 53, 561532)),
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='invoice_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 18, 50, 53, 561532)),
        ),
        migrations.AlterField(
            model_name='purchase_order_model',
            name='po_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 18, 50, 53, 561532)),
        ),
    ]
