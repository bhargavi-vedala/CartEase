# Generated by Django 4.2.7 on 2023-11-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_remove_cart_product_delete_buy_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
            ],
        ),
    ]
