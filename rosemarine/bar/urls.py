from django.urls import path
from . import views

urlpatterns = [
    path('', views.bar, name='bar'),
    path('firmovi_limonadi', views.firmovi_limonadi, name='firmovi_limonadi'),
]
