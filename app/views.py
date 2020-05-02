from django.shortcuts import render

# Create your views here.
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
def adminindex(request):
	return render(request,'adminpages/index.html',{})
def adminpages404withoutmenus(request):
	return render(request,'adminpages/pages-404-withoutmenus.html',{})
def adminpages500(request):
	return render(request,'adminpages/pages-500.html',{})
