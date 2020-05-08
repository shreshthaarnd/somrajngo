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
    path('',index),
    path('index/',index),
    path('services/',services),
    path('adminindex/',adminindex),
    path('login/',userlogin),
    path('signup/',registration),
    path('campaigns/',campaigns),
    path('userdashboard/',userdashboard),
    path('userprofile/',userprofile),
    path('saveuser/',saveuser),
    path('saveprofilepicture/',saveuserprofilepicture),
    path('usercampaigns/',usercampaigns),
    path('books/',books),
    path('changedetails/',changeuserdetails),
    path('changepassword/',changepassword),
    path('error/',error),
    path('myaccount/',myaccount),
    path('logout/',logout),
    path('bookcategorypage/',bookcategorypage),
    path('userbooks/',userbooks),
    path('saveuserbooks/',saveuserbooks),
    path('removeuserbook/',removeuserbook),

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
    path('adminhome/',adminhome),
    path('adminlogin/',adminlogin),
    path('adminpanel/',adminpanel),
    path('adminlogout/',adminlogout),
    path('adminhome/',adminhome),
    path('postnews/',postnews),
    path('savenews/',savenews),
    path('newslist/',adminnewslist),
    path('activeuser/',activeuser),
    path('nonactiveuser/',deactiveuser),
    path('makeuseractive/',makeuseractive),
    path('makeuserdeactive/',makeuserdeactive),
    path('addbooks/',adminaddbook),
    path('savebook/',savebook),
    path('addbookcategroy/',adminaddbookcategory),
    path('savebookcategroy/',savebookcategory),
    path('booklist/',adminbooklist),
    path('downloadbookpdf/',downloadbookpdf),
    path('deletebook/',deletebook),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)