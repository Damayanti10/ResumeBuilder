# Generated by Django 4.0.3 on 2022-04-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profilr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('experience', models.TextField(max_length=1000)),
                ('skill', models.TextField(max_length=1000)),
                ('about_youself', models.TextField(max_length=1000)),
            ],
        ),
    ]
