# Generated by Django 5.0.3 on 2024-05-05 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscategory',
            options={'ordering': ['-created_at'], 'verbose_name': 'News Category', 'verbose_name_plural': 'News Categories'},
        ),
    ]