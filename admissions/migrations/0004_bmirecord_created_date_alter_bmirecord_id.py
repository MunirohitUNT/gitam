# Generated by Django 4.1.7 on 2023-04-11 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_bmirecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmirecord',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bmirecord',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
