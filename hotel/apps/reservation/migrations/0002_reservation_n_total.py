# Generated by Django 4.2.6 on 2023-10-13 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='n_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
