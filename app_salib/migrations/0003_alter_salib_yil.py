# Generated by Django 5.0.4 on 2024-04-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_salib', '0002_theme_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salib',
            name='yil',
            field=models.CharField(max_length=100),
        ),
    ]