# Generated by Django 4.1.7 on 2023-04-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_category_product_review_tag_delete_recipe_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_image",
            field=models.CharField(max_length=1024, null=True),
        ),
    ]