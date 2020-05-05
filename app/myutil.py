from app.models import *

def GetUserDashboard(uemail):
	dic={}
	obj=UserData.objects.filter(User_Email=e)
	for x in obj:
		dic={
			'Fname':x.User_Fname,
			'Lname':x.User_Lname,
			'Gender':x.User_Gender,
			'fname':x.User_Email,
			'Phone':x.User_Phone,
			'Address':x.User_Address,
			'City':x.User_City,
			'State':x.User_State,
			'Age':x.User_Age,
			'Adhaar':x.User_Adhaar,
		}
	return dic