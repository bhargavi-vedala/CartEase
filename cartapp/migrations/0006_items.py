# Generated by Django 4.2.7 on 2023-11-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0005_cart_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]