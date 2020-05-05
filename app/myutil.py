from app.models import *

def GetUserDashboard(uemail):
	dic={}
	obj=UserData.objects.filter(User_Email=e)
	for x in obj:
		dic={
			'fname':x.User_Fname,
			'fname':x.User_Fname,
			'fname':x.User_Fname,
			'fname':x.User_Fname,
			'fname':x.User_Fname,
			'fname':x.User_Fname,
			'fname':x.User_Fname,
			'fname':x.User_Fname,
		}