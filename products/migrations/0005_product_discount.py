# Generated by Django 5.0.2 on 2024-02-26 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.discount'),
        ),
    ]
