# Generated by Django 4.2.7 on 2023-11-25 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0009_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
