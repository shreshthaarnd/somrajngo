# Generated by Django 2.1.9 on 2020-05-14 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_campaigndata_campaign_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donation_Date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Donation_ID', models.CharField(max_length=50)),
                ('Donation_Name', models.CharField(max_length=100)),
                ('Donation_Email', models.CharField(max_length=100)),
                ('Donation_Phone', models.CharField(max_length=15)),
                ('Donation_City', models.CharField(max_length=100)),
                ('Donation_State', models.CharField(max_length=100)),
                ('Donation_Amount', models.CharField(max_length=500)),
                ('Payment_Status', models.CharField(default='Unpaid', max_length=100)),
                ('Payment_ID', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'DonationData',
            },
        ),
    ]
