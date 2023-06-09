# Generated by Django 4.1.7 on 2023-03-31 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_file', models.ImageField(upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
