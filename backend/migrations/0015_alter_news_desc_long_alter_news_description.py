# Generated by Django 4.0.4 on 2022-11-22 14:58

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_alter_about_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='desc_long',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
