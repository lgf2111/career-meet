# Generated by Django 4.1.7 on 2023-03-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0003_event_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
    ]
