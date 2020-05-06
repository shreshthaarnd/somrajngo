from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from django.core.mail import EmailMessage
from app.models import *
from app.myutil import *

def about(request):
	return render(request,'about.html',{})
def blog(request):
	obj=NewsData.objects.all()
	return render(request,'blog.html',{'data':reversed(list(obj))})
def blogsingle(request):
	dic={}
	obj=NewsData.objects.filter(News_ID=request.GET.get('nid'))
	for x in obj:
		dic={
			'title':x.News_Title,
			'date':x.News_Date,
			'body':x.News_Body,
			'type':x.News_Media_Type,
			'media':x.News_Media.url
		}
	return render(request,'blog-single.html',dic)
def causes(request):
	return render(request,'causes.html',{})
def contact(request):
	return render(request,'contact.html',{})
def index(request):
	return render(request,'index.html',{})
def services(request):
	return render(request,'services.html',{})
def userlogin(request):
	return render(request,'userlogin.html',{})
def registration(request):
	return render(request,'registration.html',{})
def campaigns(request):
	return render(request,'campaigns.html',{})
@csrf_exempt
def userdashboard(request):
	if request.method=="POST":
		e=request.POST.get('email')
		p=request.POST.get('pass')
		if UserData.objects.filter(User_Email=e,User_Password=p,User_Status='Active').exists():
			obj=UserData.objects.filter(User_Email=e)
			for x in obj:
				request.session['user_id'] = x.User_ID
				break
			dic=GetUserDashboard(request.session['user_id'])
			return render(request,'userdashboard.html',dic)
		else:
			return render(request,'userlogin.html',{'msg':'Incorrect Email or Password'})
	else:
		return redirect('/error404/')
def userprofile(request):
	dic=GetUserDashboard(request.session['user_id'])
	return render(request,'userprofile.html',dic)
@csrf_exempt
def saveuserprofilepicture(request):
	if request.method=='POST':
		obj=UserProfilePicture.objects.filter(User_ID=request.session['user_id']).delete()
		obj=UserProfilePicture(
			User_ID=request.session['user_id'],
			User_Image=request.FILES['image']
			)
		obj.save()
	dic=GetUserDashboard(request.session['user_id'])
	return render(request,'userprofile.html',dic)
@csrf_exempt
def usercampaigns(request):
	dic=GetUserDashboard(request.session['user_id'])
	return render(request,'userdashboard.html',dic)
	
@csrf_exempt
def saveuser(request):
	if request.method=='POST':
		txt=''
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		gender=request.POST.get('gender')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		address=request.POST.get('address')
		city=request.POST.get('city')
		state=request.POST.get('state')
		age=request.POST.get('age')
		adhaar=request.FILES['adhaar']
		u="U00"
		x=1
		uid=u+str(x)
		while UserData.objects.filter(User_ID=uid).exists():
			x=x+1
			uid=u+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, email+uid)
		password=str(otp)
		password=password.upper()[0:8]
		obj=UserData(
			User_ID=uid,
			User_Fname=fname,
			User_Lname=lname,
			User_Gender=gender,
			User_Email=email,
			User_Phone=phone,
			User_Address=address,
			User_City=city,
			User_State=state,
			User_Age=age,
			User_Password=password,
			User_Adhaar=adhaar,
			)
		if UserData.objects.filter(User_Email=e).exists():
			txt='User Already Exists'
		else:
			obj.save()
			msg='''Hi '''+fname+'''!
We have recieved your application and we currently reviewing your details, till then your account is deactivated.

Please wait for our confirmation mail.

Thanks & Regards,
Team Our Demand'''
			sub='Our Demand - Application Under Process'
			email=EmailMessage(sub,msg,to=[email])
			email.send()
			txt='You have successfully resgistered and we have recieved your application. Please wait for a confirmation mail while we are reviewing your application.'
		return render(request,'registration.html',{'msg':txt})

#AdminPannel Code
def adminindex(request):
	return render(request,'adminpages/index.html',{})
def adminpages404withoutmenus(request):
	return render(request,'adminpages/pages-404-withoutmenus.html',{})
def adminpages500(request):
	return render(request,'adminpages/pages-500.html',{})
