from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home),
    path('add',views.add_money,name='add'),
    path('exp',views.add_expence,name='exp'),
    path('bal',views.view_balance,name='bal'),
    path('history',views.view_expence,name='history'),
]

