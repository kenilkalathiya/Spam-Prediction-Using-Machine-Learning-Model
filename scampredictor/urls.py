from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('signup/', views.signinPage, name='signup'),
    path('fake-news-detection/', views.fakeNewsDetection, name='fakeNewsDetection')
]
