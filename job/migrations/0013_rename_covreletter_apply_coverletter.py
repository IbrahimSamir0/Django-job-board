# Generated by Django 4.1.2 on 2022-10-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_apply_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='covreletter',
            new_name='coverletter',
        ),
    ]