from django.urls import path, include
from . import views

urlpatterns = [
    # path('guest/create/', views.createGuest, name='createGuest'),
    # path('guest/<str:id>/', views.getGuest, name='getGuest'),
    path('guest/', views.GuestView.as_view(), name='Guest'),
    path('guest/<str:id>/', views.GuestView.as_view(), name='Guest'),
    
    path('expenseparticipant/', views.ExpenseParticipantView.as_view(), name='ExpenseParticipant'),
    path('expenseparticipant/<str:id>', views.ExpenseParticipantView.as_view(), name='ExpenseParticipant'),
    path('expenseparticipant/', views.ExpenseParticipantViewList.as_view(), name='ExpenseParticipantList'),

    path('expense/', views.ExpenseView.as_view(), name='Expense'),
    path('expense/<str:id>', views.ExpenseView.as_view(), name='Expense'),
    path('expenses/', views.ExpenseViewList.as_view(), name='ExpenseList'),
    
    path('group/', views.GroupView.as_view(), name='Group'),
    path('group/<str:id>', views.GroupView.as_view(), name='Group'),
    path('group/', views.GroupViewList.as_view(), name='GroupList'),

    path('payment/', views.PaymentView.as_view(), name='Payment'),
    path('payment/<str:id>', views.PaymentView.as_view(), name='Payment'),
    path('payment/', views.PaymentViewList.as_view(), name='PaymentList'),

    path('usergroup/', views.UserGroupView.as_view(), name='UserGroup'),
    path('usergroup/<str:id>', views.UserGroupView.as_view(), name='UserGroup'),
]