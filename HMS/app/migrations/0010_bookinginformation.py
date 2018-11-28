# Generated by Django 2.1.3 on 2018-11-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20181119_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingInformation',
            fields=[
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=150)),
                ('requirements', models.CharField(blank=True, max_length=100)),
                ('booking_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'bookinginfo',
            },
        ),
    ]