# Generated by Django 4.2.5 on 2024-12-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogue", "0028_product_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="code",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                unique=True,
                verbose_name="Code can be used to store a secondary unique identifier, when upc isn't sufficient",
            ),
        ),
    ]
