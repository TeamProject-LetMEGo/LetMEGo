# Generated by Django 3.1.3 on 2020-11-20 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCB', '0002_auto_20201120_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mostcheapbank',
            name='bank_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCB.bankinfo'),
        ),
    ]
