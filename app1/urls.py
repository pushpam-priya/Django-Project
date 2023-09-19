from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('name',views.name),
    path('',views.loginpage),
    # path('index/',views.),
    path('home',views.home,name='home'),
    path('loginpage/',views.loginpage),
    path('handlelogin/',views.handlelogin),
    path('logout',views.flogout),
    path('signuppage',views.signuppage),
    path('handleSignup',views.handleSignup),
    path('contact',views.contact),
    path('about',views.about),
    path('userreq',views.usereq),
    path('result',views.result),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)