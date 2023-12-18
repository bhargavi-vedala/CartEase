# Generated by Django 4.2.7 on 2023-12-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0013_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]