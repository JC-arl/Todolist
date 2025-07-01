from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_main, name='login_main'),
    path('login/signin/', views.login_signin, name='login_signin'),
    path('login/signup/', views.login_signup, name='login_signup'),
    path('signup/', views.signup, name='signup'),
    path('myuser/', views.UserLogin, name='login'),
    path('myuser/main_page/', views.main_page, name='main_page'),
    path('logout/', views.user_logout, name='logout'),
    path('todo/', views.todo_list, name='todo_list')
]