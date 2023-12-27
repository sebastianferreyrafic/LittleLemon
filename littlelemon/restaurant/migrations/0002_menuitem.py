# Generated by Django 5.0 on 2023-12-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                ("category", models.CharField(max_length=100)),
            ],
        ),
    ]