# Generated by Django 2.1.9 on 2020-05-05 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200505_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('User_ID', models.CharField(max_length=100)),
                ('User_Fname', models.CharField(max_length=200)),
                ('User_Lname', models.CharField(max_length=200)),
                ('User_Gender', models.CharField(max_length=200)),
                ('User_Email', models.CharField(max_length=200)),
                ('User_Phone', models.CharField(max_length=200)),
                ('User_Address', models.CharField(max_length=500)),
                ('User_City', models.CharField(max_length=200)),
                ('User_State', models.CharField(max_length=200)),
                ('User_Age', models.CharField(max_length=200)),
                ('User_Status', models.CharField(default='Deactive', max_length=200)),
                ('User_Adhaar', models.FileField(upload_to='useradhaar/')),
            ],
            options={
                'db_table': 'UserData',
            },
        ),
    ]
