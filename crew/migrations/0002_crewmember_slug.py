# Generated by Django 4.1.1 on 2022-10-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crewmember',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
