from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register, name='register'),
    path('username',views.username, name='username'),
    path('login',views.loginPage, name='login'),
    path('logout',views.logoutuser, name='logout'),
    path('',views.house, name='home' ),
    path('error',views.error,name='error')
]