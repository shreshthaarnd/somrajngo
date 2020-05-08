from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from django.core.mail import EmailMessage
from app.models import *
from app.myutil import *
from django.contrib.auth import logout
from wsgiref.util import FileWrapper
from django.http import HttpResponse, HttpResponseRedirect
import mimetypes
import os

def about(request):
	dic={'session':checksession(request),'value':True}
	return render(request,'about.html',dic)
def blog(request):
	dic={'session':checksession(request),'value':True}
	obj=NewsData.objects.all()
	lobj=list(reversed(list(obj)))
	dic.update({'data':reversed(obj),
				'rdata':lobj[0:5]})
	return render(request,'blog.html',dic)
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
	dic.update({'session':checksession(request),'value':True})
	return render(request,'blog-single.html',dic)
def causes(request):
	return render(request,'causes.html',{})
def contact(request):
	dic={'session':checksession(request),'value':True}
	return render(request,'contact.html',dic)
def index(request):
	dic={'session':checksession(request),'value':True}
	return render(request,'index.html',dic)
def services(request):
	dic={'session':checksession(request),'value':True}
	return render(request,'services.html',dic)
def userlogin(request):
	dic={'session':checksession(request),'value':True}
	return render(request,'userlogin.html',dic)
def registration(request):
	dic={'session':checksession(request),'value':True}
	return render(request,'registration.html',dic)
def campaigns(request):
	dic={'session':checksession(request),'value':True}
	return render(request,'campaigns.html',dic)

#Users Section
def myaccount(request):
	dic=GetUserDashboard(request.session['user_id'])
	dic.update({'session':checksession(request),'value':True})
	return render(request,'userdashboard.html',dic)

def saveuserbooks(request):
	try:
		bid=request.GET.get('bid')
		uid=request.session['user_id']
		obj=UserBooks(
			Book_ID=bid,
			User_ID=uid
			)
		obj.save()
		return redirect('/userbooks/')
	except:
		return redirect('/userlogin/')

def myaccount(request):
	dic=GetUserDashboard(request.session['user_id'])
	dic.update({'session':checksession(request),'value':True})
	return render(request,'userdashboard.html', dic)

def removeuserbook(request):
	dic=GetUserDashboard(request.session['user_id'])
	dic.update({'session':checksession(request),'value':True})
	bid=request.GET.get('bid')
	obj=UserBooks.objects.filter(Book_ID=bid).delete()
	return redirect('/userbooks/')

def userbooks(request):
	dic=GetUserDashboard(request.session['user_id'])
	dic.update({'session':checksession(request),'value':True})
	lt=[]
	d={}
	obj=UserBooks.objects.filter(User_ID=request.session['user_id'])
	for x in obj:
		obj2=BookData.objects.filter(Book_ID=x.Book_ID)
		for y in obj2:
			d={
			'bid':y.Book_ID,
			'bname':y.Book_Name,
			'bcategory':y.Book_Category,
			'bauthor':y.Book_Author,
			'babout':y.Book_About[0:100],
			'bcover':y.Book_Cover.url
			}
			lt.append(d)
	dic.update({'bdata':lt})
	return render(request,'userbooks.html',dic)

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
			dic.update({'session':checksession(request),'value':True})
			return render(request,'userdashboard.html',dic)
		else:
			return render(request,'userlogin.html',{'msg':'Incorrect Email or Password'})
	else:
		return redirect('/error404/')
def userprofile(request):
	dic=GetUserDashboard(request.session['user_id'])
	dic.update({'session':checksession(request),'value':True})
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
	dic.update({'session':checksession(request),'value':True})
	return render(request,'userprofile.html',dic)
@csrf_exempt
def usercampaigns(request):
	dic=GetUserDashboard(request.session['user_id'])
	dic.update({'session':checksession(request),'value':True})
	return render(request,'userdashboard.html',dic)

@csrf_exempt
def changeuserdetails(request):
	if request.method=="POST":
		p=request.POST.get('phone')
		a=request.POST.get('address')
		c=request.POST.get('city')
		s=request.POST.get('state')
		obj=UserData.objects.filter(User_ID=request.session['user_id'])
		obj.update(
			User_Phone=p,
			User_Address=a,
			User_City=c,
			User_State=s
			)
		dic=GetUserDashboard(request.session['user_id'])
		dic.update({'session':checksession(request),'value':True})
		return render(request,'userprofile.html',dic)
	else:
		return redirect('/error404/')
def error(request):
	return render(request,'error.html')

def logout(request):
	try:
		del request.session['user_id']
		request.session.flush()
		return redirect('/index/')
	except:
		return redirect('/index/')

