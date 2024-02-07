from django.urls import path, include
from . import views

urlpatterns = [
    path('createguest/', views.createGuest, name='createGuest'),
    path('getguest/<str:id>/', views.getGuest, name='getGuest'),
    
]