# Generated by Django 4.1.3 on 2022-12-05 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puradata', '0002_alter_customer_cuit_alter_customer_dni_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cuit',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dni',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='cuit',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='dni',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]