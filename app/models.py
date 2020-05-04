from django.db import models
import datetime
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

class NewsData(models.Model):
	News_Date=models.DateField(("Date"), default=datetime.date.today)
	News_ID=models.CharField(max_length=100)
	News_Title=models.CharField(max_length=100)
	News_Body=models.CharField(max_length=2000)
	News_Image=models.ImageField(upload_to="newsimages/")
	class Meta:
		db_table="NewsData"