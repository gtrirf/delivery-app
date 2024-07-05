# Generated by Django 5.0.6 on 2024-07-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=100),
        ),
    ]
