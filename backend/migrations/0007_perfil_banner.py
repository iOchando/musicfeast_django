# Generated by Django 4.0.4 on 2022-10-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
