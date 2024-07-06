# Generated by Django 5.0.6 on 2024-06-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('dewasa', models.PositiveIntegerField(default=0)),
                ('anak', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PrediksiPengunjung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('dewasa', models.PositiveIntegerField(default=0)),
                ('anak', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
