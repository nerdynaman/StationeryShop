# Generated by Django 4.1.7 on 2023-04-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_product_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.CharField(
                default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.co",
                max_length=1024,
            ),
        ),
    ]
