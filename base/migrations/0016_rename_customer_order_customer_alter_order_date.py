# Generated by Django 4.1.1 on 2023-01-15 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_order_address_order_phone_alter_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 0, 7, 6, 968442)),
        ),
    ]