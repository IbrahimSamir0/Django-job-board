# Generated by Django 4.1.3 on 2022-11-05 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='emil',
            new_name='emial',
        ),
    ]