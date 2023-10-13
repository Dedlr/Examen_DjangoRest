# Generated by Django 4.2.6 on 2023-10-13 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dpi_pasaporte', models.CharField(max_length=20)),
                ('nit', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=255)),
                ('nationality', models.CharField(choices=[('Local', 'Local'), ('Extranjero', 'Extranjero')], max_length=30)),
                ('type_client', models.CharField(choices=[('Comun', 'Comun'), ('Coorporativo', 'Coorporativo')], max_length=30)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]