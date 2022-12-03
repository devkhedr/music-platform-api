from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="Login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('logout/', knox_views.LogoutView.as_view(), name="Logout"),
]
