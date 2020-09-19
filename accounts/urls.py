from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('signup/', views.signUpPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('test/', views.TestPage, name='test'),
    path('thanks/', views.ThanksPage, name='thanks')
]
