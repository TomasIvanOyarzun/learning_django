# Generated by Django 4.1.7 on 2023-02-17 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]