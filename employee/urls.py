from django.urls import path

from .views import *

urlpatterns = [
    path('', employees, name='employees'),
    path('edit/<int:id>', edit, name='edit_employee'),
    path('delete/<int:id>', delete, name='delete_employee'),
]
