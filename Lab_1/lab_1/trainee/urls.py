from django.urls import path
from .views import *

urlpatterns = [
    path('', Alltrainee, name='alltrainees'),
    path('Insert/', Insert, name="insert_tr"),
    path('Update/<int:id>/', Update, name='update_tr'),
    path('Delete/<int:id>/', Delete, name='delete_tr')
]
