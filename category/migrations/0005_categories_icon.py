# Generated by Django 5.0.2 on 2024-05-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_rename_api_type_instructions_api_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='category_images', verbose_name='Иконка'),
        ),
    ]
