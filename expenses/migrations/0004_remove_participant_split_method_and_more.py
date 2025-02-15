# Generated by Django 5.1.2 on 2024-10-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0003_user_added_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="participant",
            name="split_method",
        ),
        migrations.AddField(
            model_name="expenses",
            name="split_method",
            field=models.CharField(
                choices=[
                    ("equal", "Equal"),
                    ("percentage", "Percentage"),
                    ("exact", "Exact"),
                ],
                default="equal",
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="expenses",
            name="title",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="expenses",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
