# Generated by Django 3.2.1 on 2021-05-06 21:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenderapp', '0012_auto_20210506_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_model',
            fields=[
                ('project_no', models.IntegerField(default=0, primary_key=True, serialize=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('allocate', models.IntegerField(default=0)),
                ('utilized', models.IntegerField(default=0)),
                ('available', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 17, 2, 12, 263524)),
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='invoice_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 17, 2, 12, 263524)),
        ),
        migrations.AlterField(
            model_name='purchase_order_model',
            name='po_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 17, 2, 12, 263524)),
        ),
        migrations.CreateModel(
            name='Rml_model',
            fields=[
                ('rml_no', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('allocate', models.IntegerField(default=0)),
                ('utilized', models.IntegerField(default=0)),
                ('available', models.IntegerField(default=0)),
                ('project_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenderapp.project_model')),
            ],
        ),
        migrations.AlterField(
            model_name='invoice_model',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenderapp.project_model'),
        ),
        migrations.AlterField(
            model_name='purchase_order_model',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='tenderapp.project_model'),
        ),
        migrations.DeleteModel(
            name='Budget_model',
        ),
    ]
