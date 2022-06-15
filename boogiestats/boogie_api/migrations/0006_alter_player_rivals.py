# Generated by Django 4.0 on 2022-06-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boogie_api", "0005_player_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="rivals",
            field=models.ManyToManyField(
                blank=True, help_text="Hold ctrl to select/unselect multiple", to="boogie_api.Player"
            ),
        ),
    ]
