# Generated by Django 3.0 on 2020-10-10 20:55

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
                ('activity', models.CharField(max_length=150)),
                ('dept', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Electronics and Telecommunication', 'Electronics and Telecommunication'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil')], default='Computer Science', max_length=150)),
                ('pname', models.CharField(max_length=150)),
                ('pcontact', models.IntegerField()),
                ('participants', models.IntegerField()),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
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
