from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', signin, name='login'),
    path('accounts/logout/', signout, name='logout')
]
