# Generated by Django 4.1.1 on 2022-11-13 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category_customer_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
