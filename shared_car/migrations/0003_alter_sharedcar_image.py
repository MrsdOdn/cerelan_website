# Generated by Django 5.0.3 on 2024-05-24 21:43

import django.core.validators
import shared_car.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_car', '0002_alter_sharedcar_number_of_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedcar',
            name='image',
            field=models.ImageField(help_text='Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.', upload_to='shared_car_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png']), shared_car.models.validate_image_size]),
        ),
    ]
