# Generated by Django 3.1.4 on 2020-12-28 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20201226_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_order'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место на карте', 'verbose_name_plural': 'Места на карте'},
        ),
    ]
