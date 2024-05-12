# Generated by Django 5.0.3 on 2024-05-12 20:00

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('stop_name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('departure_time', models.DateTimeField()),
                ('return_time', models.DateTimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_stops', to='service.service')),
            ],
            options={
                'verbose_name': 'Bus Stop',
                'verbose_name_plural': 'Bus Stops',
                'db_table': 'bus_stop',
                'ordering': ['-created_at'],
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]
