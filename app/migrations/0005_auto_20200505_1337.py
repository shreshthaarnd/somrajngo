# Generated by Django 2.1.9 on 2020-05-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200505_0155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoNewsData',
        ),
        migrations.RemoveField(
            model_name='newsdata',
            name='News_Image',
        ),
        migrations.AddField(
            model_name='newsdata',
            name='News_Media',
            field=models.FileField(default=1, upload_to='newsmedia/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsdata',
            name='News_Media_Type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
