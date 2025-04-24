from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_main, name='login_main'),
    path('login_signin/', views.login_signin, name='login_signin'),
    path('login_signup/', views.login_signup, name='login_signup'),
    path('main_page/', views.main_page, name='main_page'),
]