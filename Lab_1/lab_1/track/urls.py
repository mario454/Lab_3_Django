from django.urls import path
from .views import *

urlpatterns = [
    path('', alltracks, name="alltracks"),
    path('Insert/', Insert, name="inserttrack"),
    path('Update/<int:id>/', Update, name='updatetrack'),
    path('Delete/<int:id>/', Delete, name='deletetrack')
]