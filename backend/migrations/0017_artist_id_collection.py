# Generated by Django 4.0.4 on 2022-11-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_alter_perfil_discord_alter_perfil_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='id_collection',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
