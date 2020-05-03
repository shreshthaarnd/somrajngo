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
    path('error404/',adminpages404withoutmenus),
    path('adminlogin/',adminlogin),
    path('adminpanel/',adminpanel),
    path('adminlogout/',adminlogout),
    path('adminhome/',adminhome),
    path('postnews/',postnews),
]