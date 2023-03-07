from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('<int:pk>/', csrf_exempt(views.UserView.as_view())),
]
