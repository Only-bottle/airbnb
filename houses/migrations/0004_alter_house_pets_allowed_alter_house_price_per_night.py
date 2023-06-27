# Generated by Django 4.2.2 on 2023-06-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("houses", "0003_rename_price_house_price_per_night"),
    ]

    operations = [
        migrations.AlterField(
            model_name="house",
            name="pets_allowed",
            field=models.BooleanField(
                default=True,
                help_text="Does this house allow pets?",
                verbose_name="Pets Allowed?",
            ),
        ),
        migrations.AlterField(
            model_name="house",
            name="price_per_night",
            field=models.PositiveIntegerField(
                help_text="Positive Numbers Only", verbose_name="Price"
            ),
        ),
    ]
