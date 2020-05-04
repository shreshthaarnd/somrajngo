from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about),
    path('blog/',blog),
    path('blogsingle/',blogsingle),
    path('causes/',causes),
    path('contact/',contact),
    path('index/',index),
    path('services/',services),
    path('adminindex/',adminindex),
    path('userlogin/',userlogin),
    path('registration/',registration),

    path('adminpages404withoutmenus/',adminpages404withoutmenus),
    path('adminpages500/',adminpages500),
    path('adminformsadvanced/',adminformsadvanced),
    path('adminformsbasic/',adminformsbasic),
    path('adminformscodeeditor/',adminformscodeeditor),
    path('adminformslayouts/',adminformslayouts),
    path('adminformsvalidation/',adminformsvalidation),
    path('adminformswizard/',adminformswizard),
    path('adminlayoutsboxed/',adminlayoutsboxed),
    path('adminlayoutsboxed/',adminlayoutsboxed),


    path('error404/',adminpages404withoutmenus),
    path('adminlogin/',adminlogin),
    path('adminpanel/',adminpanel),
    path('adminlogout/',adminlogout),
    path('adminhome/',adminhome),
    path('postnews/',postnews),
    path('adminvideonewspost/',adminvideonewspost),
    path('adminnewslist/',adminnewslist),
    path('adminvideonewslist/',adminvideonewslist),

]