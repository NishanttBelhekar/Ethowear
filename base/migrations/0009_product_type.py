# Generated by Django 4.1.1 on 2022-11-17 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='base.type'),
        ),
    ]
