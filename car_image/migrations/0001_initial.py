# Generated by Django 5.0.3 on 2024-05-12 18:59

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('minibus', '0001_initial'),
        ('shared_car', '0002_alter_sharedcar_number_of_passengers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
                ('minibus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='minibus.minibus')),
                ('shared_car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='shared_car.sharedcar')),
            ],
            options={
                'verbose_name': 'Car Image',
                'verbose_name_plural': 'Car Images',
                'db_table': 'car_image',
                'ordering': ['-created_at'],
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]
