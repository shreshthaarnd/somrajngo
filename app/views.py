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