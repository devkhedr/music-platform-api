from django.urls import path, include 
from . import views
from knox import views as knox_views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view()),
    path('login/', views.LoginUserView.as_view()),
    path('logout/',knox_views.LogoutView.as_view()),
]