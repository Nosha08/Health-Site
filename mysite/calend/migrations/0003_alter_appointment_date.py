# Generated by Django 4.2.3 on 2023-07-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calend', '0002_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
