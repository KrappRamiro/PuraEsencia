# Generated by Django 4.1.3 on 2022-12-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puradata', '0005_rename_invoiced_order_facturado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='cash_payment_currency',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='mercado_pago_payment_currency',
        ),
        migrations.AlterField(
            model_name='orderline',
            name='cash_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderline',
            name='mercado_pago_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
