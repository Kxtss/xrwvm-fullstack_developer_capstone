# Generated by Django 5.2.1 on 2025-05-28 04:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('car_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon'), ('COUPE', 'Coupe'), ('HATCHBACK', 'Hatchback'), ('MINIVAN', 'Minivan'), ('VAN', 'Van'), ('CONVERTIBLE', 'Convertible'), ('SPORTS CAR', 'Sports Car'), ('TRUCK', 'Truck'), ('HYBRID', 'Hybrid'), ('ELECTRIC', 'Electric'), ('OTHER', 'Other')], default='SUV', max_length=20)),
                ('year', models.IntegerField(default=2025, validators=[django.core.validators.MaxValueValidator(2026), django.core.validators.MinValueValidator(2015)])),
                ('dealer_id', models.IntegerField()),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake')),
            ],
        ),
    ]
