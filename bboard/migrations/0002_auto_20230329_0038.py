# Generated by Django 3.0.7 on 2023-03-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='lastname_eng',
            field=models.CharField(default='Фамилия', max_length=100, verbose_name='Фамилия на английском'),
        ),
        migrations.AddField(
            model_name='students',
            name='middlename_eng',
            field=models.CharField(default='Отчество', max_length=100, verbose_name='Отчество на английском'),
        ),
        migrations.AddField(
            model_name='students',
            name='name_eng',
            field=models.CharField(default='Имя', max_length=100, verbose_name='Имя на английском'),
        ),
    ]