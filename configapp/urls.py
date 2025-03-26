
from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name='home'),
    path('', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
]