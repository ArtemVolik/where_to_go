# Generated by Django 3.1.4 on 2021-01-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20201228_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(verbose_name='Короткое описание'),
        ),
    ]
