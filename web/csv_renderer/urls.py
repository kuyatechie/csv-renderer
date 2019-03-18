from django.urls import path

from . import views

urlpatterns = [
    path('list', views.file_list, name='list'),
    path('file/<str:filename>', views.index, name='csv'),
]