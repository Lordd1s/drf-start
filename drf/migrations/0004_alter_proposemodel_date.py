# Generated by Django 4.2.6 on 2023-10-09 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drf", "0003_alter_proposemodel_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proposemodel",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 9, 1, 26, 11, 691611, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]