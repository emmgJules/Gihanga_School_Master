# Generated by Django 5.0.4 on 2024-04-24 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0002_remove_pages_creator_remove_pnotice_creator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='dob',
        ),
    ]
