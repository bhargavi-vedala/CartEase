# Generated by Django 4.2.7 on 2023-11-24 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0006_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Buy',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]