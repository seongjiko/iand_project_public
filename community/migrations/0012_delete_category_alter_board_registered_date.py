# Generated by Django 5.0 on 2023-12-26 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0011_remove_board_category_alter_board_registered_date"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.AlterField(
            model_name="board",
            name="registered_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 26, 7, 45, 50, 24722, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
