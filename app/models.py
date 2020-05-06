from django.db import models
import datetime
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

class NewsData(models.Model):
	News_Date=models.DateField(("Date"), default=datetime.date.today)
	News_ID=models.CharField(max_length=100)
	News_Title=models.CharField(max_length=100)
	News_Body=models.CharField(max_length=2000)
	News_Media_Type=models.CharField(max_length=100)
	News_Media=models.FileField(upload_to="newsmedia/")
	class Meta:
		db_table="NewsData"

class UserData(models.Model):
	User_Date=models.DateField(("Date"), default=datetime.date.today)
	User_ID=models.CharField(max_length=100)
	User_Fname=models.CharField(max_length=200)
	User_Lname=models.CharField(max_length=200)
	User_Gender=models.CharField(max_length=200)
	User_Email=models.CharField(max_length=200)
	User_Phone=models.CharField(max_length=200)
	User_Address=models.CharField(max_length=500)
	User_City=models.CharField(max_length=200)
	User_State=models.CharField(max_length=200)
	User_Age=models.CharField(max_length=200)
	User_Password=models.CharField(max_length=200, default='1')
	User_Status=models.CharField(max_length=200, default='Deactive')
	User_Adhaar=models.FileField(upload_to="useradhaar/")
	class Meta:
		db_table="UserData"