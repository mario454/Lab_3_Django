from django.urls import path
from .views import *
app_name = 'myuser'
urlpatterns = [
    path("Login/", Login, name='login'),
    path("Register/", Register, name='register'),
    path("Logout/", Logout, name='logout'),
]
