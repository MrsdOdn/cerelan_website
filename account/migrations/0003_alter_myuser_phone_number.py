# Generated by Django 5.0.3 on 2024-05-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_myuser_first_name_alter_myuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