def adminformsadvanced(request):
	return render(request,'adminpages/forms-advanced.html',{})
def adminformsbasic(request):
	return render(request,'adminpages/forms-basic.html',{})
def adminformscodeeditor(request):
	return render(request,'adminpages/forms-code-editor.html',{})
def adminformslayouts(request):
	return render(request,'adminpages/forms-layouts.html',{})
def adminformsvalidation(request):
	return render(request,'adminpages/forms-validation.html',{})
def adminformswizard(request):
	return render(request,'adminpages/forms-wizard.html',{})
def adminlayoutsboxed(request):
	return render(request,'adminpages/layouts-boxed.html',{})

def adminlogin(request):
	return render(request,'adminpages/adminlogin.html',{})

@csrf_exempt
def adminpanel(request):
	if request.method=='POST':
		e=request.POST.get('adminid')
		p=request.POST.get('pass')
		if e=='admin@ngo.com' and p=='1234':
			request.session['admin_id'] = e
			return render(request,'adminpages/index.html',{})
		else:
			return render(request,'adminpages/adminlogin.html',{'msg':'Incorrect ID or Password'})
	else:
		return redirect('/error404/')

def adminhome(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			return render(request,'adminpages/index.html',{})
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

@csrf_exempt
def adminlogout(request):
	try:
		del request.session['admin_id']
		request.session.flush()
		return redirect('/adminlogin/')
	except:
		return redirect('/error404/')


def adminnewslist(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			return render(request,'adminpages/newslist.html',{'obj':reversed(list(NewsData.objects.all()))})
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

def postnews(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			return render(request,'adminpages/postnews.html',{'msg':'Post News'})
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')
@csrf_exempt
def savenews(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			if request.method=='POST':
				title=request.POST.get('title')
				body=request.POST.get('body')
				media=request.FILES['media']
				mtype=request.POST.get('mediatype')
				n="N00"
				x=1
				nid=n+str(x)
				while NewsData.objects.filter(News_ID=nid).exists():
					x=x+1
					nid=n+str(x)
				x=int(x)
				obj=NewsData(
					News_ID=nid,
					News_Title=title,
					News_Body=body,
					News_Media_Type=mtype,
					News_Media=media
				)
				obj.save()
				return render(request,'adminpages/postnews.html',{'msg':'News Posted Successfully'})		
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')
def activeuser(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			obj=UserData.objects.filter(User_Status='Active')
			return render(request,'adminpages/activeuser.html',{'data':reversed(list(obj))})
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

def deactiveuser(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			obj=UserData.objects.filter(User_Status='Deactive')
			return render(request,'adminpages/deactiveuser.html',{'data':reversed(list(obj))})
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

def makeuseractive(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			uid=request.GET.get('uid')
			obj=UserData.objects.filter(User_ID=uid)
			obj.update(User_Status='Active')
			fname=''
			pas=''
			mail=''
			for x in obj:
				fname=x.User_Fname
				pas=x.User_Password
				mail=x.User_Email
			msg='''Hi '''+fname+'''!
Your account has been activated,

Email : '''+mail+'''
Password : '''+pas+'''

Thanks & Regards,
Team Our Demand'''
			sub='Our Demand - Account Activated'
			email=EmailMessage(sub,msg,to=[mail])
			email.send()
			obj=UserData.objects.filter(User_Status='Deactive')
			return render(request,'adminpages/deactiveuser.html',{'data':reversed(list(obj))})
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

def makeuserdeactive(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			uid=request.GET.get('uid')
			obj=UserData.objects.filter(User_ID=uid)
			obj.update(User_Status='Deactive')
			fname=''
			mail=''
			for x in obj:
				fname=x.User_Fname
				mail=x.User_Email
			msg='''Hi '''+fname+'''!
Your account has been deactivated due to some reasons. Please contact to our admin for activating your account.

Thanks & Regards,
Team Our Demand'''
			sub='Our Demand - Account Dectivated'
			email=EmailMessage(sub,msg,to=[mail])
			email.send()
			obj=UserData.objects.filter(User_Status='Active')
			return render(request,'adminpages/activeuser.html',{'data':reversed(list(obj))})
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')