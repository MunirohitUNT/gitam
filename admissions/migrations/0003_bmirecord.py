# Generated by Django 4.1.7 on 2023-04-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BmiRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('bmi', models.FloatField()),
            ],
        ),
    ]