# Generated by Django 5.0.3 on 2024-05-26 12:14

import django.core.validators
import news.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(help_text='Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.', upload_to=news.models.news_image_upload_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])]),
        ),
    ]
