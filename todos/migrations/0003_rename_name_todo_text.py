# Generated by Django 4.0.10 on 2024-01-31 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_complete_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='text',
        ),
    ]