# Generated by Django 5.0 on 2023-12-19 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tryModel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='AGE',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='CITY',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Name',
            new_name='name',
        ),
    ]