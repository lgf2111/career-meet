# Generated by Django 4.1.7 on 2023-03-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="profile_pics/default.png", upload_to="profile_pics"
            ),
        ),
    ]
