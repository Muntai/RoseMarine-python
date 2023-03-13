from django.urls import path
from . import views

urlpatterns = [
    path('', views.kuhnya, name='kuhnya'),
    path('pershi_stravi', views.pershi_stravi, name='pershi_stravi'),
]
