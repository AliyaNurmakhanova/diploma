# Generated by Django 3.0.7 on 2023-03-26 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20230326_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='lastname_kz',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='middlename_kz',
            new_name='middlename',
        ),
        migrations.RemoveField(
            model_name='students',
            name='stud_id',
        ),
    ]
