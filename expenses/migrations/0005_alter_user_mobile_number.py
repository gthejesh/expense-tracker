# Generated by Django 5.1.2 on 2024-10-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0004_remove_participant_split_method_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="mobile_number",
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
