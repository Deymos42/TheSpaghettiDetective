# Generated by Django 2.2.10 on 2021-03-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20210228_1959'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalPrint',
        ),
        migrations.DeleteModel(
            name='HistoricalPrinter',
        ),
    ]