@csrf_exempt
def changepassword(request):
	if request.method=='POST':
		op=request.POST.get('oldpass')
		np=request.POST.get('newpass')
		uid=request.session['user_id']
		obj=UserData.objects.filter(User_ID=uid)
		obj.update(User_Password='1')
		if UserData.objects.filter(User_ID=uid,User_Password=op).exists():
			obj=UserData.objects.filter(User_ID=uid,User_Password=op)
			obj.update(User_Password=np)
			dic=GetUserDashboard(request.session['user_id'])
			dic.update({'session':checksession(request),'value':True})
			return render(request,'userprofile.html',dic)
		else:
			return render(request,'error.html',{'msg':'Incorrect Password'})
	else:
		return redirect('/error404/')
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
def adminaddbook(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			dic={'cate':BookCategoryData.objects.all(),
				'msg':'Add Books'}
			return render(request,'adminpages/addbook.html',dic)
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

@csrf_exempt
def savebook(request):
	#try:
		if request.session['admin_id'] == 'admin@ngo.com':
			if request.method=="POST":
				obj=BookData.objects.all().delete()
				name=request.POST.get('bname')
				author=request.POST.get('bauthor')
				about=request.POST.get('babout')
				category=request.POST.get('bcategory')
				image=request.FILES['bimage']
				pdf=request.FILES['bpdf']
				print(category)
				n="B00"
				x=1
				nid=n+str(x)
				while BookData.objects.filter(Book_ID=nid).exists():
					x=x+1
					nid=n+str(x)
				x=int(x)
				obj=BookData(
					Book_ID=nid,
					Book_Name=name,
					Book_Category=category,
					Book_Author=author,
					Book_About=about,
					Book_Cover=image,
					Book_PDF=pdf
					)
				if BookData.objects.filter(Book_Name=name).exists():
					dic={'cate':BookCategoryData.objects.all(),
						'msg':'Book Already Exists'}
					return render(request,'adminpages/addbook.html',dic)
				else:
					obj.save()
					dic={'cate':BookCategoryData.objects.all(),
						'msg':'Book Saved Successfully'}
					return render(request,'adminpages/addbook.html',dic)
			else:
				return redirect('/error404/')
		else:
			return redirect('/error404/')
	#except:
	#	return redirect('/error404/')

def adminaddbookcategory(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			dic={'msg':'Add Books Category',
				'data':BookCategoryData.objects.all()}
			return render(request,'adminpages/addbookcategory.html',dic)
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

@csrf_exempt
def savebookcategory(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			if request.method=="POST":
				c=request.POST.get('name')
				n="BC00"
				x=1
				nid=n+str(x)
				while BookCategoryData.objects.filter(Category_ID=nid).exists():
					x=x+1
					nid=n+str(x)
				x=int(x)
				obj=BookCategoryData(
					Category_ID=nid,
					Category_Name=c
					)
				if BookCategoryData.objects.filter(Category_Name=c).exists():
					dic={'msg':'Already Exists',
						'data':BookCategoryData.objects.all()}
					return render(request,'adminpages/addbookcategory.html',dic)
				else:
					obj.save()
					dic={'msg':'Saved Successfully',
						'data':BookCategoryData.objects.all()}
					return render(request,'adminpages/addbookcategory.html',dic)
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')
def adminbooklist(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			dic={'data':reversed(list(BookData.objects.all()))}
			return render(request,'adminpages/booklist.html',dic)
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')

def deletebook(request):
	try:
		if request.session['admin_id'] == 'admin@ngo.com':
			obj=BookData.objects.filter(Book_ID=request.GET.get('bid'))
			obj.delete()
			dic={'data':reversed(list(BookData.objects.all()))}
			return render(request,'adminpages/booklist.html',dic)
		else:
			return redirect('/error404/')
	except:
		return redirect('/error404/')


def downloadbookpdf(request):
	obj=BookData.objects.filter(Book_ID=request.GET.get('bid'))
	file_path=''
	for x in obj:
		file_name = x.Book_PDF.name
	file_path = settings.MEDIA_ROOT +'/'+ file_name
	file_wrapper = FileWrapper(open(file_path,'rb'))
	file_mimetype = mimetypes.guess_type(file_path)
	response = HttpResponse(file_wrapper, content_type=file_mimetype )
	response['X-Sendfile'] = file_path
	response['Content-Length'] = os.stat(file_path).st_size
	response['Content-Disposition'] = 'attachment; filename=%s' % file_name 
	return response

def books(request):
	obj=BookData.objects.all()
	dic={'session':checksession(request),
		'value':True,
		'data':reversed(list(obj)),
		'cate':BookCategoryData.objects.all()}
	return render(request,'books.html',dic)

def bookcategorypage(request):
	obj=BookData.objects.filter(Book_Category=request.GET.get('category'))
	dic={'session':checksession(request),
		'value':True,
		'data':reversed(list(obj)),
		'cate':BookCategoryData.objects.all()}
	return render(request,'books.html',dic)