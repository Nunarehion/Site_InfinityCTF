# Generated by Django 5.1.6 on 2025-03-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/users', verbose_name='Изображение'),
        ),
    ]
