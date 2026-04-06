from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.Signupview.as_view(), name='signup'),
    path('login/', views.loginview.as_view(), name='login'),
]