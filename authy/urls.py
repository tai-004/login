from django.urls import path
from authy.views import UserProfile




urlpatterns = [
   	
    path('<username>/', UserProfile, name='profile'),
   
]