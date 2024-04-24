# Generated by Django 5.0.4 on 2024-04-23 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('class_attended', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management.student')),
            ],
        ),
    ]
