# Generated by Django 5.0.3 on 2024-08-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_delete_qttmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationmodel',
            name='ASDDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quotationmodel',
            name='ASDNo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='quotationmodel',
            name='BRName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='quotationmodel',
            name='EmailID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='quotationmodel',
            name='MOBILENO',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
