from django.urls import path, include
from . import views

urlpatterns = [
    # path('guest/create/', views.createGuest, name='createGuest'),
    # path('guest/<str:id>/', views.getGuest, name='getGuest'),
    path('expense/create/', views.createExpense, name='createExpense'),
    path('expense/<str:id>/', views.getExpense, name='getExpense'),
    path('group/create/', views.createGroup, name='createGroup'),
    path('group/<str:id>/', views.getGroup, name='getGroup'),
    path('payment/create/', views.createPayment, name='createPayment'),
    path('payment/<str:id>/', views.getPayment, name='getPayment'),
    path('expenseparticipant/create/', views.createExpenseParticipant, name='createExpenseParticipant'),
    path('expenseparticipant/<str:id>/', views.getExpenseParticipant, name='getExpenseParticipant'),
    path('usergroup/create/', views.createUserGroup, name='createUserGroup'),
    path('usergroup/<str:id>/', views.getUserGroup, name='getUserGroup'),
    path('guest/', views.GuestView.as_view(), name='Guest'),
    path('guest/<str:id>/', views.GuestView.as_view(), name='Guest'),
]