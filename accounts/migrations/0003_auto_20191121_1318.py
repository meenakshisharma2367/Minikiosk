# Generated by Django 2.2.7 on 2019-11-21 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191121_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=50)),
                ('host_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('host_phone', models.IntegerField()),
                ('host_image', models.ImageField(upload_to='assets/img/doctors')),
                ('host_desc', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.TextField(max_length=100)),
                ('current_meeting_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 21, 13, 18, 32, 352663)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2019, 11, 21, 13, 18, 32, 352663)),
        ),
    ]