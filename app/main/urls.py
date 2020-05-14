from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('fridge/', views.fridge, name='fridge'),
    path('memo/', views.memo, name='memo'),
    path('menu/', views.menu, name='menu'),
    path('recommendation/', views.recommendation, name='recommendation'),
]
