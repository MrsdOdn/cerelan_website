# Generated by Django 5.0.3 on 2024-05-12 18:38

import django.core.validators
import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Minibus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('driver_first_name', models.CharField(max_length=64)),
                ('driver_last_name', models.CharField(max_length=64)),
                ('driver_contact_no', models.CharField(max_length=10)),
                ('pickup_location', models.CharField(max_length=64)),
                ('drop_off_location', models.CharField(max_length=64)),
                ('pickup_time', models.DateTimeField()),
                ('image', models.ImageField(help_text='Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.', upload_to='shared_car_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('route', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(blank=True, max_length=200, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minibus', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Minibus',
                'verbose_name_plural': 'Minibuses',
                'db_table': 'minibus',
                'ordering': ['-created_at'],
            },
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]
