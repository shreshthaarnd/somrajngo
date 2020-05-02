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
