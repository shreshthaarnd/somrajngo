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