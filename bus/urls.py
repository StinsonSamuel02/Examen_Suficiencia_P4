from django.urls import path

from .views import *

urlpatterns = [
    path('', buses, name='buses'),
    path('edit/<int:id>', edit, name='edit_bus'),
    path('delete/<int:id>', delete, name='delete_bus'),
]
