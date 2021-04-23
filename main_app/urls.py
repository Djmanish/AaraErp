from django.urls import path, include
from main_app import *
from main_app import views


urlpatterns = [
  path('',views.login_page,name='login_page'),
  path('register',views.register,name='registration'),
  path('logout',views.logout_page,name='logout_page'),
]
