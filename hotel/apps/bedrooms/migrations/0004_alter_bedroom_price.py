# Generated by Django 4.2.6 on 2023-10-13 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedrooms', '0003_bedroom_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedroom',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10),
        ),
    ]
