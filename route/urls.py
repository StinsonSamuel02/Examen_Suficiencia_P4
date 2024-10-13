from django.urls import path

from .views import *

urlpatterns = [
    path('', routes, name='routes'),
    path('create/', create, name='create_route'),
    path('edit/<int:id>', edit, name='edit_route'),
    path('edit-route/<int:id>', edit_route, name='edit_route_route'),
    path('delete/<int:id>', delete, name='delete_route'),
]
