# Generated by Django 4.2.3 on 2023-07-27 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='recommendations',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('office_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='medical.office')),
            ],
        ),
    ]
