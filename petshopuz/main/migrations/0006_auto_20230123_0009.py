# Generated by Django 3.2.16 on 2023-01-22 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230122_2339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yan',
            options={'verbose_name': 'asosiydog', 'verbose_name_plural': 'AsosiyDogs'},
        ),
        migrations.AddField(
            model_name='yan',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='yan',
            name='img',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='zakazlar',
            name='vaqt',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 23, 0, 9, 29, 443072)),
        ),
    ]
