# Generated by Django 3.1.2 on 2020-11-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_studfac1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studfac1',
            name='type_of_meeting_open_GFM_or_HOD_close',
            field=models.CharField(max_length=150, verbose_name='Type of meeting (GFM/HOD)'),
        ),
    ]
