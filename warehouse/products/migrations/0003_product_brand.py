# Generated by Django 4.2.7 on 2023-11-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='n/a', max_length=20),
        ),
    ]
