from app.models import *

def GetUserDashboard(uid):
	dic={}
	obj=UserData.objects.filter(User_ID=uid)
	for x in obj:
		dic={
			'Fname':x.User_Fname,
			'Lname':x.User_Lname,
			'Gender':x.User_Gender,
			'Email':x.User_Email,
			'Phone':x.User_Phone,
			'Address':x.User_Address,
			'City':x.User_City,
			'State':x.User_State,
			'Age':x.User_Age,
			'Adhaar':x.User_Adhaar,
		}
	obj=UserProfilePicture.objects.filter(User_ID=uid)
	for x in obj:
		dic.update({'image':x.User_Image.url})
	return dic

def checksession(request):
	try:
		if UserData.objects.filter(User_ID=request.session['user_id']).exists():
			return True
		else:
			return False
	except:
		return False

def GetHomeBlogs():
	obj=NewsData.objects.all()
	lt=[]
	d={}
	for x in obj:
		d={
		'News_Date':x.News_Date,
		'News_ID':x.News_ID,
		'News_Title':x.News_Title,
		'News_Body':x.News_Body[0:120],
		'News_Media_Type':x.News_Media_Type,
		'News_Media':x.News_Media
		}
		obj1=NewsCommentData.objects.filter(News_ID=x.News_ID)
		d.update({'commentcount':len(obj1)})
		lt.append(d)
	lt2=list(reversed(lt))
	dic={'blog1':lt2[0:1], 'blog2':lt2[1:2], 'blog3':lt2[2:4]}
	return dic

def GetHomeCampaigns():
	d={}
	lt=[]
	obj=CampaignData.objects.filter(Campaign_Status='Active')
	for x in obj:
		if x.Campaign_Title != 'NA':
			d={
				'camid':x.Campaign_ID,
				'date':x.Campaign_Date,
				'title':x.Campaign_Title,
				'about':x.Campaign_About[0:65]+'....',
				'donation':x.Campaign_Donation.upper(),
				'cover':x.Campaign_Images,
				'acnumber':x.Campaign_Account_Number,
				'acname':x.Campaign_Account_Name,
				'acifsc':x.Campaign_Account_IFSC,
				'acbank':x.Campaign_Account_Bank
			}
			obj1=CampaignData.objects.filter(Campaign_ID=x.Campaign_ID)
			for y in obj1:
				d.update({'image':y.Campaign_Images})
				break
			lt.append(d)
	lt2=list(reversed(lt))
	dic={'cam1':lt2[0:1], 'cam2':lt2[1:2], 'cam3':lt2[2:4]}
	return dic