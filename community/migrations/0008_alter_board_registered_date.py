# Generated by Django 5.0 on 2023-12-26 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0007_alter_board_registered_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="registered_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 26, 5, 16, 29, 481796, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
