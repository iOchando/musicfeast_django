# Generated by Django 4.0.4 on 2022-12-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_nftmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftmedia',
            name='artista',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
