# Generated by Django 4.1.1 on 2022-10-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('distance', models.CharField(max_length=128)),
                ('travel', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
