# Generated by Django 3.1.2 on 2020-10-11 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('activity_name', models.CharField(max_length=150)),
                ('department_name', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Electronics and Telecommunication', 'Electronics and Telecommunication'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil')], default='Computer Science', max_length=150)),
                ('resourse_person_name', models.CharField(max_length=150)),
                ('resourse_person_contact', models.IntegerField()),
                ('no_of_participants', models.IntegerField()),
                ('event_from_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('event_to_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('departments', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Electronics and Telecommunication', 'Electronics and Telecommunication'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil')], default='Computer Science', max_length=150)),
                ('employer', models.CharField(max_length=150)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('package', models.IntegerField()),
                ('ref_no', models.IntegerField()),
            ],
        ),
    ]
