from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from django.core.mail import EmailMessage

def about(request):
	return render(request,'about.html',{})
def blog(request):
	return render(request,'blog.html',{})
def blogsingle(request):
	return render(request,'blog-single.html',{})
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
			return render(request,'adminpages/postnews.html',{})
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

def postnews(request):
	#try:
	#	if request.session['admin_id'] == 'admin@ngo.com':
			return render(request,'adminpages/postnews.html',{})
	#	else:
	#		return redirect('/error404/')
	#except:
	#	return redirect('/error404/')
def adminvideonewspost(request):
	return render(request,'adminpages/videonewspost.html',{})
def adminnewslist(request):
	return render(request,'adminpages/newslist.html',{})
def adminvideonewslist(request):
	return render(request,'adminpages/videonewslist.html',{})
def registration(request):
	return render(request,'registration.html',{})	

