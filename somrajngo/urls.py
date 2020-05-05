from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about),
    path('news/',blog),
    path('blogsingle/',blogsingle),
    path('causes/',causes),
    path('contact/',contact),
    path('index/',index),
    path('services/',services),
    path('adminindex/',adminindex),
    path('login/',userlogin),

    path('error404/',adminpages404withoutmenus),
    path('adminlogin/',adminlogin),
    path('adminpanel/',adminpanel),
    path('adminlogout/',adminlogout),
    path('adminhome/',adminhome),
    path('postnews/',postnews),
    path('savenews/',savenews),
    path('newslist/',adminnewslist),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)