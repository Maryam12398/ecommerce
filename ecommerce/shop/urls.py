from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home_page, name='home_page'), # The empty string means the homepage
    path('my_account', views.my_account, name='my_account'), # The empty string means the homepage
    path("signup", views.Sign_up, name= "signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]