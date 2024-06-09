# Generated by Django 5.0.2 on 2024-05-07 11:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_rename_api_type_instructions_api_type'),
        ('new_services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='newapi',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='newapi',
            name='categories',
            field=models.ManyToManyField(to='category.categories', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='newapi',
            name='content',
            field=models.TextField(max_length=300, verbose_name='Подробная информация'),
        ),
        migrations.AlterField(
            model_name='newapi',
            name='summary',
            field=models.CharField(max_length=100, verbose_name='Краткая информация'),
        ),
    ]
