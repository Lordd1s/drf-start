# Generated by Django 4.2 on 2023-11-05 04:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0006_alter_proposemodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposemodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
