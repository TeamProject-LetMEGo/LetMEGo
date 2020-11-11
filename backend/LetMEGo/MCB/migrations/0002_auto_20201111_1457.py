# Generated by Django 3.1.3 on 2020-11-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignbank',
            name='jpy_to_local_money',
            field=models.FloatField(null=True, verbose_name='1엔 to 도착지 돈'),
        ),
        migrations.AddField(
            model_name='foreignbank',
            name='usd_to_local_money',
            field=models.FloatField(null=True, verbose_name='1달러 to 도착지 돈'),
        ),
    ]
