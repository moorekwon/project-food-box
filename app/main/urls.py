from django.urls import path

from main import views

urlpatterns = [
    path('', views.base, name='base'),
]