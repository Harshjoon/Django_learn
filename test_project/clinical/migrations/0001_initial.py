# Generated by Django 4.2.7 on 2023-11-15 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hospital_name", models.CharField(max_length=100)),
                ("patient_name", models.CharField(max_length=100)),
                ("surgery_type", models.CharField(max_length=100)),
                (
                    "surgery_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
