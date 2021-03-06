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

class UserProfilePicture(models.Model):
	User_ID=models.CharField(max_length=100)
	User_Image=models.FileField(upload_to="userprofilepictures/")
	class Meta:
		db_table="UserProfilePicture"

class UserBooks(models.Model):
	User_ID=models.CharField(max_length=100)
	Book_ID=models.CharField(max_length=100)
	class Meta:
		db_table="UserBooks"

class BookCategoryData(models.Model):
	Category_ID=models.CharField(max_length=100)
	Category_Name=models.CharField(max_length=100)
	class Meta:
		db_table="BookCategoryData"

class BookData(models.Model):
	Book_ID=models.CharField(max_length=100)
	Book_Name=models.CharField(max_length=100)
	Book_Category=models.CharField(max_length=100)
	Book_Author=models.CharField(max_length=100)
	Book_About=models.CharField(max_length=1000)
	Book_Cover=models.ImageField(upload_to="bookcover/")
	Book_PDF=models.FileField(upload_to="bookpdf/")
	Download=models.CharField(max_length=100,default='0')
	class Meta:
		db_table="BookData"

class NewsCommentData(models.Model):
	Comment_ID=models.CharField(max_length=100)
	Comment_Date=models.DateField(("Date"), default=datetime.date.today)
	News_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	Comment=models.CharField(max_length=1000)
	class Meta:
		db_table="NewsCommentData"

class CampaignData(models.Model):
	Campaign_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	Campaign_Date=models.DateField(("Date"), default=datetime.date.today)
	Campaign_Title=models.CharField(max_length=1000, default='NA')
	Campaign_About=models.CharField(max_length=2000, default='NA')
	Campaign_Donation=models.CharField(max_length=50, default='NA')
	Campaign_Account_Number=models.CharField(max_length=50, default='NA')
	Campaign_Account_Name=models.CharField(max_length=50, default='NA')
	Campaign_Account_IFSC=models.CharField(max_length=50, default='NA')
	Campaign_Account_Bank=models.CharField(max_length=50, default='NA')
	Campaign_Status=models.CharField(max_length=50, default='Deactive')
	Campaign_Images=models.FileField(upload_to="campaignimages/")
	class Meta:
		db_table="CampaignData"

class DonationData(models.Model):
	Donation_Date=models.DateField(("Date"), default=datetime.date.today)
	Donation_ID=models.CharField(max_length=50)
	Donation_Name=models.CharField(max_length=100)
	Donation_Email=models.CharField(max_length=100)
	Donation_Phone=models.CharField(max_length=15)
	Donation_City=models.CharField(max_length=100)
	Donation_State=models.CharField(max_length=100)
	Donation_Amount=models.CharField(max_length=500)
	Payment_Status=models.CharField(max_length=100, default='Unpaid')
	Payment_ID=models.CharField(max_length=100, blank=True)
	class Meta:
		db_table="DonationData"